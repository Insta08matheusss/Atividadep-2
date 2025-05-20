import os
from dataclasses import dataclass 
import time
os.system("clear")

@dataclass
class Funcionario: 
    nome: str
    cpf: str    
    cargo : str
    salario: str
    
    def mostrar_dados(self):
        print("Nome: {self.nome}")
        print("Cpf: {self.cpf}") 
        print("Cargo: {self.cargo}")
        print("Salário: {self.salario}")
        
def verificar_lista_vazia(lista):
    if not lista:
        print("\nA lista está vazia.")
        return True
    return False 

def adicionar(lista):
    print("= Digite os dados do funcionário = ")
    funcionario = Funcionario(
        nome=input("Nome: "),
        cpf=input("CPF: "),
        cargo=input("Cargo: "),
        salario=input("Salário: ")
    )
    lista.append(funcionario)
    print("Funcionário adicionado com sucesso.")
    
def mostrar(lista):
    if verificar_lista_vazia(lista):
        return
   
    print("\n= Lista de nomes =")
    for nome in lista:
        print(f"- {nome} ")
    
    
def atualizar(lista):
    if verificar_lista_vazia(lista):
        return
    
    print("\n= Lista de nomes =")
    for nome in lista:
        print(f"- {nome}")
        
    nome_atualizar = input("Digite o nome do funcionário que deseja atualizar: ")
    encontrado = False
   
    for funcionario in lista:
        if funcionario.nome == nome_atualizar:
            print("= Digite os dados do funcionário = ")
            funcionario.nome=input("Nome: ")
            funcionario.cpf=input("CPF: ")
            funcionario.cargo=input("Cargo: ")
            funcionario.salario=input("Salário: ")
            encontrado = True
            break
   
    if not encontrado:
        print(f"\nO funcionário com o nome {funcionario.nome} não foi encontrado.")
       
    mostrar(lista)
    
def excluir(lista):
    if verificar_lista_vazia(lista):
        return
    mostrar(lista) 
    funcionario_excluir = input("Digite o nome que deseja remover: ")
    for funcionario in lista:
        if funcionario.nome == funcionario_excluir:
            lista.remove(funcionario)
           
def salvar_lista(lista):
    nome_arquivo = "Funcionários.csv"
    with open(nome_arquivo, "a") as arquivo:
        for funcionario in lista:
            arquivo.write(f"{funcionario.nome}, {funcionario.cpf},{funcionario.cargo},{funcionario.salario}\n")

lista = []

# Menu.
while True:
    print("= Gerenciador de funcionários =")
    print("1 - Adicionar")
    print("2 - Ver Lista")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Sair")
   
    opcao = int(input("Digite uma das opções acima: "))
   
    match opcao:
        case 1:
            adicionar(lista)
            salvar_lista(lista)
        case 2:
            mostrar(lista)
        case 3:
            atualizar(lista)
        case 4:
            excluir(lista)
        case 5:
            print("\nSaindo do programa.")
            break
        case _:
            print("\nOpção inválida. \nTente novamente.")
    if opcao != 1:
        time.sleep(1)
    os.system("cls || clear")     
   
   
print("\nSalvo")