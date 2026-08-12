# 🏦 Sistema Bancário em Python

Um sistema bancário simples desenvolvido em Python, contendo funcionalidades de **depósito**, **saque**, **extrato** e **controle de limites diários**.  
Projeto criado para fins de estudo e prática de lógica de programação.

---

## 📌 Funcionalidades

### ✔ Depósito  
- Permite adicionar valores positivos ao saldo.
- Movimentação registrada automaticamente no extrato.

### ✔ Saque  
- Verifica:
  - Saldo disponível;
  - Limite máximo por saque (R$ 300,00);
  - Limite diário de 3 saques.
- Movimentação registrada no extrato.

### ✔ Extrato  
- Exibe todas as movimentações realizadas.
- Mostra o saldo atual formatado.

### ✔ Sair  
- Encerra o sistema com uma mensagem de despedida.

---

## 🧠 Lógica Utilizada

O programa utiliza:

- Estrutura de repetição `while True`
- Validação de entradas com `try / except`
- Variáveis principais:
  - `saldo`
  - `limite`
  - `numero_de_saques`
  - `LIMITE_SAQUES`
  - `extrato`
- Formatação monetária usando `f-strings`

---

## 🏗 Código Completo

```python
print("=== SISTEMA BANCÁRIO ===")
print("Bem-vindo! Escolha uma das opções abaixo.")

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

LIMITE_POR_SAQUE = 300.00
LIMITE_SAQUES = 3

saldo = 0.00
numero_de_saques = 0
extrato = []


def obter_valor(mensagem):
    """Solicita um valor numérico ao usuário."""
    try:
        return float(input(mensagem))
    except ValueError:
        print("❌ Valor inválido! Digite apenas números.")
        return None


def depositar():
    global saldo

    valor = obter_valor("Informe o valor para depósito: R$ ")

    if valor is None:
        return

    if valor <= 0:
        print("❌ O valor deve ser maior que zero.")
        return

    saldo += valor
    extrato.append(f"Depósito: +R$ {valor:.2f}")

    print("✔ Depósito realizado com sucesso!")


def sacar():
    global saldo, numero_de_saques

    if numero_de_saques >= LIMITE_SAQUES:
        print("❌ Você já atingiu o limite diário de saques.")
        return

    valor = obter_valor("Informe o valor para saque: R$ ")

    if valor is None:
        return

    if valor <= 0:
        print("❌ O valor deve ser maior que zero.")
        return

    if valor > saldo:
        print("❌ Saldo insuficiente.")
        return

    if valor > LIMITE_POR_SAQUE:
        print(
            f"❌ O limite por saque é de "
            f"R$ {LIMITE_POR_SAQUE:.2f}."
        )
        return

    saldo -= valor
    numero_de_saques += 1
    extrato.append(f"Saque: -R$ {valor:.2f}")

    print("✔ Saque realizado com sucesso!")


def mostrar_extrato():
    print("\n========== EXTRATO ==========")

    if not extrato:
        print("Nenhuma movimentação registrada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)

    print("------------------------------")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================\n")


while True:
    opcao = input(MENU).lower().strip()

    if opcao == "d":
        depositar()

    elif opcao == "s":
        sacar()

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        print("\nEncerrando o sistema...")
        print("Obrigado por usar nosso banco! 👋")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
