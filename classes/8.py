import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Endereco:
    longradouro: str
    numero : int

@dataclass
class Funcionario:
    nome_funcionario: str
    data_de_admissao : int
    matricula : int
    rg : int
    cpf : int
@dataclass
class Cliente:
    nome_cliente: str
    data_de_nascimento: int
    endereco : Endereco

lista_funcinarios = []
lista_clientes = []
QUANTIDADE_DE_FUNCIONARIOS = 3
QUANTIDADE_DE_CLIENTES = 3

for i in range(QUANTIDADE_DE_FUNCIONARIOS):
    funcionario = Funcionario(
        nome_funcionario = input("Digite seu nome: "),
        data_de_admissao = int(input("Digite sua data de admissão: ")),
        matricula = int(input("Digite sua matrícula: ")),
        rg = int(input("Digite seu Rg: ")),
        cpf = int(input("Digite seu CPF: "))   
                )

for i in range(QUANTIDADE_DE_CLIENTES):
    cliente = Cliente(

        nome_cliente = input("Digite seu nome: "),
        data_de_nascimento = int(input("Digite sua data de nascimento: ")),
        endereco = input("Digite seu endereço: ")
    )

for i in range(3):
    for funcionario in lista_funcinarios:       
        print(f"Nome do funcionário: {funcionario.nome_funcionario}"),
        print(f"Matrícula: {funcionario.matricula}"),
        print(f"Rg: {funcionario.rg}"),
        print(f"CPF: {funcionario.cpf}")
    for cliente in lista_clientes:
        print(f"Nome do cliente: {cliente.nome_cliente}"),
        print(f"Data de nascimento: {cliente.data_de_nascimento}"),
        print(f"Endereço: {cliente.endereco}")
