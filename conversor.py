print("Bem-Vindo ao conversor de Dolár!\n".center(80))
while True:
    print("1-Real para dólar\n2-Dólar para real")
    inp = int(input("Qual operação você quer fazer: "))
    escolha = inp - 1
    match escolha:
        case 0:
            try:
                Real = int(input("Valor em Real: "))
                print(Real/5) 
            except:
                print("Digite um número válido!")
                continue
        case 1:
            try:
                Real = int(input("Valor em Real: "))
                print(Real/5) 
            except:
                print("Digite um número válido!")
                continue