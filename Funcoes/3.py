import os
os.system("cls || clear")


def tabuada(numero):
    print(f"O número informado é: {numero}")
    for i in range (1,11):
        print(f"{numero} x {i} = {i*numero}")
        
numero = int(input("Digite o número: "))
tabuada(numero)