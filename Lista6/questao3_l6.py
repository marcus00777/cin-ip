tabela_estatisca = {}
resultados = []
gols_brasil = []

gols_marcados = 0 
gols_sofridos = 0  

for i in range(6):
    informacoes = input().split()

    #modelo de entrada: Brasil 0 X 0 Marrocos, [0]: País casa, [1]: gols casa, [2]: X, [3]: gols visitante, [4]: País visitante
    selecao_casa = informacoes[0]
    gols_casa = int(informacoes[1])
    gols_visitante = int(informacoes[3])
    selecao_visitante = informacoes[4]

    tupla = (selecao_casa, gols_casa, gols_visitante, selecao_visitante)

    resultados.append(tupla)

    for selecao in [selecao_casa, selecao_visitante]:
        if selecao not in tabela_estatisca:
            tabela_estatisca[selecao] = {"pontos": 0, "vitórias": 0, "derrotas": 0, "empates": 0, "saldo": 0}

    tabela_estatisca[selecao_casa]["saldo"] += gols_casa - gols_visitante
    tabela_estatisca[selecao_visitante]["saldo"] += gols_visitante - gols_casa

    #Se o time da casa ganhar
    if gols_casa > gols_visitante:
        tabela_estatisca[selecao_casa]["pontos"] += 3
        tabela_estatisca[selecao_casa]["vitórias"] += 1
        tabela_estatisca[selecao_visitante]["derrotas"] += 1

    #Se o time visitante ganhar
    elif gols_visitante > gols_casa:
        tabela_estatisca[selecao_visitante]["pontos"] += 3
        tabela_estatisca[selecao_visitante]["vitórias"] += 1
        tabela_estatisca[selecao_casa]["derrotas"] += 1

    #Se resultar em empate
    elif gols_casa == gols_visitante:
        tabela_estatisca[selecao_casa]["pontos"] += 1
        tabela_estatisca[selecao_visitante]["pontos"] += 1
        tabela_estatisca[selecao_casa]["empates"] += 1
        tabela_estatisca[selecao_visitante]["empates"] += 1

    #Verificando que é a seleção brasileira, dependendo da entrada
    if selecao_visitante == "Brasil" or selecao_casa == "Brasil":
        if selecao_casa == "Brasil":
            gols_brasileiros = gols_casa
            gols_oponentes = gols_visitante

        if selecao_visitante == "Brasil":
            gols_brasileiros = gols_visitante
            gols_oponentes = gols_casa

        gols_marcados += gols_brasileiros
        gols_sofridos += gols_oponentes

        soma = 0
        #Quem marcou gols pela seleção brasileira
        while soma < gols_brasileiros:
            entrada_jogador = input().split()

            nome = entrada_jogador[0]
            quantidade = int(entrada_jogador[1])

            encontrado = False

            for i in range(len(gols_brasil)):

                jogador, gols = gols_brasil[i]

                if jogador == nome:
                    gols_brasil[i] = (jogador, gols + quantidade)

                    encontrado = True

            if not encontrado:
                gols_brasil.append((nome, quantidade))

            soma += quantidade




#Organizando o Ranking
ranking = list(tabela_estatisca.keys())

for i in range(len(ranking)):
    for j in range(i + 1, len(ranking)):

        selecao1 = ranking[i]
        selecao2 = ranking[j]

        dados1 = tabela_estatisca[selecao1]
        dados2 = tabela_estatisca[selecao2]

        trocar = False

        #Se tiver mais pontos troca de posição
        if dados2["pontos"] > dados1["pontos"]:
            trocar = True

        #Pontuação igual
        elif dados1["pontos"] == dados2["pontos"]:

            #verifica saldo de gols 
            if dados2["saldo"] > dados1["saldo"]:
                trocar = True

            #Saldo igual
            elif dados1["saldo"] == dados2["saldo"]:

                #Ordem alfabética
                if selecao2 < selecao1:
                    trocar = True

        if trocar:
            ranking[i], ranking[j] = ranking[j], ranking[i]

print("------- Grupo C -------")

for i in range(len(ranking)):
    selecao = ranking[i]

    dados = tabela_estatisca[selecao]

    print(f"{i+1}º | {selecao} | {dados['pontos']} | {dados['vitórias']} | {dados['derrotas']} | {dados['empates']} | {dados['saldo']}")

print()

#Informações sobre a seleção brasileira
posicao_brasil = ranking.index("Brasil") + 1   #Posição do Brasil na fase de grupo
print("-- Desempenho Brasileiro --")
print(f"Posição: {posicao_brasil}")
print(f"Gols Marcados: {gols_marcados}")
print(f"Gols Sofridos: {gols_sofridos}")

#Verificando se possui gols do Brasil
if gols_brasil:

    for jogador, gols in gols_brasil:
        print(f"{jogador}: {gols}")

    #Artilharia
    artilheiro = gols_brasil[0]

    for jogador in gols_brasil:
        if jogador[1] > artilheiro[1]:
            artilheiro = jogador
    
    print(f"Artilheiro: {artilheiro[0]}")