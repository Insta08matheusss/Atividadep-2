import os 
os.system("clear")

quantidade = 6
lista_de_numeros = []

def pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        return pares, impares

for i in range(quantidade):
    numero = int(input(f"Digite o {i+1}° número: "))
    lista_de_numeros.append(numero)

pares, impares = pares_impares(lista_de_numeros)

for i, numero in enumerate(lista_de_numeros, start=1):
    print(f"{i}° número: {numero}")

print(f"Pares: {pares}")
print(f"Impares: {impares}")