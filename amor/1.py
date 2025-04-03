import os
os.system("clear")

print("""
 ==========Quer Namorar Comigo?======
            codigo|resposta
            1     |    sim
            2     |    não
 """)

namoro = input("Quer namorar comigo? ").lower()

if namoro == "1":
    print("Eu te amo meu amor!!")
elif namoro == "2":
    print("VA TOMAR EM SEU CU ENTÃO")