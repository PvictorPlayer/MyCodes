import customtkinter as ctk
from customtkinter import CTkFont

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class aplicativo(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title ("Tabela Prática")
        self.geometry("400x500")

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.principal = ctk.CTkFrame(self, width=200, fg_color="darkblue")
        self.principal.grid(row=0, column=0, sticky="nsew", padx=(10,10), pady=(10,10))

        self.construir()

        self.botao()

    def construir(self):
        # Titulo
        self.titulo = ctk.CTkLabel(self.principal,
                                    text="Tabela Prática",
                                    font=ctk.CTkFont(size=24, weight="bold"))
        self.titulo.pack(pady=10)
        
        # Prefeitura

        self.prefeitura = ctk.CTkEntry(self.principal,
                                       placeholder_text="Prefeitura:",
                                       width=200)
        self.pref = ctk.CTkLabel(self.principal,
                                 text="")
        self.prefeitura.pack()
        self.pref.pack()

        # Assistência

        self.assistencia = ctk.CTkEntry(self.principal,
                                       placeholder_text="Assistência:",
                                       width=200)
        self.assis = ctk.CTkLabel(self.principal,
                                 text="")
        self.assistencia.pack()
        self.assis.pack()

        # Saúde

        self.saude = ctk.CTkEntry(self.principal,
                                       placeholder_text="Saúde:",
                                       width=200)
        self.sau = ctk.CTkLabel(self.principal,
                                 text="")
        self.saude.pack()
        self.sau.pack()

        # Educação

        self.educacao = ctk.CTkEntry(self.principal,
                                       placeholder_text="Educação: ",
                                       width=200)
        self.educ = ctk.CTkLabel(self.principal,
                                 text="")
        self.educacao.pack()
        self.educ.pack()
        
    def somar(self, texto):
        if not texto.strip():
            return 0
        try:
            numeros = texto.replace(",", ".").split()
            return sum(map(float, numeros))
        except:
            return 0
    def pegar(self):
        self.pref.configure(text=f"Prefeitura: {self.somar(self.prefeitura.get())}")
        self.assis.configure(text=f"Assistência: {self.somar(self.assistencia.get())}")
        self.sau.configure(text=f"Saúde: {self.somar(self.saude.get())}")
        self.educ.configure(text=f"Educação: {self.somar(self.educacao.get())}")
    def botao(self):
        self.button = ctk.CTkButton(self.principal,
                               text="Solicitar",
                               command=self.pegar)
        self.button.pack()
    


janela = aplicativo()
janela.mainloop()