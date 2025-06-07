from bancos import Banco
from clientes import Cliente
from contas import Conta

joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")
jose = Cliente("Jose Vargas", "9721-3000")

contaJM = Conta([joao, maria], "100")
contaJ = Conta([jose], "10")

tatu = Banco("Tatu")


tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)

contaJM.deposito(1000)
contaJ.deposito(500)
contaJM.saque(40.54)

tatu.lista_contas()


# conta = Conta([joao, maria], "999-111")

# conta1 = Conta([joao], "1", 1000)
# conta2 = Conta([maria, joao], "2", 500)

# conta1.saque(50)
# conta2.deposito(300)
# conta1.saque(190)
# conta2.deposito(95.15)
# conta2.saque(250)
# conta1.extrato()
# conta2.extrato()
