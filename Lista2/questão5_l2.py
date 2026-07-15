print("Radar de Fofocas de Copacabana iniciado!")

numeros_rodada = int(input())
palavra_encontrada = 0

#Input do num de  fofoca de acordo com o núm de rodada 
for x in range(1,numeros_rodada + 1):
    ponto = 15
    numero_fofocas = int(input())
    print(f"Rodada {x}/{numeros_rodada}")
    print(f"Fofocas registradas: {numero_fofocas}")
    print("Pontuação inicial: 15")

#Input de fofoca
    todas_fof = ""
    for i in range(1,numero_fofocas + 1):
        fofoca = input()
        todas_fof += fofoca + "/"

    palavra_proibida = input()

    tentativa = ''
    todas_tent = ""

    while ponto > 0 and tentativa != "fim":
        tentativa = input()

        if tentativa != "fim":

            if tentativa + "/" in todas_tent:
                print(f"Você já investigou '{tentativa}'. Tente outra.")

            else:
                todas_tent += tentativa + "/"

                if tentativa == palavra_proibida:
                    ponto -= 5
                    print(f"Armadilha da Sueli! '{tentativa}' era proibida! -5 pontos")

#Verificando a ocorrência e se tentativa está em fofocas
                else:
                    ocorrencias = 0
                    juntar_pa = ""
                    for c in todas_fof:
                        if c != " " and c != "/":
                            juntar_pa += c
                        else:
                            if juntar_pa == tentativa:
                                ocorrencias += 1
                            juntar_pa = ""

                    if ocorrencias > 0:
                        palavra_encontrada += 1
                        ponto += 2 * ocorrencias
                        print(f"Investigação bem sucedida! '{tentativa}' apareceu {ocorrencias} vez(es).")

                    else:
                        print(f"Nada encontrado sobre '{tentativa}'. -1 ponto")
                        ponto -= 1
                print(f"Pontuação atual: {ponto}")
     
    if ponto <= 0:
            print("Você ficou sem pontos! Sueli venceu essa rodada")

    elif tentativa == "fim" :
        print(f"Rodada encerrada! Pontuação final: {ponto}")



