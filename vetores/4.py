import os 
os.system("clear")

lista_de_numeros = []

for i in range(5):
    numeros = input(f"Digite seu {i+1}° número: ")
    lista_de_numeros.append(numeros)
    maior_número = max(lista_de_numeros)
    menor_numero = min(lista_de_numeros)


print()
for i, numeros in enumerate(lista_de_numeros, start=1):
    print(f"{i}° Número: {numeros}")

print(f"Maior número: {maior_número}")
print(f"Menor número: {menor_numero}")


