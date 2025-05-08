import os
os.system("clear")

def calcular_media(lista):
    media = sum(lista) / len(lista)
    return media

lista_notas = []
quantidade_notas = 2 

for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+1}° nota: "))

for i in range(quantidade_notas):
    nota = float(input(f"Digite a {i+}"))

media = calcular_media(lista_notas)

print(f"\nMédia: {media}")
