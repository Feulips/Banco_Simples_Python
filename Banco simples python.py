print("Seja bem-vindo")
print("Escolha as opcoes abaixo")
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

saldo = 0
limite = 300
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente.")
        elif valor > limite:
            print("Valor excede o limite por saque.")
        elif numero_de_saques >= LIMITE_SAQUES:
            print("Número máximo de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Valor inválido para saque.")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo: R$ {saldo:.2f}")
        print("=============================\n")
    
    elif opcao == "q":
        print("Saindo...")
        break
    else:
        print("Opção não válida.")