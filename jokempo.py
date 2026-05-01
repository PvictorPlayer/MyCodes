import random

pontos_player = 0
pontos_pc = 0

def jogo():

    global pontos_player, pontos_pc

    print("vamos começar o pedra, papel, tesoura!\nPara sair digite 'sair'!")

    regras = {
        "pedra": "tesoura",
        "papel": "pedra",
        "tesoura": "papel"
    }

    while True:

        if pontos_pc == 10 or pontos_player == 10:
            print("o jogo acabou!")
            escolha = str( input("você quer jogar denovo?") )

            if escolha.lower().strip() == "sim":
                pontos_pc = 0
                pontos_player = 0
                jogo()
                return
            elif escolha.lower().strip() == "nao" or "não":
                pontos_player = 0
                pontos_pc = 0
                break
            else:
                print("faça uma escolha válida!")
                continue
        PCchoices = ["pedra", "papel", "tesoura"]
        pc = random.choice(PCchoices)
        playerChoices = ["pedra", "papel", "tesoura", "sair"]

        player = str( input("Digite sua escolha! ") )
        if player not in playerChoices:
            print("\nfaça uma escolha valida!\n")
            continue
        elif player == "sair":
            break
            print("o jogo  acabou!")
        else:
            print(f"minha escolha é... {pc}!")

            if player == pc:
                print("\nEmpate!\n")
            elif regras[player] == pc:
                print("\nVocê ganhou!\n")
                pontos_player += 1
                print(f"placar: Você {pontos_player} X {pontos_pc} Pc")
            else:
                print("\nVocê perdeu...\n")
                pontos_pc += 1
                print(f"placar: Você {pontos_player} X {pontos_pc} Pc")
jogo()