import os 
os.system("clear")

def converter_centimetros(numero):
    return numero * 100

numero = float(input("Digite o valor em metros: "))

centimetros = converter_centimetros(numero)

print(f"Convertendo {numero} m em centímetros é: {centimetros} cm.")