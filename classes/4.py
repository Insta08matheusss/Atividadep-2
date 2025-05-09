import os
from dataclasses import dataclass
os.system("clear")

@dataclass
class Endereco:
    logradouro: str
    numero: int
@dataclass
class Email:
    email : str
@dataclass
class Pessoa:
    nome: str
    email: Email
    endeco: Endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, número: {self.endereco.numero}")


endereco1 = Endereco("Rua A", 23)
email1 = Email("mtfranca06@gmail.com")
pessoa1 = Pessoa("Marta", email1, endereco1)
pessoa1.exibir_dados()

print()

endereco2 = Endereco("Rua das Ostras", 14)
email2 = Email("contatomatheus48@gmail.com")
pessoa2 = Pessoa("Julia", email2, endereco2)
pessoa2.exibir_dados()