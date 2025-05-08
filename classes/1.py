import os
from dataclasses import dataclass
os.system("clear")


@dataclass
class Pessoa:
    nome: str
    idade: int
@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

pessoa1 = Pessoa("Alice", 30)
pessoa2 = Pessoa("Bob", 25)

pet1 = Pet("Totó", 4, 7.8)
pet2 = Pet("Tubarão", 6, 9.2)

print("\n= Dados da pessoa =")
print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade} anos.")
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade} anos.")

print("\n= Dados da pessoa =")
print(f"Nome: {pet1.nome}, Idade: {pet1.idade} anos.")
print(f"Nome: {pet2.nome}, Idade: {pet2.idade} anos.")

