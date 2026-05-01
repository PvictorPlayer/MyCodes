import os
import json
import hashlib
import getpass as gp

def Login():

    with open("programaçao/usuarios.json", 'a'):
        pass
    try:
        with open('programaçao/usuarios.json', 'r') as arquivo:
            usuarios = json.load(arquivo)
    except:
        usuarios = {}

    logado = False

    print("Bem-vindo ao Nosso Site!\nPara prosseguir Faça a escolha a seguir")

    while True:

        if logado == False:
            print("\n1-Cadastre-se\n2-Login\n3-sair")
            escolha = (input("Escolha: "))

            # cadastro

            if escolha == '1' and logado == False:
                user = input("Digite seu novo seu username: ").strip().lower()
                senha = gp.getpass("Digite sua nova senha: ")

                senha_hash = hashlib.sha256(senha.encode()).hexdigest()
                      
                print("Parabéns, você foi cadastrado!")
                usuarios[user] = {
                    "senha": senha_hash,
                    "logado": False
                }
                with open('programaçao/usuarios.json', 'w') as arquivo:
                    json.dump(usuarios, arquivo, indent=4) 

            # login

            elif escolha == '2' and logado == False:
                user = input("insira seu username: ")
                senha = gp.getpass("insira sua senha: ")

                senha_hash = hashlib.sha256(senha.encode()).hexdigest()

                if user in usuarios and usuarios[user]["senha"] == senha_hash:
                    print("\nParabéns, você logou!")
                    usuarios[user]["logado"] = True
                    logado = True
                    with open("programaçao/usuarios.json", "w") as arquivo:
                        json.dump(usuarios, arquivo, indent=4)
                else:
                    print("Erro")
            elif escolha.lower() == '3':
                print("saindo...")
                break
            else:
                print("Escolha Inválida!")
                continue

        else:
            print("\n1-Ver nome\n2-Logout\n3-sair")
            escolha = (input("Escolha: "))
            if escolha == '1':
                print(f"Seu nome de usuario é {user}")
            elif escolha == '2':
                os.system('cls')
                logado = False
            elif escolha.lower() == "3":
                print("saindo...")
                break
    return logado
Login()