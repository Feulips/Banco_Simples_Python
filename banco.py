class ContaBancaria:
    LIMITE_POR_SAQUE = 300.00
    LIMITE_SAQUES = 3

    def __init__(self):
        self.saldo = 0.00
        self.numero_de_saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor <= 0:
            return False, "O valor deve ser maior que zero."

        self.saldo += valor
        self.extrato.append({"tipo": "Depósito", "valor": valor})
        return True, "Depósito realizado com sucesso!"

    def sacar(self, valor):
        if self.numero_de_saques >= self.LIMITE_SAQUES:
            return False, "Você já atingiu o limite diário de saques."
        if valor <= 0:
            return False, "O valor deve ser maior que zero."
        if valor > self.saldo:
            return False, "Saldo insuficiente."
        if valor > self.LIMITE_POR_SAQUE:
            return False, f"O limite por saque é de R$ {self.LIMITE_POR_SAQUE:.2f}."

        self.saldo -= valor
        self.numero_de_saques += 1
        self.extrato.append({"tipo": "Saque", "valor": valor})
        return True, "Saque realizado com sucesso!"

    def obter_extrato(self):
        return self.extrato

    def obter_saldo(self):
        return self.saldo

    def saques_restantes(self):
        return self.LIMITE_SAQUES - self.numero_de_saques
