import os
import sqlite3

from .db_agenda import (
    DBDadoAgenda,
    DBNome,
    DBTelefone,
    DBTiposTelefone,
    DBTipoTelefone,
)

BANCO = """CREATE TABLE tipos(id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT);
CREATE TABLE nomes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT);
CREATE TABLE telefones(id INTEGER PRIMARY KEY AUTOINCREMENT, id_nome INTEGER, numero TEXT, id_tipo INTEGER);
INSERT INTO tipos(descricao) VALUES ("Celular");
INSERT INTO tipos(descricao) VALUES ("Fixo");
INSERT INTO tipos(descricao) VALUES ("Fax");
INSERT INTO tipos(descricao) VALUES ("Casa");
INSERT INTO tipos(descricao) VALUES ("Trabalho");
"""


class DBAgenda:
    def __init__(self, banco) -> None:
        self.tiposTelefone = DBTiposTelefone()
        self.banco = banco
        novo: bool = not os.path.isfile(banco)
        self.conexao = sqlite3.connect(banco)
        self.conexao.row_factory = sqlite3.Row
        if novo:
            self.cria_banco()
        self.carregaTipos()

    def carregaTipos(self):
        for tipo in self.conexao.execute("SELECT * FROM tipos;"):
            id_ = tipo["id"]
            descricao = tipo["descricao"]
            self.tiposTelefone.adiciona(DBTipoTelefone(id_, descricao))

    def cria_banco(self):
        self.conexao.executescript(BANCO)

    def pesquisaNome(self, nome: DBNome):
        if not isinstance(nome, DBNome):
            raise TypeError("nome deve ser do tipo DBNome")

        achado = self.conexao.execute(
            "SELECT COUNT(*) FROM nomes WHERE nome = ?", (nome.nome,)
        ).fetchone()

        if achado[0] > 0:
            return self.carrega_por_nome(nome)
        else:
            return None

    def carrega_por_id(self, id):
        consulta = self.conexao.execute(
            "SELECT * FROM nomes where id = ?", (id,)
        )
        return self.carrega(consulta.fetchone())

    def carrega_por_nome(self, nome):
        consulta = self.conexao.execute(
            "SELECT * FROM nomes WHERE Nome = ?", (nome.nome,)
        )

        return self.carrega(consulta.fetchone())

    def carrega(self, consulta):
        if consulta is None:
            return None

        novo = DBDadoAgenda(DBNome(consulta["nome"], consulta["id"]))  # type: ignore
        for telefone in self.conexao.execute(
            "SELECT * FROM telefones WHERE id_nome = ?", (novo.nome.id,)
        ):
            ntel = DBTelefone(
                telefone["numero"], None, telefone["id"], telefone["id_nome"]
            )

            for tipo in self.tiposTelefone:
                if tipo.id == telefone["id_tipo"]:
                    ntel.tipo = tipo
                    break

            novo.telefones.adiciona(ntel)
        return

    def lista(self):
        consulta = self.conexao.execute("SELECT * FROM nomes ORDER BY nome;")

        for registro in consulta:
            yield self.carrega(registro)

    def novo(self, registro):
        try:
            cur = self.conexao.cursor()
            cur.execute(
                "INSERT INTO nomes(nome) VALUES (?)", (str(registro.nome),)
            )
            registro.nome.id = cur.lastrowid

            for telefone in registro.telefones:
                cur.execute(
                    "INSERT INTO telefones(numero, id_tipo, id_nome) VALUES(?,?,?)",
                    (telefone.numero, telefone.tipo.id, registro.nome.id),
                )

                telefone.id = cur.lastrowid

            self.conexao.commit()

        except Exception:
            self.conexao.rollback()
            raise

        finally:
            cur.close()  # type: ignore

    def atualiza(self, registro):
        try:
            cur = self.conexao.cursor()
            cur.execute(
                "UPDATE nomes SET nome = ? WHERE id = ?",
                (str(registro.nome), registro.nome.id),
            )

            for telefone in registro.telefones:
                if telefone.id is None:
                    cur.execute(
                        "INSERT INTO telefones(numero, id_tipo, id_nome) VALUES (?,?,?);",
                        (telefone.numero, telefone.tipo.id, registro.nome.id),
                    )
                    telefone.id = cur.lastrowid
                else:
                    cur.execute(
                        "UPDATE telefones SET numero = ?, id_tipo = ?, WHERE id = ?;",
                        (
                            telefone.numero,
                            telefone.tipo.id,
                            registro.nome.id,
                            telefone.id,
                        ),
                    )

                for apagado in registro.telefones.apagados:
                    cur.execute(
                        "DELETE FROM telefones WHERE id = ?", (apagado,)
                    )

                self.conexao.commit()
                registro.telefones.limpa()

        except:
            self.conexao.rollback()
            raise

        finally:
            cur.close()  # type: ignore

    def apaga(self, registro):
        try:
            cur = self.conexao.cursor()
            cur.execute(
                "DELETE FROM telefones WHERE id_nome = ?", (registro.nome.id,)
            )
            cur.execute(
                "DELETE FROM telefones WHERE id = ?", (registro.nome.id,)
            )

            self.conexao.commit()

        except Exception:
            self.conexao.rollback()
            raise

        finally:
            cur.close()  # type: ignore
