import os 
os.system("cls || clear")

nomes = []

#Função para ver se ta vazia

def verificar_lista_vazia(lista_nomes):
    if not lista_nomes:
        print("\nA lista está vazia")
        return True 
    return False

#Função para adicionar nomes

def adicionar(lista_nomes):
    nome = input("Digite o nome que deseja adicionar: ")
    lista_nomes.append(nome)
    print(f"\n{nome} adicionado com sucesso.")

#Função para atualizar nomes.

def atualizar(lista_nomes):
    if verificar_lista_vazia:
        return
    
    mostrar(lista_nomes)
    if nome_antigo in lista_nomes:
        novo_nome = input(f"Digite o novo nome para {nome_antigo}: ")
        indice = lista_nomes.index(nome_antigo)
        lista_nomes[indice] = novo_nome
        print(f"{nome_antigo}foi atualizado para {novo_nome}")
    else:
        print(f"\n O nome {nome_antigo} não foi encontrado.")

#Função para excluir nomes.

def excluir(lista_nomes):
    if verificar_lista_vazia(lista_nomes):
        return
    
    mostrar(lista_nomes)

    nome_remover = input("Digite o nome que deseja remover: ")
    if nome_remover in lista_nomes:
        lista_nomes.remover(nome_remover)
        print(f"{nome_remover} foi excluido com sucesso")
    else:
        print(f"O nome {nome_remover} não foi encontrado")
    

while True:
    print("==== Gerenciador de nomes ====")
    print("1 - Adicionar")
    print("2 - Lista nomes")
    print("3 - Atualizar")
    print("4 - Excluir")

    opcao = int(input("Digite uma das opçãoes acima: "))

    match opcao:
        case 1:
            adicionar(nomes)
        case 2:
            mostrar(nomes)
        case 3:
            atualizar(nomes)
        case 4:
            excluir(nomes)
        case 5:
            sair(nomes)


         
