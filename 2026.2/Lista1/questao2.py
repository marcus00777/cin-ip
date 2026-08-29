print("Byte recebeu um novo chamado! Preparando-se para a aventura...")

nivel_preparo = 0

energia_byte = int(input())

if energia_byte > 0 and energia_byte < 100:

    quantidade_petiscos = int(input())
    quantidade_agua = int(input())

    bateria_coleira = int(input())

    if bateria_coleira > 0 and bateria_coleira <= 100:
        #sim ou nao
        gps = input()

        #sim ou nao
        bolinha = input()

        #sim ou nao
        chuva = input()

        temperatura = int(input())

        #num entre 0 e 100
        intensidade_sinal = int(input())

        if intensidade_sinal > 0 and intensidade_sinal <= 100:

            if energia_byte >= 70:
                print("Byte está cheio de energia!")
                nivel_preparo += 2

            elif energia_byte < 30:
                print("Byte está muito cansado... A missão ficou mais difícil.")
                nivel_preparo -= 2

            if quantidade_agua >= 1 and quantidade_petiscos >= 2:
                print("Suprimentos preparados!")
                nivel_preparo += 2

            if bateria_coleira >= 50 and gps == "sim":
                print("Coleira tecnológica preparada!")
                nivel_preparo += 2

            elif bateria_coleira <= 20:
                print("A bateria da coleira está crítica! Isso pode atrapalhar a missão.")
                nivel_preparo -= 1

            if bolinha == "sim" or quantidade_petiscos >= 4:
                print("Byte está ainda mais animado para a aventura!")
                nivel_preparo += 1

            if chuva == "sim" or temperatura > 32:
                print("O clima não está ajudando... Isso vai dificultar a missão.")
                nivel_preparo -= 2

            if intensidade_sinal >= 70:
                print("O sinal está forte! Há algo estranho por perto...")
                nivel_preparo += 1

            print()
            print(f"Nível de preparo: {nivel_preparo}")
            if nivel_preparo >= 5:
                print("Byte está pronto! A nova aventura começa agora!")

            else:
                print("Byte ainda não está pronto. Melhor se preparar um pouco mais!")