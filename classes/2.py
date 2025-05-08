import os
from dataclasses import dataclass
os.system("clear")


@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: "))

)

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade} anos, Peso: {pessoa1.peso:.2f} kg, Altura {pessoa1.altura:.2f}")