import os 
os.system ("clear")

def dois(par_impar):
    os.system("clear")
    print(f"Seu número é: {par_impar}")
    if numero > 0:
        print("Seu número é positivo")
    elif numero == 0:
        print("Seu número é neutro")
    else:
        print("Seu número é negativo")

numero = int(input("Digite seu número: "))
dois(numero)