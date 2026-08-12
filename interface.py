import customtkinter as ctk
from tkinter import messagebox
from banco import ContaBancaria


class SistemaBancario(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.conta = ContaBancaria()
        self.title("Sistema Bancário")
        self.geometry("1100x700")
        self.minsize(900, 600)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.criar_interface()
        self.mostrar_dashboard()

    def criar_interface(self):
        self.sidebar = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(self.sidebar, text="🏦  BANCO", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(40, 50))
        self._botao_menu("🏠  Dashboard", self.mostrar_dashboard)
        self._botao_menu("💰  Depositar", self.abrir_deposito)
        self._botao_menu("💸  Sacar", self.abrir_saque)
        self._botao_menu("📄  Extrato", self.abrir_extrato)
        ctk.CTkButton(self.sidebar, text="🚪  Sair", height=45, fg_color="transparent", border_width=1, command=self.destroy).pack(side="bottom", padx=20, pady=30, fill="x")

        self.conteudo = ctk.CTkFrame(self, fg_color="transparent")
        self.conteudo.pack(side="right", fill="both", expand=True, padx=30, pady=30)

    def _botao_menu(self, texto, comando):
        ctk.CTkButton(self.sidebar, text=texto, height=45, command=comando).pack(padx=20, pady=8, fill="x")

    def limpar_conteudo(self):
        for widget in self.conteudo.winfo_children():
            widget.destroy()

    def mostrar_dashboard(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.conteudo, text="Olá, Felipe 👋", font=ctk.CTkFont(size=30, weight="bold")).pack(anchor="w")
        ctk.CTkLabel(self.conteudo, text="Bem-vindo ao seu sistema bancário.", font=ctk.CTkFont(size=15)).pack(anchor="w", pady=(5, 30))

        card = ctk.CTkFrame(self.conteudo, height=180, corner_radius=20)
        card.pack(fill="x", pady=(0, 25))
        card.pack_propagate(False)
        ctk.CTkLabel(card, text="Saldo disponível", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=30, pady=(25, 5))
        ctk.CTkLabel(card, text=f"R$ {self.conta.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."), font=ctk.CTkFont(size=36, weight="bold")).pack(anchor="w", padx=30)

        ctk.CTkLabel(self.conteudo, text="Ações rápidas", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w", pady=(0, 15))
        frame = ctk.CTkFrame(self.conteudo, fg_color="transparent")
        frame.pack(fill="x")
        frame.grid_columnconfigure((0, 1, 2), weight=1)
        for i, (texto, comando) in enumerate([("💰\nDepositar", self.abrir_deposito), ("💸\nSacar", self.abrir_saque), ("📄\nExtrato", self.abrir_extrato)]):
            ctk.CTkButton(frame, text=texto, height=100, command=comando).grid(row=0, column=i, padx=5, sticky="ew")

        info = ctk.CTkFrame(self.conteudo, corner_radius=15)
        info.pack(fill="x", pady=30)
        ctk.CTkLabel(info, text="Informações da conta", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", padx=25, pady=(20, 10))
        ctk.CTkLabel(info, text=f"Saques restantes: {self.conta.saques_restantes()}", font=ctk.CTkFont(size=15)).pack(anchor="w", padx=25, pady=(0, 20))

    def abrir_deposito(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.conteudo, text="💰 Realizar depósito", font=ctk.CTkFont(size=28, weight="bold")).pack(anchor="w", pady=(0, 30))
        frame = ctk.CTkFrame(self.conteudo, corner_radius=20)
        frame.pack(fill="x")
        ctk.CTkLabel(frame, text="Valor do depósito", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=30, pady=(30, 10))
        self.valor_deposito = ctk.CTkEntry(frame, placeholder_text="Ex: 500.00", height=50)
        self.valor_deposito.pack(padx=30, fill="x")
        ctk.CTkButton(frame, text="Confirmar depósito", height=50, command=self.realizar_deposito).pack(padx=30, pady=30, fill="x")

    def realizar_deposito(self):
        try:
            valor = float(self.valor_deposito.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")
            return
        sucesso, mensagem = self.conta.depositar(valor)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.mostrar_dashboard()
        else:
            messagebox.showerror("Erro", mensagem)

    def abrir_saque(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.conteudo, text="💸 Realizar saque", font=ctk.CTkFont(size=28, weight="bold")).pack(anchor="w", pady=(0, 30))
        frame = ctk.CTkFrame(self.conteudo, corner_radius=20)
        frame.pack(fill="x")
        ctk.CTkLabel(frame, text=f"Saldo disponível: R$ {self.conta.saldo:.2f}", font=ctk.CTkFont(size=16)).pack(anchor="w", padx=30, pady=(30, 10))
        ctk.CTkLabel(frame, text=f"Limite por saque: R$ {self.conta.LIMITE_POR_SAQUE:.2f}").pack(anchor="w", padx=30)
        ctk.CTkLabel(frame, text=f"Saques restantes: {self.conta.saques_restantes()}").pack(anchor="w", padx=30, pady=(5, 20))
        self.valor_saque = ctk.CTkEntry(frame, placeholder_text="Ex: 100.00", height=50)
        self.valor_saque.pack(padx=30, fill="x")
        ctk.CTkButton(frame, text="Confirmar saque", height=50, command=self.realizar_saque).pack(padx=30, pady=30, fill="x")

    def realizar_saque(self):
        try:
            valor = float(self.valor_saque.get().replace(",", "."))
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor válido.")
            return
        sucesso, mensagem = self.conta.sacar(valor)
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.mostrar_dashboard()
        else:
            messagebox.showerror("Erro", mensagem)

    def abrir_extrato(self):
        self.limpar_conteudo()
        ctk.CTkLabel(self.conteudo, text="📄 Extrato bancário", font=ctk.CTkFont(size=28, weight="bold")).pack(anchor="w", pady=(0, 20))
        ctk.CTkLabel(self.conteudo, text=f"Saldo atual: R$ {self.conta.saldo:.2f}", font=ctk.CTkFont(size=18, weight="bold")).pack(anchor="w", pady=(0, 20))
        tabela = ctk.CTkScrollableFrame(self.conteudo, corner_radius=15)
        tabela.pack(fill="both", expand=True)
        extrato = self.conta.obter_extrato()
        if not extrato:
            ctk.CTkLabel(tabela, text="Nenhuma movimentação registrada.", font=ctk.CTkFont(size=16)).pack(pady=40)
            return
        for movimento in reversed(extrato):
            tipo = movimento["tipo"]
            valor = movimento["valor"]
            sinal = "+" if tipo == "Depósito" else "-"
            linha = ctk.CTkFrame(tabela, height=60, corner_radius=10)
            linha.pack(fill="x", pady=5)
            ctk.CTkLabel(linha, text=tipo, font=ctk.CTkFont(size=15, weight="bold")).pack(side="left", padx=20)
            ctk.CTkLabel(linha, text=f"{sinal} R$ {valor:.2f}", font=ctk.CTkFont(size=15, weight="bold")).pack(side="right", padx=20)

    def executar(self):
        self.mainloop()
