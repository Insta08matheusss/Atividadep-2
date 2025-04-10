import os
os.system("clear")

soma = 0

def calcular(soma):
    return soma / 2

for i in range(2):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = calcular(soma)

if media < 7:
    print("Reprovado")
else:
    print("Aprovado")

print(f"Média: {media}")
