from classes.clientes import Cliente
from classes.contas import Conta

joao = Cliente("Joao da Silva", "777-1234")
maria = Cliente("Maria da Silva", "555-4321")

conta = Conta([joao, maria], "999-111")
