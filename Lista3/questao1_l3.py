print("Édipo: Inicializando sistema de embarque. Tripulantes atuais: Zaphod Beeblebrox, Ford Prefect, Arthur Dent, Marvin")

n = int(input())
dados = ["Zaphod Beeblebrox", "Ford Prefect", "Arthur Dent", "Marvin"]

for i in range(n):
    q = input()

    if "embarcar" in q:
        nome = q.replace("embarcar ", "")

        if nome == "Trillian":
            print("Finalmente alguém sensata a bordo! Bem-vinda, Trillian!")

        dados.append(nome)

    elif "priorizar" in q:

        nome = q.replace("priorizar ", "")

        if nome == "Zaphod Beeblebrox":
            print("EU SOU O PRESIDENTE DA GALAXIA! Primeiro lugar é pouco!")

        elif nome == "Ford Prefect":
            print("Sou um escritor do Guia! Mereço destaque!")

        if nome in dados:
            dados.remove(nome)
        dados.insert(0, nome)

    elif "remover" in q:

        nome = q.replace("remover ", "")

        if nome == "Marvin":
            print("Ninguem se importa comigo mesmo. Tchau")

        elif nome == "Arthur Dent":
            print("Eu só queria poder tomar chá... vou descer no próximo planeta")

        if nome in dados:
            dados.remove(nome)

    elif "mover" in q:
        partes = q.split()
        nome = " ".join(partes[1:-1]) 
        pos = int(partes[-1])  

        if nome in dados:
            dados.remove(nome)
            dados.insert(pos, nome)
if len(dados) >= 3:
    print(f"Édipo: Graças à improbabilidade, os novos comandantes são: {dados[0]}, {dados[1]} e {dados[2]}.")

elif len(dados) == 0:
    print("Édipo: Graças à improbabilidade, os novos comandantes são: ninguém... a nave está vazia!")

if len(dados) > 0:
    print ("Convocando tripulantes:")
    if len(dados) > 0 and len(dados) < 3:
        for nome in dados:
            print("- " + nome)

    elif len(dados) > 3:
        rest = dados[3:]
        for nome in rest:
            print("- " + nome)