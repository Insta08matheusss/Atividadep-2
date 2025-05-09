import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str

lista_clientes = []
QUANTIDADE_CLIENTES = 2

print("Informe os dados do cliente")
for i in range(QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome = input("Nome: "),
        email = input("E-mail: "),
        telefone = input("Telefone: ")
        )
    lista_clientes.append(cliente)

print("\n Exibindo dados clientes")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"E-mail: {cliente.email}")
    print(f"Telefone: {cliente.telefone}")

nome_arquivo = "dados_clientes.txt"

with open(nome_arquivo, "a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome}, {cliente.email},{cliente.telefone}\n")

print("\nSalvo")