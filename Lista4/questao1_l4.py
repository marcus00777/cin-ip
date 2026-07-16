nome_chefe = input()
vida_chefe = 140
mascara = 5
carretel = 0

#print inicial de acordo com o nome do chefe
if nome_chefe == "Tessela":
    print("Tessela: Ha Ha Ha! Parece que a aranha retornou.\n")

elif nome_chefe == "Grande Mãe Seda":
    print("Hornet: Monarca, seu reino de tirania acaba aqui!\n")

elif nome_chefe == "A Última Juíza":
    print("Hornet: Não posso recuar agora, a cidadela está logo ali.\n")

else:
    print(f"Hornet: {nome_chefe}, levante sua lâmina!\n")


#função da hornet
#input para saber o que a Hornet irá fazer
def hornet_fun():
    return input()


#função do chefe
#input para saber o que o chefe irá fazer
def chefe_fun():
    return input()


#função de batalha
#Toda parte do cálculo e das condições da batalha, incluindo a vitória (com relatório) e a derrota de Hornet
def batalha_fun(vida_chefe, mascara, carretel):

    seda_gerada = 0
    seda_utilizada = 0
    mascara_recuperada = 0

    while vida_chefe > 0 and mascara > 0:

        #ação da Hornet
        if mascara > 0 :
            acao_h = hornet_fun()

            #Se for Ferrão
            if acao_h == "Ferrão":
                vida_chefe -= 10
                carretel = min(carretel + 2, 8)
                seda_gerada += 2

            #Se for ataque seda 
            elif acao_h == "Ataque de Seda":
                if carretel >= 3:
                    vida_chefe -= 20
                    carretel -= 3
                    seda_utilizada += 3
            
            #Se for vincular, analisando a quantidade de máscara que pode ser recuperada (máx 3)
            elif acao_h == "Vincular":
                if carretel == 8:
                    seda_utilizada += 8
                    carretel = 0
                    if mascara < 5:
                        recuperado = min(3, 5 - mascara)
                        mascara += recuperado
                        mascara_recuperada += recuperado

        #ação do chefe
        if vida_chefe > 0:
            acao_c = chefe_fun()
            if acao_c == "Acerto":
                mascara -= 1
        
            elif acao_c == "Acerto Duplo":
                mascara -= 2
                
            elif acao_c == "Errou":
                mascara += 0
    
    seda_restante = carretel
    seda_desperdicada = seda_gerada - seda_utilizada

#Resultado da batalha se hornet ganhar, ou seja, vida do chefe <= 0
    if vida_chefe <= 0:
        print("RESULTADOS DA BATALHA")
        print(f"Máscaras restantes: {mascara}")
        print(f"Máscaras recuperadas: {mascara_recuperada}")
        print(f"Seda restante: {seda_restante}")
        print(f"Seda desperdiçada: {seda_desperdicada}\n")
        print("Hornet: Não cairei tão fácil.")

#Resultado da batalha se hornet perder, ou seja, vida Hornet <= 0 
    if mascara <= 0:
        print("Hornet: Hm?")
        print(f"Vida Restante: {vida_chefe}")

    return 0

batalha_fun(vida_chefe, mascara, carretel)