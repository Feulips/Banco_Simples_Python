# 🏦 Sistema Bancário em Python

Um sistema bancário simples desenvolvido em **Python**, criado para praticar lógica de programação, estruturas de repetição, funções, validação de dados e organização de código.

O sistema permite realizar **depósitos**, **saques**, consultar o **extrato** e controlar limites de movimentação.

---

## 📌 Funcionalidades

### 💰 Depósito

- Permite realizar depósitos com valores maiores que zero.
- Atualiza o saldo automaticamente.
- Registra a movimentação no extrato.
- Valida entradas inválidas.

### 💸 Saque

O sistema realiza algumas verificações antes de permitir o saque:

- Verifica se o valor é maior que zero;
- Verifica se existe saldo suficiente;
- Limita cada saque a **R$ 300,00**;
- Permite no máximo **3 saques por dia**;
- Registra cada saque no extrato;
- Atualiza o saldo automaticamente.

### 📄 Extrato

- Exibe todas as movimentações realizadas;
- Mostra depósitos e saques individualmente;
- Informa quando não existem movimentações;
- Exibe o saldo atual formatado em reais.

### 🚪 Sair

Encerra o sistema e exibe uma mensagem de despedida.

---

## 🧠 Conceitos praticados

O projeto utiliza diversos conceitos fundamentais de Python:

- `while True`
- `if`, `elif` e `else`
- `try / except`
- Funções
- Parâmetros e retorno
- Variáveis globais
- Listas
- `for`
- `f-strings`
- Validação de dados
- Operações matemáticas
- Manipulação de strings
- Organização e reutilização de código

---

## 🏗️ Estrutura do código

O sistema foi dividido em funções para evitar que toda a lógica fique concentrada no menu principal.

### `obter_valor()`

Responsável por receber e validar valores digitados pelo usuário.

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
