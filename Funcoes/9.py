import os
os.system("clear")

def somar(n1,n2):
    calcular = n1 + n2
    return calcular

def subtrair(n1,n2):
    calcular = n1 - n2
    return calcular

def multiplicar(n1,n2):
    return n1*n2

def dividir(n1,n2):
    return n1/n2

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = somar(n1, n2)
subtração = subtrair(n1, n2)
multiplicacao = multiplicar(n1,n2)
divisao = dividir(n1,n2)

print(f"Soma: {soma}")
print(f"Subtração: {subtração}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")