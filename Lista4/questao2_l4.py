
#função para classificar o alvo
def alvo_fun(lista_alvo):
    #a função irá analisar índices de uma lista para verificar o nível de ameaça do alvo e verificar se o alvo está armado

    if lista_alvo[1] >= 7 and lista_alvo[2] == "sim":
        classificado = "Elite"

    elif lista_alvo[1] >= 7 and lista_alvo[2] == "nao":
        classificado = "Executor"

    elif lista_alvo[1] >= 4 and lista_alvo[1] < 7 and lista_alvo[2] == "sim":
        classificado = "Veterano"
   
    elif lista_alvo[1] >= 4 and lista_alvo[1] < 7 and lista_alvo[2] == "nao":
        classificado = "Operador"

    elif lista_alvo[1] < 4:
        classificado = "Iniciante"

    return classificado

#função para analisar as tentativas
def tentativa_fun(list_tentativa):
    #a função irá somar os elementos da lista e dividir pela quantidadde de tentativa, analisando o resto da divisão entre eles
    soma = 0
    for c in list_tentativa:
        soma += c

    resultado = soma % len(list_tentativa)

    return resultado

#função para os ataques refletidos 
def ataques_fun(list_ataques_inimigos):
    #a função irá verificar os números que são múltiplos aos valores favoritos para refletir
    multiplos = []

    for num in list_ataques_inimigos:
        if num % 3 == 0 or num % 5 == 0:
            multiplos.append(num)

    return len(multiplos)


print("Entendo… Vamos começar do começo.")

dia_inicial = int(input())

rodando = True
missao = True

while dia_inicial >= 0 and rodando:
    print()
    print(f"====== Restam {dia_inicial} dias. ======")
    
    
    list_tentativa = []
    list_ataques_inimigos = []

    #musica em uma lista
    musica = input()
    print(f"Escutando: {musica}")
    musica_lst = musica.split(" - ")

    #ETAPA 1
    #alvo em uma lista para ser aplicado na função
    alvo = input()
    lista_alvo = alvo.split(" - ")
    lista_alvo[1] = int(lista_alvo[1])

    #Caso especial 
    if musica_lst[1] == "DJ Electrohead" and lista_alvo[0] == "DJ Electrohead":
        print("DJ Electrohead é morto na sua frente. Lhe avisaram para NÃO FALAR com ele.")
    

    else:
        print(f"Analisando alvo: {lista_alvo[0]}... Classificação: {alvo_fun(lista_alvo)}")
        
        #ETAPA 2
        #convertendo tentativa para uma lista (aplicação na função)
        tentativa = input().split()
        for x in tentativa:
            list_tentativa.append(int(x))

        resultado = tentativa_fun(list_tentativa)

        if resultado == 0:
            print(f"Missão Completa. | Manipulação temporal: {len(list_tentativa)} tentativa(s)")
            
            #ETAPA 3
            #convertendo ataques dos inimigos para uma lista (aplicação na função)
            ataques_inimigos = input().split()
            for v in ataques_inimigos:
                list_ataques_inimigos.append(int(v))

            print(f"Dragão refletiu {ataques_fun(list_ataques_inimigos)} ataque(s)!")

        else:
            print("Missão Fracassou! ZERO não foi capaz de assassinar o alvo e acabou morrendo. Nunca descobrirá o que realmente aconteceu.")
            rodando = False
            missao = False

    dia_inicial -= 1

if missao:
    print() 
    print("====== FIM DAS MISSÕES ======")
    print("Parabéns Subject ZERO! Seu trabalho deve ser recompensado. Nova dose do seu remédio esta aqui.")
            

