import random

def jogo():

    contador = 0
    generated = random.randint(1, 100)
    playerInp = 0

    print("\nJogo Adivinho!\n")
    print("Número de 0 - 100 gerado!")

    while contador < 7:
        try:
            playerInp = int( input("Escolha um número!") )
        except ValueError:
            print("\nInsira um número válido!")
            jogo()
            return
        contador += 1

        if playerInp > generated:
            print("\nMuito alto!")
        elif playerInp < generated:
            print("\nMuito baixo!")
        elif playerInp == generated:
            print("\nParabéns, Você ganhou!")
            opcao = str( input("Gostaria de recomeçar?") )
            if opcao.lower() == "sim":
                jogo()
                return
            else:
                return
    if contador == 7:
        opcao = str( input("Você perdeu, Gostaria de recomeçar?") )
        if opcao.lower() == "sim":
            jogo()
            return
        else:
            return
jogo()