import os
os.system("clear")

def somar(n1,n2):
    calcular = n1 + n2
    return calcular

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = somar(n1,n2)

print(f"Soma: {soma}")