# Pesquisa todas as ocorrências em uma string

s: str = "um tigre, dois tigres, tres tigres"
p: int = 0

while p > -1:
    p = s.find("tigre", p)

    if p >= 0:
        print(f"posição: {p}")
        p += 1
