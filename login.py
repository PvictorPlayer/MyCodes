import os

def menu():
    print("Bem-vindo ao nosso Site! Oque você gostaria de fazer?".center(50))
    
    while True:
        opcao = input("1-Criar conta\n2-Login\n3-Ver usuários\n4-Sair\n: ")

        if opcao == "1":
            usercadas = input("Digite seu username: ")
            senhacadas = input("Digite sua senha: ")
            print("\nParabéns, Você criou sua conta!\n")
        elif opcao == '2':
            username = input("username: ")
            senha = input("senha: ")
            if username.lower() == usercadas.lower() and senha == senhacadas:
                print("\nparabéns, Você está logado!\n")
            else:
                print("\nSenha ou Username incorretos!\n")
                continue
        elif opcao == '3':
            usuarios = ["ana", "pedro e", "marcos"]
            for u in usuarios:
                print(u)
        else:
            break
menu()
