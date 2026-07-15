coletados = []
quantidade = []
ordem = []
contador_ordem = 0

objetivos = ["Capacitor de Fluxo", "Válvula de Vácuo", "Fragmento do Ponto-Zero"]
bonus = ["Escopeta Lendária", "Vira-Vira", "Peixinho-Dourado Mítico"]
lixo = ["Lata Enferrujada", "Bota Velha", "Cogumelo Mordido"]

print("FASE 1:")
print("Marty McFly: Vamos buscar os Recursos que o Doc pediu.")
#fase 1
f = True
while f:
    coleta = input()

    if coleta == "Fim Da Coleta!":
        f = False
    else:
        itens = coleta.split(", ")

        for i in itens:
            if i in lixo:
                print("Marty McFly: Pra que eu preciso disso? Só vai encher meu inventário.")
            
            else:
                if i in coletados:
                    posicao = coletados.index(i)
                    quantidade[posicao] += 1
                else:
                    coletados.append(i)
                    quantidade.append(1)
                    ordem.append(contador_ordem)
                    contador_ordem += 1

                pos = coletados.index(i)
                qtd = quantidade[pos]

                if i in objetivos:
                    if qtd == 1:
                        print("Marty McFly: Boa Embananado, estávamos precisando disso.")
                    else:
                        print("Marty McFly: Por via das dúvidas, vamos levar mais.")

                elif i in bonus:
                    print("Marty McFly: Não podemos deixar uma raridade dessas pra trás né?!")

#ordenação
n = len(quantidade)

for i in range(n):
    for j in range(0, n - i - 1):
        if (quantidade[j] < quantidade[j + 1]) or ( quantidade[j] == quantidade[j + 1] and ordem[j] > ordem[j + 1]):
            quantidade[j], quantidade[j + 1] = quantidade[j + 1], quantidade[j]

            coletados[j], coletados[j + 1] = coletados[j + 1], coletados[j]
            
            ordem[j], ordem[j + 1] = ordem[j + 1], ordem[j]
print("Marty McFly: Nossa coleta termina aqui.")
tem_objetivo = False
pontos = 0
for i in coletados:
    if i in objetivos:
        tem_objetivo = True

if not tem_objetivo:
     print("Marty McFly: Infelizmente não encontramos nenhum dos objetivos, não poderemos continuar com a missão.")

else:
    for i in range(len(coletados)):
        it = coletados[i]
        qtd = quantidade[i]

        for _ in range(qtd):

            if it in objetivos:
                pontos = pontos + 30

            elif it in bonus:
                pontos = pontos + 10

            else:
                pontos = pontos - 5

            if pontos > 100:
                pontos = 100
            if pontos < 0:
                pontos = 0

    print(f"PONTUAÇÃO DA COLETA = {pontos}")
    if pontos < 30:
        print("Marty McFly: Pontuação Insuficiente, não poderemos continuar com a missão.")

    else:
        print()

        #Fase 2
        print("FASE 2:")
        print("Doc Brown: De onde estão vindo esses sinais de rádio-frequência dimensional? Eles formam uma matriz perfeita!")    

        linhas = int(input())
        colunas = int(input())

        matriz = []

        for q in range(linhas):
            linha = input().split(" - ")
            matriz.append([float(x) for x in linha])

        saida = [['.' for _ in range(colunas)] for _ in range(linhas)]

        q,j = 0, 0
        saida[q][j] = "X"

        movendo = True
        distancia_percorrida = 0

        while movendo:
            atual = matriz[q][j]

            melhor = atual
            nq, nj = q, j
            direcao = ''

            # cima
            if q - 1 >= 0:
                if matriz[q-1][j] > melhor:
                    melhor = matriz[q-1][j]
                    nq, nj = q-1, j
                    direcao = "^"

            # baixo
            if q + 1 < linhas:
                if matriz[q+1][j] > melhor:
                    melhor = matriz[q+1][j]
                    nq, nj = q+1, j
                    direcao = "v"

            # esquerda
            if j - 1 >= 0:
                if matriz[q][j-1] > melhor:
                    melhor = matriz[q][j-1]
                    nq, nj = q, j-1
                    direcao = "<"

            # direita
            if j + 1 < colunas:
                if matriz[q][j+1] > melhor:
                    melhor = matriz[q][j+1]
                    nq, nj = q, j+1
                    direcao = ">"

            #Parar
            if nq == q and nj == j:
                movendo = False
            else:
                saida[q][j] = direcao
                q, j = nq, nj
                saida[q][j] = "X"
                distancia_percorrida += 1

        #Print caminho
        for linha in saida:
            print("".join(linha))
    
        #Relatório
        print(f"Doc Brown: Os sinais vêm da posição [{q}][{j}]!")
        print(f"Localização triangulada com sucesso após {distancia_percorrida} movimentos pela grade dimensional.")
        print()

        #Fase 3
        print("FASE 3:")
        print("Doc Brown: Está quase tudo pronto para voltarmos para casa!")

      
        estado_inicial = input()

        atual = int(estado_inicial, 2)
        atual_fixo = atual
        alvo = 88

        trocas_totais = 0

        while atual < alvo:
            prox = atual + 1

            b1 = format(atual, '07b')
            b2 = format(prox, '07b')

            trocas = 0

            v = 0
            while v < len(b1):
                if b1[v] != b2[v]:
                    trocas += 1
                v += 1

            trocas_totais += trocas
            atual = prox

        print("SISTEMA SINCRONIZADO!")
        print(f"Doc Brown: Marty, para acelerarmos de {atual_fixo} até 88 mph, o Capacitor teve que realizar {trocas_totais} trocas de estado nos bits de processamento!")
        print("--- #1 VICTORY ROYALE: Bem-Vindos a 1985! ---")