import os
os.system("clear")

lista_notas = []

for i in range(3):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)

media = sum(lista_notas) / 3

print()
for nota in lista_notas:
    print(f"Nota: {nota}")

print()
print(f"Somente a primeira nota: {lista_notas[0]}")