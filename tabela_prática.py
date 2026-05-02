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

    def pegar(self):
        self.prefeituraget = self.prefeitura.get()
        self.assistenciaget = self.assistencia.get()
        self.saudeget = self.saude.get()
        self.educacaoget = self.educacao.get()
        if self.prefeituraget != "":
            pref_int = (self.prefeituraget)

        if self.assistenciaget != "":
            assis_int = (self.assistenciaget)

        if self.saudeget != "":
            saude_int = (self.saudeget)

        if self.educacaoget != "":
            educ_int = (self.educacaoget)

        pref_int = pref_int.replace(',', '.')

    def botao(self):
        self.button = ctk.CTkButton(self.principal,
                               text="enviar",
                               command=self.pegar)
        self.button.pack()
    


janela = aplicativo()
janela.mainloop()