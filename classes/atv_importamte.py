import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Carro:
    marca: str
    modelo: str
    categoria: str
    preco: float

lista_carros = []
QUANTIDADE_CARROS = 2

for i in range(QUANTIDADE_CARROS):
    carros = Carro(
        marca = input("Digite a marca do seu carro: "),
        modelo = str(input("Digite o modelo do seu caro: ")),
        categoria = str(input("Digite a categoria do seu carro: ")),
        preco = float(input("Digite o valor do seu carro: "))
        )   
        
    lista_carros.append(carros)

print()
print(f"Marca: {carros.marca}")
print(f"Modelo: {carros.modelo}")
print(f"Categoria: {carros.categoria}")
print(f"Preço: {carros.preco}")

nome_arquivo = "carros.txt"

with open(nome_arquivo, "w") as arquivo:
    for carros in lista_carros:
        arquivo.write(f"{carros.marca}, {carros.modelo},{carros.categoria},{carros.preco}\n")

print("\nSalvo")