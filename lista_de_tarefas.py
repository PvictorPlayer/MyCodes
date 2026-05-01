import os
import json

def listaTarefas():
    with open('programaçao/ListaDeTarefas.json', 'a'):
        pass
    try:
        with open('programaçao/ListaDeTarefas.json', 'r') as arquivo:
            lista = json.load(arquivo)
    except:
        lista = []

    print("Bem-vindo a Lista de tarefas! Faça uma escolha")

    while True:
        print("\n1-Adicionar Tarefa\n2-Remover Tarefa\n3-Marcar como feita\n4-Ver lista\n5-Sair")
        escolha = int(input("Faça sua escolha: "))

        match escolha:
            case 1:
                adicionar = input("Digite sua tarefa: ")
                lista.append(adicionar)
                with open('programaçao/ListaDeTarefas.json', 'w') as arquivo:
                    json.dump(lista, arquivo, indent=4)
            case 2:
                if not lista:
                    print("Nenhuma tarefa para remover.")
                    continue
                for ind, item in enumerate(lista):
                    print(f"{ind+1}.{item}")
                remover = int(input("Qual tarefa você quer Remover?"))
                indice = remover - 1
                removida = lista.pop(indice)
                print(f"Tarefa \"{removida}\" removida!")
                with open('programaçao/ListaDeTarefas.json', 'w') as arquivo:
                    json.dump(lista, arquivo, indent=4)
            case 3:
                for ind, item in enumerate(lista):
                    print(f"{ind+1}.{item}")
                marcar = int(input("Qual tarefa você quer marcar como feita?"))
                lista[marcar - 1] = '✓ ' + lista[marcar - 1]
                print(f"A tarefa \"{lista[marcar-1]}\" foi marcada como feita!")
                with open('programaçao/ListaDeTarefas.json', 'w') as arquivo:
                    json.dump(lista, arquivo, indent=4)
            case 4:
                print("")
                for ind, item in enumerate(lista):
                    print(f"{ind+1}.{item}")
                continue
            case 5:
                break
listaTarefas()