import os 
os.system("clear")

preco_total = 0
pratos_solicitados = ""

while True:
    def card_matheus():
        os.system("cls || clear")
        print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
          """)
    
    print("""
    ================= MENU =================
    1 \t Picanha \t\tR$ 25,00
    2 \t Lasanha \t\tR$ 20,00
    3 \t Strogonoff \t\tR$ 18,00
    4 \t Bife acebolado \tR$ 15,00
    5 \t Pão com ovo \t\tR$ 5,00
          """)
    cmd = int(input("Qual prato vc deseja?: "))

    card_matheus()
    match cmd:
        case 1: 
            numero = "1"
            resultado = 25.00
    card_matheus()
    match cmd:
        case 2: 
            numero = "2"
            resultado = 20.00
    card_matheus()
    match cmd:
        case 3: 
            numero = "3"
            resultado = 18.00
    card_matheus()
    match cmd:
        case 4: 
            numero = "4"
            resultado = 15.00
    card_matheus()
    match cmd:
        case 5: 
            numero = "5"
            resultado = 5.0
    
    preco_total += resultado
    pratos_solicitados += ", " + numero if pratos_solicitados else numero

    mais_pedidos = input("Deseja fazer um novo pedido?\nUse 'S' or 'N' para responder: ").lower()

    if mais_pedidos == "n":
        break

total_pagar = preco_total

print(f"Pratos solicitados: {pratos_solicitados}")
print(f"Valor total: {preco_total}")

