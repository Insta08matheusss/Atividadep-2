import os 
os.system ("clear")

def um(nota):
    os.system("clear")
    print(f"sua primeira nota: {nota}")

    

def dois(nota):
    os.system("clear")
    print(f"sua segunda nota: {nota}")


os.system("clear")

numero1 = int(input("Digite sua primeira nota: "))
um(numero1)
numero2 = int(input("Digite sua segunda nota: "))
dois(numero2)

media = (numero1 + numero2) / 2
print(f"Sua media é: {media}")

if media >= 7:
    print("Aprovado fi da puta")
else:
    print("Reprovado fi da puta")





