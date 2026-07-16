def recursao(ind, velocidade, glitch, pista, tempo):

    #caso de parada, quando percorreu todas as pistas retorna o menor tempo
    if ind == len(pista):
        return tempo
    
    tipo_terreno = pista[ind][0]
    tamanho = pista[ind][1] 
    p1 = pista[ind][2]
    p2 = pista[ind][3]

    melhor_tempo = -1

    #verificando cada ação (acelerar, manter, frear)
    for acao in [10, 0, -10]:
        velocidade_entrada = velocidade + acao

        #analisar se a velocidade é menor ou igual a 0, se tiver glich usa
        if velocidade_entrada <= 0:

            if glitch > 0:
                resposta = recursao(ind+1, 10, glitch - 1, pista, tempo)

                if resposta != -1:
                        if melhor_tempo == -1 or resposta < melhor_tempo:
                            melhor_tempo = resposta

        #se a velocidade for maior que zero
        else: 
            
            velocidade_saida = velocidade_entrada
            flag = True
            
            #se a pista for uma reta mantém a velocidade 
            if tipo_terreno == "Reta":
                velocidade_saida = velocidade_entrada

            #se a pista for uma curva, verifica se a velocidade de entrada é maior que o limite  
            elif tipo_terreno == "Curva":
                if velocidade_entrada > p1:
                    flag = False

            #se a pista for uma subida, aplica a força para trás e se possui aceleração
            elif tipo_terreno == "Subida":
                velocidade_saida = velocidade_entrada - p1
                if velocidade_saida <= 0:
                    flag = False

            #se a pista for descida, aplica a força para frente e verifica se ultrapassa o limite  
            elif tipo_terreno == "Descida":
                velocidade_saida = velocidade_entrada + p1
                if velocidade_saida > p2:
                    flag = False

            if flag:

                #tempo do trecho
                tempo_trecho = tamanho/velocidade_entrada

                resposta = recursao(ind+1, velocidade_saida, glitch, pista, tempo + tempo_trecho)
                
                if resposta != -1:
                    if melhor_tempo == -1 or resposta < melhor_tempo:
                        melhor_tempo = resposta

            #caso tenha glich e morrer ela pode voltar
            if flag == False and glitch > 0:
                resposta = recursao(ind+1, 10, glitch - 1, pista, tempo)
                
                if resposta != -1:
                    if melhor_tempo == -1 or resposta < melhor_tempo:
                        melhor_tempo = resposta

    return melhor_tempo 


print("Calibrando a gravidade e o atrito da pista...\n")
N, V0, G = input().split()
N, V0, G = int(N), int(V0), int(G)

#adicionando as informações das pistas em uma lista e perguntando as informações de acordo com o número de pistas informados
pista = []
for i in range(N):
    tipo_terreno, tamanho, p1, p2 = input().split()
    pista.append((tipo_terreno, float(tamanho), float(p1), float(p2)))
    
resultado = recursao(0, V0, G, pista, 0)

if resultado != -1:
    print(f"A corrida foi um sucesso! Tempo minimo cravado: {resultado:.2f}s.")

else:
    print("Bug fatal! Vanellope capotou e o kart virou pixels.")