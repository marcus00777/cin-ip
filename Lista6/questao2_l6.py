print("Somente o melhor deve ser lembrado")

#vai servir para comparar os empates, caso aconteça
ranking = ("França", "Espanha", "Argentina", "Inglaterra", "Portugal", "Brasil", "Holanda", "Marrocos", "Bélgica", "Alemanha", "Croácia", "Colômbia", "Senegal", "México", "Estados Unidos", "Uruguai", "Japão", "Suíça", "Irã", "Turquia", "Equador", "Áustria", "Coreia Do Sul", "Australia", "Argélia", "Egito", "Canadá", "Noruega", "Panamá", "Costa Do Marfim", "Suécia", "Paraguai", "Tchéquia", "Escócia", "Tunísia", "Républica Democrática Do Congo", "Uzbequistão", "Catar", "Iraque", "Africa Do Sul", "Arábia Saudita", "Jordânia", "Bósnia-Herzgovina", "Cabo Verde", "Gana", "Curaçao", "Haiti", "Nova Zelândia")
 

nome_jogador = ''
dicionario_jogadores = dict()

while nome_jogador != "FIM":

    nome_jogador = input()

    if nome_jogador != "FIM":

        #verifica a quantidade de jogadores que apareceram na entrada e as repetições dos jogadores serão os gols
        if nome_jogador in dicionario_jogadores:
            dicionario_jogadores[nome_jogador] += 1
        else:
            dicionario_jogadores[nome_jogador] = 1

 
#encontrar a posição da seleção no ranking
def ranking_pos(pais):

    pos = 0
    achou = False

    for selecao in ranking:

        if selecao == pais:
            achou = True

        if not achou:
            pos += 1

    return pos


#Primeiro jogador com mais gols

mais_gols = -1
melhor_jogador = ""

for j in dicionario_jogadores:

    gols = dicionario_jogadores[j]
    nome, pais = j.split(" - ")

    if melhor_jogador == "":

        melhor_jogador = j
        mais_gols = gols

    else:

        nome_melhor, pais_melhor = melhor_jogador.split(" - ")

        pos = ranking_pos(pais)
        pos_melhor = ranking_pos(pais_melhor)

        #quem tem mais gols vence
        if gols > mais_gols:
            melhor_jogador = j
            mais_gols = gols

        elif gols == mais_gols:
            
            #empatou o gol, ver a seleção
            if pos < pos_melhor:
                melhor_jogador = j

            elif pos == pos_melhor:

                #se persistir no empate, ordem alfabética
                if nome < nome_melhor:
                    melhor_jogador = j


del dicionario_jogadores[melhor_jogador]


# Segundo jogador com mais gols

gols2 = -1
segundo_jogador = ""

for j in dicionario_jogadores:

    gols = dicionario_jogadores[j]
    nome, pais = j.split(" - ")

    if segundo_jogador == "":

        segundo_jogador = j
        gols2 = gols

    else:

        nome_seg, pais_seg = segundo_jogador.split(" - ")

        pos = ranking_pos(pais)
        pos_seg = ranking_pos(pais_seg)

        if gols > gols2:
            segundo_jogador = j
            gols2 = gols

        elif gols == gols2:

            if pos < pos_seg:
                segundo_jogador = j
                gols2 = gols

            elif pos == pos_seg:

                if nome < nome_seg:
                    segundo_jogador = j
                    gols2 = gols


del dicionario_jogadores[segundo_jogador]


#Terceiro jogador com mais gols

gols3 = -1
terceiro_jogador = ""

for j in dicionario_jogadores:

    gols = dicionario_jogadores[j]
    nome, pais = j.split(" - ")

    if terceiro_jogador == "":

        terceiro_jogador = j
        gols3 = gols

    else:

        nome_ter, pais_ter = terceiro_jogador.split(" - ")

        pos = ranking_pos(pais)
        pos_ter = ranking_pos(pais_ter)

        if gols > gols3:
            terceiro_jogador = j
            gols3 = gols

        elif gols == gols3:

            if pos < pos_ter:
                terceiro_jogador = j
                gols3 = gols

            elif pos == pos_ter:

                if nome < nome_ter:
                    terceiro_jogador = j

#pegando apenas o nome dos jogadores
nome1, _ = melhor_jogador.split(" - ")
nome2, _ = segundo_jogador.split(" - ")
nome3, _ = terceiro_jogador.split(" - ")

print(f"O artilheiro foi {nome1} com {mais_gols} gols")
print(f"Eu poderia falar do {nome2} mas ele é somente o primeiro a ser esquecido")
print(f"O {nome3} então, nem pensar")