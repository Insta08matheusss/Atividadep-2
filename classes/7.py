import os
from dataclasses import dataclass
import time
os.system("clear")

while True:
    for i in range(3):
        @dataclass
        class Livro:
            titulo: str
            ano: int

        @dataclass
        class Autor:
            nome: str
            biografia: str    
            livro: Livro

            def exibir_detalhes(self):
                    print(f"Nome do livro: {self.nome}"),
                    print(f"Biografia: {self.biografia}")
                    print(f"Autor: {self.livro.titulo}, Ano: {self.livro.ano}")
                    

        
        livro = Livro("Davi Brito", 2024)
        autor = Autor("Um cara comum da Bahia","A vida de um campeão",livro )
        autor.exibir_detalhes()
    time.sleep (0.010)