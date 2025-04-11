import os
os.system("clear")

lesta_de_compras = []
quantidade = 3

print("= Lista de controle =")

for i in range(quantidade):
    item = input(f"Digite o {i+1}° intem para lista: ")
    lesta_de_compras.append(item)

print("\n= ITENS DA LISTA =")
for i, item in enumerate(lesta_de_compras):
    print(f"{i}° item: {item}")