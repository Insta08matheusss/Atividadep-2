import os
from dataclasses import dataclass
os.system("cls || clear")


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
    endereco : str

def salvar_clientes(lista):
    nome_arquivo = "dados_clientes.csv"

    with open(nome_arquivo, "a") as arquivo_clientes:
        for cliente in lista:
            arquivo_clientes.write(f"{cliente.nome_cliente}, {cliente.data_de_nascimento}, {cliente.endereco}\n")
   
    print("Dados dos clientes salvos com sucesso.")

def salvar_funcionario(lista):
    nome_arquivo = "dados_funcionario.csv"

    with open(nome_arquivo, "a") as arquivo_funcionario:
        for funcionario in lista:
            arquivo_funcionario.write(f"{funcionario.nome_funcionario}, {funcionario.data_de_admissao}, {funcionario.matricula},{funcionario.matricula},{funcionario.rg},{funcionario.cpf}\n")
   
    print("Dados dos clientes salvos com sucesso.")

lista_funcinarios = []
lista_clientes = []

QUANTIDADE_TOTAL = 1

for i in range(QUANTIDADE_TOTAL): 
    print("==Dados do funcionário==")
    funcionario = Funcionario(
        nome_funcionario = input("Digite seu nome: "),
        data_de_admissao = input("Digite sua data de admissão: "),
        matricula = input("Digite sua matrícula: "),
        rg = input("Digite seu Rg: "),
        cpf = input("Digite seu CPF: ")  
                )
    lista_funcinarios.append(funcionario)
    print()

    print("==Dados do cliente==")
    cliente = Cliente(

        nome_cliente = input("Digite seu nome: "),
        data_de_nascimento = input("Digite sua data de nascimento: "),
        endereco = input("Digite seu endereço: ")
    )
    lista_clientes.append(cliente)

for i in range(QUANTIDADE_TOTAL):
    for funcionario in lista_funcinarios:       
        print(f"Nome do funcionário: {funcionario.nome_funcionario}"),
        print(f"Matrícula: {funcionario.matricula}"),
        print(f"Rg: {funcionario.rg}"),
        print(f"CPF: {funcionario.cpf}")
    for cliente in lista_clientes:
        print(f"Nome do cliente: {cliente.nome_cliente}"),
        print(f"Data de nascimento: {cliente.data_de_nascimento}"),
        print(f"Endereço: {cliente.endereco}")

salvar_funcionario(lista_funcinarios)
salvar_clientes(lista_clientes)