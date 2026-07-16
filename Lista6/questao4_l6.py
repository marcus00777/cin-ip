dicionario = {"EN": {}, "ES": {}}   #Dicionário para salvar as palvras

n = int(input())

for i in range(n):
    informacoes = input().split()

    #Coletando a operação e o idioma
    operacao = informacoes[0]
    idioma = informacoes[1]

    #Se operação for 1 a palavra será registrada 
    if operacao == "1":
        ptbr = informacoes[2]
        estrangeira = informacoes[3]

        dicionario[idioma][estrangeira] = ptbr

    #Tradução da frase
    elif operacao == "2":
        frase = informacoes[2:]

        traducao = []
        conseguiu = True

        for p in frase:
            if p in dicionario[idioma]:
                traducao.append(dicionario[idioma][p])

            else:
                conseguiu = False

        #Se conseguir traduzir a palavra 
        if conseguiu:
            print(" ".join(traducao))   

        else:
            print(f"Não entendi nada daqui, faltam palavras no meu dicionário de {idioma}!")
