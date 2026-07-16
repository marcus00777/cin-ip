print("Conexão CBF e CIn-UFPE estabelecida! Processando os dados da convocação rumo ao Hexa...\n")

dicionario = {}

vagas = int(input())

flag = True
analisado = 0
relatorio = ""

#Se o número de vagas for zero encerra o código
if vagas == 0:
    print("Vixe, zero vagas? Parece que a panela já ta formada e o mister já tem os 26 nomes na cabeça.")

else:

    while flag:
        relatorio = input()

        #Condição de parada do loop se receber a frase "A coletiva vai começar"
        if relatorio == "A coletiva vai começar":            
            if analisado == 0:
                print("Ue, a coletiva começou mas ninguém foi analisado? O professor vai convocar os gandulas?")
            else:
                flag = False
                
        else:
            analisado += 1
            dados = relatorio.replace("Partida: ", "")

            nome, gols, assistencias, dribles, lesao = dados.split(" - ")

            gols = int(gols)
            assistencias = int(assistencias)
            dribles = int(dribles)
            lesao = int(lesao)

            #Verificando se o jogador está no dicionário 
            jogador_dicionario = nome in dicionario

            if jogador_dicionario == True:

                gols_antigo, assistencias_ant, dribles_ant, lesao_ant = dicionario[nome]

                dicionario[nome] = (gols_antigo + gols, assistencias_ant + assistencias, dribles_ant + dribles, lesao_ant + lesao)

            else:

                dicionario[nome] = (gols, assistencias, dribles, lesao)

            if nome == "Neymar":
                if lesao == 0:
                    print("O homem jogou! A esperanca do hexa respira.")

                else:
                    print("Neymar machucou... Mas deixa ele recuperar, na Copa ele decide!")

            else:
                if lesao == 1:
                    print(f"Ih, {nome} foi pro estaleiro. Ancelotti ta preocupado.")

                else:
                    if jogador_dicionario == True:
                        print(f"Mais um jogo pra conta de {nome}.")

                    else:
                        print(f"Vamos ver o que Ancelotti achará de {nome}.")

    print()
    print("--- CONVOCADOS PARA O HEXA ---")

    convocacao_ney = False
    convocados = 0

    for posicao in range(1, vagas + 1):

        melhor_nome = ""
        melhor_score = -9999
        melhor_gols = -99999

        for nome in dicionario:

            gols, assistencias, dribles, lesoes = dicionario[nome]

            #Verificando o nome do jogador, pois se for Neymar muda o score
            if nome == "Neymar":
                score = (gols * 5) + (assistencias * 3) + dribles + 20

            else:
                score = (gols * 5) + (assistencias * 3) + dribles - (lesoes * 10)

            #Critérios para o ranking

            #Para quem possui o maior score
            if score > melhor_score:

                melhor_nome = nome
                melhor_score = score
                melhor_gols = gols

            #Se empatar, verifica o saldo de gols
            elif score == melhor_score:

                if gols > melhor_gols:

                    melhor_nome = nome
                    melhor_gols = gols

                #Se o saldo de gols empatar, ordem alfabética
                elif gols == melhor_gols:

                    if nome < melhor_nome:

                        melhor_nome = nome

        if melhor_nome != "":

            gols, assistencias, dribles, lesoes = dicionario[melhor_nome]

            if melhor_nome == "Neymar":
                score = (gols * 5) + (assistencias * 3) + dribles + 20
                convocacao_ney = True

            else:
                score = (gols * 5) + (assistencias * 3) + dribles - (lesoes * 10)

            print(f"{posicao}. {melhor_nome} - {score} pts (G: {gols}, A: {assistencias})")

            convocados += 1

            del dicionario[melhor_nome]

    # Mensagem Neymar
    if convocacao_ney:
        print("Prepara o pagode e a caixa de som, o Ney ta on!")

    else:
        print("Eita... Ancelotti bancou a tática e deixou o menino Ney de fora!")

    #Se o número de convocados for menor que o número de vagas, prints especiais 
    if convocados < vagas:
        if convocacao_ney:
            print("A lista não encheu, mas com o camisa 10 lá dentro, Ancelotti já tá com a cabeça no Hexa.")
        else:
            print("Se liga, professor... ainda tem espaço pra o Ney!")
