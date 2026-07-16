#Função para exibir as informações propostas em Destaque, Bola de ouro e Fim
def criterio_fun(info):
    #A função irá verificar e guardar os principais critérios de desempate

    jogador = info[0]
    dados = info[1]

    selecao = dados[0]
    gols = int(dados[1])
    assistencias = int(dados[2])
    passes = int(dados[3])
    amarelos = int(dados[4])
    vermelhos = int(dados[5])

    return(-gols, -assistencias, vermelhos, amarelos, -passes, selecao, jogador)

print("Bem, amigos da rede! Sistema de Estatísticas VAR Edition no ar. Aguardando comandos...")
dados = {}

informacoes = []
while informacoes != ["*FIM"]:
    informacoes = input().split()

    #Verificar se a entrada for para adicionar jogador
    if informacoes[0] == "*ADD":
        jogador = informacoes[1]
        selecao = informacoes[2]
        gols = int(informacoes[3])
        assistencias = int(informacoes[4])
        passes_certos = int(informacoes[5])
        cartoes_amarelos = int(informacoes[6])
        cartoes_vermelhos = int(informacoes[7])

        tupla = (selecao, gols, assistencias, passes_certos, cartoes_amarelos, cartoes_vermelhos)

        #Verificando se o jogador existe no dicionário com os dados
        if jogador in dados:
            dados_antigos = dados[jogador]

            #Se for da mesma seleção soma os valores dos dados fornecidos
            if dados_antigos[0] == selecao:
                tupla_n = (selecao, dados_antigos[1] + gols, dados_antigos[2] + assistencias, dados_antigos[3] + passes_certos, dados_antigos[4] + cartoes_amarelos, dados_antigos[5] + cartoes_vermelhos)

                dados[jogador] = tupla_n

        #Se o jogador não estiver em dados ele só adiciona o jogador e seu dados
        else:
            dados[jogador] = (selecao, gols, assistencias, passes_certos, cartoes_amarelos, cartoes_vermelhos)

    #Se a informação for para deletar, verifico se o jogador está em dados, se estiver deleta, se não estiver entra em loop
    if informacoes[0] == "*DEL":

        jogador = informacoes[1]
        selecao = informacoes[2]
        
        #Deleta
        if jogador in dados and dados[jogador][0] == selecao:
            del dados[informacoes[1]]

            print(f"O jogador: {jogador} da seleção: {selecao} foi retirado do sistema")

        #Loop
        else:
            print(f"O jogador: {jogador} da seleção: {selecao} não foi encontrado insira uma outra combinação de jogador e seleção:")
            entrada = input().split()

            while entrada[0] not in dados or dados[entrada[0]][0] != entrada[1]:
                print(f"O jogador: {entrada[0]} da seleção: {entrada[1]} não foi encontrado insira uma outra combinação de jogador e seleção:")

                entrada = input().split()   #Nome do jogador e seleção
                
            del dados[entrada[0]]
            print(f"O jogador: {entrada[0]} da seleção: {entrada[1]} foi retirado do sistema")

    #Se a informação for para buscar, exibir dados do jogador solicitado
    if informacoes[0] == "*BUSCAR":

        jogador = informacoes[1]
        selecao = informacoes[2]

        if jogador in dados and dados[jogador][0] == selecao:
            print(f"{jogador} ({selecao}): {dados[jogador][1]}G, {dados[jogador][2]}A, {dados[jogador][3]}P, {dados[jogador][4]}CA, {dados[jogador][5]}CV")

        #Caso especial da busca
        elif jogador == "Neymar":
            print("E o pessoal tá lá: 'será que Carlo Ancelotti vai convocar o Neymar?'")

        else:
            print(f"Jogador não encontrado na seleção {selecao}")

    #Se a informação for para exibir o destaque da partida
    if informacoes[0] == "*DESTAQUE_SELECAO":

        selecao = informacoes[1]

        jogadores_selecao = []

        for i in dados.items():

            if i[1][0] == selecao:
                jogadores_selecao.append(i)

        if len(jogadores_selecao) == 0:
            print(f"Nenhum dado encontrado para a seleção {selecao}")

        else:
            melhor_jogador = jogadores_selecao[0]

            for i in jogadores_selecao:
                if criterio_fun(i) < criterio_fun(melhor_jogador):
                    melhor_jogador = i

            jogador = melhor_jogador[0]
            estatisticas = melhor_jogador[1]

            print(f"Destaque da {selecao}: {jogador} {estatisticas[1]} gols, {estatisticas[2]} assistências")

    #Se a informação for Bola de ouro, exibir melhor jogador
    if informacoes[0] == "*BOLA_DE_OURO":

        if len(dados) == 0:
            print("Nenhum jogador registrado no torneio")

        else:
            jogadores = list(dados.items())

            melhor_jogador = jogadores[0]

            for i in jogadores:
                if criterio_fun(i) < criterio_fun(melhor_jogador):
                    melhor_jogador = i

            jogador = melhor_jogador[0]
            estatisticas = melhor_jogador[1]
            print(f"Bola de Ouro atual: {jogador} {estatisticas[0]} com {estatisticas[1]} gols")


    #Se a informação for Fim, encerra o torneio e exibi o ranking
    if informacoes[0] == "*FIM":

        if len(dados) == 0:
            print("Nenhum jogador registrado para o ranking final.")

        else:
            print("Ranking Final:")
            ranking = list(dados.items())

            for i in range(len(ranking)):

                melhor = i

                for j in range(i + 1, len(ranking)):
                    if criterio_fun(ranking[j]) < criterio_fun(ranking[melhor]):
                        melhor = j

                ranking[i], ranking[melhor] = ranking[melhor], ranking[i]

            for i in range(len(ranking)):
                jogador = ranking[i][0]
                estatistica = ranking[i][1]
                print(f"{i + 1}. {jogador} ({estatistica[0]}) - G: {estatistica[1]}, A: {estatistica[2]}, P: {estatistica[3]}, CA: {estatistica[4]}, CV: {estatistica[5]}")



        