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

        self.pegarPref()

        self.pegarAssis()

        self.pegarSaude()

        self.pegarEduc()

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
        
    def pegarPref(self):
        self.prefeituraget = self.prefeitura.get()

        if self.prefeituraget != "":
            pref_int = (self.prefeituraget) 
            pref_int = pref_int.replace(',', '.')
        pref_int = list(map(float, pref_int.split()))
        self.preftotal = sum(pref_int)

        self.pref.configure(text=f"Prefeitura: {self.preftotal}")

    def pegarAssis(self):
        self.assistenciaget = self.assistencia.get()

        if self.assistenciaget != "":
            assis_int = (self.assistenciaget)

        assis_int = assis_int.replace(',', '.')
        assis_int = list(map(float, assis_int.split()))
        self.assistotal = sum(assis_int)

        self.assis.configure(text=f"Assistência: {self.assistotal}")

    def pegarSaude(self):

        self.saudeget = self.saude.get()
        if self.saudeget != "":
            saude_int = (self.saudeget)
        
        saude_int = saude_int.replace(',', '.')
        saude_int = list(map(float, saude_int.split()))
        self.saudetotal = sum(saude_int)

        self.sau.configure(text=f"Saúde: {self.saudetotal}")

    def pegarEduc(self):
        self.educacaoget = self.educacao.get()
        if self.educacaoget != "":
            educ_int = (self.educacaoget)

        educ_int = educ_int.replace(',', '.')
        educ_int = list(map(float, educ_int.split()))
        self.eductotal = sum(educ_int)

        self.educ.configure(text=f"Educação: {self.eductotal}")

    def botao(self):
        self.button = ctk.CTkButton(self.principal,
                               text="Solicitar",
                               command=self.pegar)
        self.button.pack()
    


janela = aplicativo()
janela.mainloop()