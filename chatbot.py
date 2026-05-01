import re

def responder(entrada):
    if re.search(r"\b(olá|oi|ola|eae|opa)\b", entrada):
        return "Olá, como posso ajudar?"
    elif re.search(r"\b(beleza?|tudo bem?|deboa?|como você está?)\b", entrada):
        return "tô bem, e você?"
    elif re.search(r"\b(também|tambem|bem|bem tambem|eu tambem)\b", entrada):
        return "que bom!"
    elif re.search(r"\b(rafael| Rafael)\b", entrada):
        return "O rafael é Bi😁"
    elif re.search(r"\b(Moraes|moraes)\b", entrada):
        return "O Moraes é Femboy😁"
    elif re.search(r"\b(daniel|Daniel)\b", entrada):
        return "O daniel é Macho😁"
    elif re.search(r"\b(livino|Livino)\b", entrada):
        return "O livino é Japonego😁"
    elif re.search(r"\b(hugo|Hugo)\b", entrada):
        return "O hugo é Gay😁"
    elif re.search(r"\b(de mim|mim|De mim|Mim)\b", entrada):
        return "Você parece Ser uma pessoa incrivel!"
    elif re.search(r"\b(gay|viado|veado|Gay|Viado|GAY|VIADO)\b", entrada):
        return "Eu não sou, Já você..."
    else:
        return "Desculpe, não entendi sua pergunta"
    
print("Bem-vindo ao Chatbot! Digite 'Sair' para Encerrar a interação")

while True:
    user_input = input("Você: ").lower()
    if user_input == 'sair':
        print("Chatbot: Até mais!")
        break
    resposta = responder(user_input)
    print(f"Chatbot: {resposta}")