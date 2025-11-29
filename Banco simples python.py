print("=== Sistema Bancário ===")
print("Bem-vindo! Escolha uma das opções abaixo:\n")

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0.0
limite = 300.0
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower().strip()
    
    if opcao == "d":
        try:
            valor = float(input("Informe o valor para depósito: R$ "))
        except ValueError:
            print("❌ Valor inválido! Digite apenas números.")
            continue
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: +R$ {valor:.2f}\n"
            print("✔ Depósito realizado com sucesso!")
        else:
            print("❌ O valor deve ser maior que zero.")
    
    elif opcao == "s":
        try:
            valor = float(input("Informe o valor para saque: R$ "))
        except ValueError:
            print("❌ Valor inválido! Digite apenas números.")
            continue
        
        if valor <= 0:
            print("❌ O valor deve ser maior que zero.")
        elif valor > saldo:
            print("❌ Saldo insuficiente.")
        elif valor > limite:
            print(f"❌ Limite por saque é de R$ {limite:.2f}.")
        elif numero_de_saques >= LIMITE_SAQUES:
            print("❌ Você já atingiu o limite diário de saques.")
        else:
            saldo -= valor
            extrato += f"Saque: -R$ {valor:.2f}\n"
            numero_de_saques += 1
            print("✔ Saque realizado com sucesso!")
    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Nenhuma movimentação registrada.")
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("==============================\n")
    
    elif opcao == "q":
        print("Encerrando o sistema... Obrigado por usar nosso banco!")
        break
    
    else:
        print("❌ Opção inválida. Tente novamente.")
