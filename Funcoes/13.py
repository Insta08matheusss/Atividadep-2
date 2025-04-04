import os 
os.system("clear")


def inflaciona(preco):
    if preco < 100:
        valor = preco * 1.10
    else:
        valor = preco * 1.20
        return valor
    
preco = float(input("Digite o valor do produto: "))

preco_final = inflaciona(preco)

print(f"Preço final: {preco_final: 2f}")