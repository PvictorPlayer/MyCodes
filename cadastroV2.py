import os
import sqlite3
import hashlib
import getpass as gp
from jogo import jogo

connect = sqlite3.Connection("Contas.db")
cursor = connect.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS contas_users(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL,
                senha  TEXT NOT NULL,
                logado INTEGER CHECK (logado IN (1,0))
               )""")
# cursor.execute("""INSERT INTO contas_users(
#                usuario, senha, logado) VALUES ('paulo', 'victor', 0)""")

logado = 0

while True: 
    print("Bem-vindo ao nosso site!")
    if logado == 0:  
        escolha = int(input("Selecione uma opção:\n1-cadastrar\n2-login\n3-sair\n"))
        if escolha == 1:
            user = input("Digite seu novo nome de usuário: ")
            senha = input("Digite sua nova senha: ")

            cursor.execute("""INSERT INTO contas_users(
                           usuario, senha, logado) VALUES (?,?,?)""", (user, senha, 0,))
            connect.commit()
            cursor.execute("""SELECT usuario FROM contas_users WHERE usuario = ?""", (user,))

            print("Você foi cadastrado!")
        elif escolha == 2:
            userlog = input("Digite seu username: ").lower().strip()
            senhalog = input("Digite sua senha: ").strip()

            cursor.execute("""SELECT * FROM contas_users WHERE usuario = ? AND senha = ?""", (userlog, senhalog,))
            conta = cursor.fetchone()
            if conta is not None:
                cursor.execute("""UPDATE contas_users SET logado = 1 WHERE usuario = ? AND senha = ?""", (userlog, senhalog,))
                connect.commit()
                cursor.execute("""SELECT logado FROM contas_users WHERE usuario = ? and senha = ?""", (userlog, senhalog))
                logado = cursor.fetchone()
                print("\nParabéns, você foi logado!\n")
                os.system('cls')
            else:
                print("\nUsuário ou senha incorretos\n")
        elif 3:
            break
        else:
            print("Escolha incorreta!")
    else:
        escolha = int(input("Selecione uma opção:\n1-ver usuário\n2-logout\n3-jogar!\n4-sair\n"))
        if escolha == 1:
            cursor.execute("""SELECT id, usuario, senha FROM contas_users
                            WHERE usuario = ? AND senha = ?""", (userlog, senhalog,))
            info = cursor.fetchall()
            for usuario in info:
                id_user, nome, senha = usuario
                print(f"\nid: {id_user}\nnome: {nome}\nsenha: {senha}\n")
        elif escolha == 2:
            cursor.execute("""UPDATE contas_users SET logado = 0
                            WHERE usuario = ? AND senha = ?""", (userlog, senhalog,))
            logado = 0
            connect.commit()
            if os.name == 'nt':
                os.system('cls')
            else:
                os.system('clear')
        elif 3:
            jogo()
        elif escolha == 4:
            break
        else:
            print("Escolha incorreta!")