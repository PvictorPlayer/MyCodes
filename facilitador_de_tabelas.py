import os

# Prefeitura, Assistencia, Saúde e educação

def facilitador():
    print("Bem-vindo ao Facilitador de Tabelas!\n".center(80))
    print("Preencha os Dados:")
    
    while True:
        pref = input("\nPrefeitura: Digite 3 valores separados por espaço: ")
        pref = pref.replace(",", ".")
        prefval = list(map(float, pref.split()))
        totalpref = sum(prefval)
        
        assis = input("\nAssistência: Digite 3 valores separados por espaço: ")
        assis = assis.replace(",", ".")
        assisval = list(map(float, assis.split()))
        totalassis = sum(assisval)

        saude = input("\nSaúde: Digite 3 valores separados por espaço: ")
        saude = saude.replace(",", ".")
        saudeval = list(map(float, saude.split()))
        totalsaude = sum(saudeval)

        educ = input("\nEducação: Digite 3 valores separados por espaço: ")
        educ = educ.replace(",", ".")
        educval = list(map(float, educ.split()))
        totaleduc = sum(educval)

        print(f"\nPrefeitura: {totalpref}\nAssistencia: {totalassis}\nSaúde: {totalsaude}\nEducação: {totaleduc}")
        break
    opcao = input("Quer repetir o processo? ")
    if opcao == "sim".lower().strip():
        facilitador()
        return
    else:
        return
facilitador()