import os
os.system("clear")

peso = 0
altura = 0

def numero(peso, altura):
    return peso / valor_altura


peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

valor_altura = altura * altura
total = numero(peso, altura)


print(f"Peso: {peso}")
print(f"Altura: {altura}")
os.system("clear")
print(f"Seu IMC é de: {total: .1f}")

print("""
IMC            | Classificação   | Recomendação 
Abaixo de 18.5 |Abaixo do peso   | Consulte um nutricionista para orientação
18.5 a 24.9    |Peso normal      | Matenha hábitos saudáveis
25 a 29.9      |Sobrepeso        | Considere uma dieta balanceada e atividade fisica
30 a 34.9      |Obesidade grau 1 | Procure orientação de um profissional de saúde
35 a 39.9      |Obesiadade grau 2| Consulte um médico para avaliação e orientação
40 ou mais     |Obesidade grau 3 | Busque assistência médica imediatamente!!                
""")
if total >= 40:
    print("Obesidade grau 3\nBusque assistência médica imediatamente!!")

elif total >= 30:
    print("Obesidade grau 2\nConsulte um médico para avaliação e orientação")

elif total >= 25: 
    print("Obesidade grau 1\nprocure orientação de um profissional de saúde")

elif total >=18:
    print("Peso normal\nMatenha hábitos saudáveis")

else:
    print("Abaixo do peso\nConsulte um nutricionista para orientação")
