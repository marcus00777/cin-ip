
convocacao_brasil = {
    'Alisson': [],
    'Ederson': [],
    'Bento': [],
    'Alex Sandro': [],
    'Danilo': [],
    'Douglas Santos': [],
    'Wesley': [],
    'Marquinhos': [],
    'Gabriel Magalhães': [],
    'Bremer': [],
    'Léo Pereira': [],
    'Andrey Santos': [],
    'Bruno Guimarães': [],
    'Casemiro': [],
    'Danilo Santos': [],
    'Fabinho': [],
    'Joelinton': [],
    'Endrick': [],
    'Igor Thiago': [],
    'Gabriel Martinelli': [],
    'João Pedro': [],
    'Neymar': [],
    'Luiz Henrique': [],
    'Matheus Cunha': [],
    'Raphinha': [],
    'Vinícius Júnior': []
}

convocacao_marrocos = {
    'Bounou': [],
    'Munir Mohamedi': [],
    'El Mehdi Benabid': [],
    'Hakimi': [],
    'Mazraoui': [],
    'Aguerd': [],
    'Chadi Riad': [],
    'Yahya Attiat-Allah': [],
    'Abdelkabir Abqar': [],
    'Achraf Dari': [],
    'Ayoub El Amloud': [],
    'Amrabat': [],
    'Ounahi': [],
    'Brahim Díaz': [],
    'Bilal El Khannouss': [],
    'Ismael Saibari': [],
    'Amir Richardson': [],
    'Oussama El Azzouzi': [],
    'Amine Harit': [],
    'Ziyech': [],
    'Amine Adli': [],
    'En-Nesyri': [],
    'Ezzalzouli': [],
    'Soufiane Rahimi': [],
    'Ilias Akhomach': [],
    'Ayoub El Kaabi': []
}

titulares_marrocos = ['Bounou', 'Hakimi', 'Mazraoui', 'Aguerd', 'Chadi Riad', 'Amrabat', 'Ounahi', 'Brahim Díaz', 'Ziyech', 'Amine Adli', 'En-Nesyri']

#Fase 1 - Escalção
jogadores_campo = []     #jogadores do Brasil e Marrocos na lista
titulares_brasil = []
esquema_tatico = []
jogo_iniciado = False
jogo_valido = False

esquema = input().split("-")
esquema_valido = True

#Verificação do esquema
#se o tamanho do esquema for diferente de 3, esquema inválido
if len(esquema) != 3:
    esquema_valido = False

#Se não for valores numéricos, esquema inválido
else:
    for valor in esquema:
        if valor.isnumeric() == False:
            esquema_valido = False

#Se o esquema for válido, continua
if esquema_valido:
    defesa = int(esquema[0])
    meio = int(esquema[1])
    ataque = int(esquema[2])

    #Se alguma parte for menor que 1, esquema inválido
    if defesa < 1 or meio < 1 or ataque < 1:
        esquema_valido = False

    #Se a soma for diferente de 10, esquema inválido
    if defesa + meio + ataque != 10:
        esquema_valido = False

if esquema_valido == False:
    print("Esquema inválido!")

#Se o esquema for validado, continua
else:
        esquema_tatico.append(defesa)
        esquema_tatico.append(meio)
        esquema_tatico.append(ataque)
        
        #Coletando a escalção titular 
        goleiro = input()

        defensores = []
        for _ in range(defesa):
            d = input()
            defensores.append(d)

        meio_at = []
        for _ in range(meio):
            m = input()
            meio_at.append(m)

        atacantes = []
        for _ in range(ataque):
            a = input()
            atacantes.append(a)

        titulares_brasil.append(goleiro)

        for jogador in defensores:
            titulares_brasil.append(jogador)

        for jogador in meio_at:
            titulares_brasil.append(jogador)

        for jogador in atacantes:
            titulares_brasil.append(jogador)

        #Verificando se a escalação está correta
        escalacao_valida = True  

        for jogador in titulares_brasil:
            if jogador not in convocacao_brasil:
                escalacao_valida = False

            if titulares_brasil.count(jogador) > 1:
                escalacao_valida = False

        if escalacao_valida == False:
            print("Elenco inválido. Simulação Cancelada!")

        else:
            #se a escalação for válida
            print(f"O Brasil vem a campo com o goleiro {goleiro}.")

            print(f"A defesa é composta por {', '.join(defensores)}.")

            print(f"O meio de campo vem com {', '.join(meio_at)}.")

            print(f"E no ataque temos {', '.join(atacantes)}.")

            jogadores_campo = titulares_brasil + titulares_marrocos
            jogadores_participaram = []     #vou usar para definir o melhor da partida

            for jogador in jogadores_campo:
                jogadores_participaram.append(jogador)

            cartoes_amarelos = {}
            cartoes_vermelhos = []
            assistencias = {}
            pontuacao = {}

            for jogador in jogadores_campo:
                cartoes_amarelos[jogador] = 0
                assistencias[jogador] = []

            for jogador in jogadores_campo:
                pontuacao[jogador] = 0

            #Fase 2 - O jogo
            tempo = 1
            substituicoes_brasil = 0
            substituicoes_marrocos = 0
            jogadores_substituidos = []
            relato_partida = []
            gols_brasil = 0
            gols_marrocos = 0
            tempo_anterior = 0

            jogo_valido = True
            jogo_iniciado = False

            acabou = False  #Flag de parada do while

            #Fase 2 - O jogo
            while acabou == False:
                tempo = input()     #tempo sendo uma string númerica, para verificar as condições depois

                if tempo.upper() == "FIM":
                    acabou = True

                else:
                    entrada_valida = True
                    
                    #Se o tempo não for formado por números, entrada inválida
                    if tempo.isnumeric() == False:
                        entrada_valida = False

                    if entrada_valida:

                        tempo = int(tempo)      #convertendo o tempo para inteiro para verificar as condições dos intervalos

                        #Se o tempo não estiver no intervalo de 1 a 90, entrada inválida
                        if tempo < 1 or tempo > 90:
                            entrada_valida = False

                        #Se o tempo não for maior que o tempo anterior, entrada inválida
                        if tempo <= tempo_anterior:
                            entrada_valida = False

                    if entrada_valida == False:

                        if jogo_iniciado == False:
                            print("Entrada inválida. O jogo não foi iniciado!")

                        acabou = True

                    #Se o tempo for válido, continua
                    else:

                        jogo_iniciado = True
                        tempo_anterior = tempo      #Salva o tempo para testar novamente no loop
                        
                        #Verificando a ação e verificando se as ações são válidas ou não
                        acao = input().lower()

                        acao_valida = False

                        if acao == "gol":
                            acao_valida = True

                        if acao == "cartão amarelo":
                            acao_valida = True

                        if acao == "cartão vermelho":
                            acao_valida = True

                        if acao == "substituição":
                            acao_valida = True

                        if acao_valida == False:
                            print("Ação inválida! Simulação Cancelada")
                            jogo_valido = False
                            acabou = True

                        #Se a ação for válida, continua
                        else:
                            jogador = input()         #Recebendo o jogador que fez a ação
                            jogador_existe = False
                            if jogador in convocacao_brasil:    
                                jogador_existe = True

                            if jogador in convocacao_marrocos:
                                jogador_existe = True

                            if jogador_existe == False:
                                print("Jogador inválido. Simulação Cancelada")
                                jogo_valido = False
                                acabou = True

                            else:
                                if jogador not in jogadores_campo:
                                    print(f"{jogador} não está em campo! Simulação Cancelada")
                                    jogo_valido = False
                                    acabou = True

                                elif jogador in cartoes_vermelhos:
                                    print(f"{jogador} não está em campo! Simulação Cancelada")
                                    jogo_valido = False
                                    acabou = True

                                else:
                                    #Se foi gol
                                    if acao == "gol":
                                        if jogador in convocacao_brasil:    #Validando gol para o Brasil, se o jogador for do Brasil
                                            gols_brasil += 1

                                        else:
                                            gols_marrocos += 1      #Validando gol para o Marrocos, se o jogador for do Marrocos

                                        pontuacao[jogador] += 8

                                        #Verificando se houve assistência no gol ou não
                                        com_assistencia = input().lower()

                                        if com_assistencia == "sim":

                                            assistente = input()

                                            if assistente not in pontuacao:
                                                pontuacao[assistente] = 0

                                            pontuacao[assistente] += 5

                                            relato_partida.append(f"{tempo}'⚽ {jogador}; 🅰️ {assistente}")

                                        elif com_assistencia == "não":
                                            relato_partida.append(f"{tempo}'⚽ {jogador}")

                                        else:
                                            print("Entrada inválida!")
                                            jogo_valido = False
                                            acabou = True

                                    #Se a ação for cartão amarelo, aplica o cartão ao jogador, se for 2 cartões amarelos o jogador recebe vermelho
                                    elif acao == "cartão amarelo":
                                        cartoes_amarelos[jogador] += 1

                                        if cartoes_amarelos[jogador] == 0:
                                            pontuacao[jogador] -= 2

                                        relato_partida.append(f"{tempo}'🟨 {jogador}")

                                        if cartoes_amarelos[jogador] == 2:
                                            cartoes_vermelhos.append(jogador)
                                            pontuacao[jogador] -= 3

                                            relato_partida.append(f"{tempo}'🟥 {jogador}")
                                    
                                    #Se a ação for cartão vermelho, aplica o cartão ao jogador
                                    elif acao == "cartão vermelho":

                                        cartoes_vermelhos.append(jogador)

                                        pontuacao[jogador] -= 5

                                        relato_partida.append(f"{tempo}'🟥 {jogador}")

                                    #Se a ação for substitutição, verifica se a substituição foi de jogadores do Brasil ou do Marrocos
                                    elif acao == "substituição":

                                        jogador_substituto = input()

                                        substituicao_valida = True

                                        #substituição de jogadores brasileiros
                                        if jogador in convocacao_brasil:

                                            if substituicoes_brasil >= 5:
                                                substituicao_valida = False

                                            if jogador_substituto not in convocacao_brasil:
                                                substituicao_valida = False

                                            if jogador_substituto in jogadores_campo:
                                                substituicao_valida = False

                                            if jogador_substituto in jogadores_substituidos:
                                                substituicao_valida = False

                                            if jogador_substituto in cartoes_vermelhos:
                                                substituicao_valida = False

                                            if substituicao_valida:

                                                titulares_brasil.remove(jogador)
                                                titulares_brasil.append(jogador_substituto)

                                                jogadores_substituidos.append(jogador)

                                                jogadores_campo = titulares_brasil + titulares_marrocos

                                                substituicoes_brasil += 1

                                        #substituição dos jogadores do Marrocos
                                        elif jogador in convocacao_marrocos:

                                            if substituicoes_marrocos >= 5:
                                                substituicao_valida = False

                                            if jogador_substituto not in convocacao_marrocos:
                                                substituicao_valida = False

                                            if jogador_substituto in jogadores_campo:
                                                substituicao_valida = False

                                            if jogador_substituto in jogadores_substituidos:
                                                substituicao_valida = False

                                            if jogador_substituto in cartoes_vermelhos:
                                                substituicao_valida = False

                                            if substituicao_valida:

                                                titulares_marrocos.remove(jogador)
                                                titulares_marrocos.append(jogador_substituto)

                                                jogadores_substituidos.append(jogador)

                                                jogadores_campo = titulares_brasil + titulares_marrocos

                                                substituicoes_marrocos += 1

                                        if substituicao_valida == False:
                                            print("A substituição não pôde ser concluída! Simulação Cancelada")
                                            jogo_valido = False
                                            acabou = True

                                        else:
                                            if jogador_substituto not in pontuacao:
                                                pontuacao[jogador_substituto] = 0
                                        
                                            if jogador_substituto not in cartoes_amarelos:
                                                cartoes_amarelos[jogador_substituto] = 0

                                            if jogador_substituto not in jogadores_participaram:
                                                jogadores_participaram.append(jogador_substituto)

                                            relato_partida.append(f"{tempo}'⬆️ {jogador_substituto} ⬇️ {jogador}")

#Se o jogo foi validado
#Fase 3 Análise da Partida
if jogo_iniciado and jogo_valido:
    print()
    print(f"Fim de jogo! Brasil {gols_brasil}x{gols_marrocos} Marrocos.")

    #Relato da partida
    for i in relato_partida:
        print(i)

    #Verificando quem foi o melhor jogador, se empatar ordem alfabética
    melhor_jogador = jogadores_participaram[0]

    for jogador in jogadores_participaram:
                
        if pontuacao[jogador] > pontuacao[melhor_jogador]:
            melhor_jogador = jogador

        elif pontuacao[jogador] == pontuacao[melhor_jogador]:

            if jogador < melhor_jogador:
                melhor_jogador = jogador

    if melhor_jogador in convocacao_brasil:
        selecao = "Brasil"

    else:
        selecao = "Marrocos"

    print(f"🏆 O melhor em campo foi {melhor_jogador}, do {selecao}.")
    print()

    #Outputs do resultado
    if gols_brasil > gols_marrocos:
        if gols_brasil - gols_marrocos >= 3:
            print("QUE GOLEADA! O INÍCIO DO SONHO DO HEXA!!!")
        else:
            print("Boa vitória! Essa Copa é nossa, Brasil!")

    elif gols_marrocos > gols_brasil:
        if gols_marrocos - gols_brasil >= 3:
            print("Era melhor nem ter vindo pra essa Copa…")
        else:
            print("Foco, Brasil! Vamos nos recuperar dessa!")

    else:
        if gols_brasil == gols_marrocos == 0:
            print("Zzzzzzzzzzzzz…")
        else:
            print("Jogo difícil, mas podia ser melhor!")               