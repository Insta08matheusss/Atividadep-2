import os 
os.system ("clear")

def dois(par_impar):
    os.system("clear")
    print(f"Seu número é: {par_impar}")
    if numero % 2 == 1:
        print("Seu número é impar")
    else:
        print("Seu numero é par")

numero = int(input("Digite seu número: "))
dois(numero)