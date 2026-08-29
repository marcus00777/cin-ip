destino_visita = input()
nivel_carisma = int(input())
interesse_ful = int(input())
interesse_ten = int(input())

if destino_visita == "Tsinghua" or destino_visita == "Shenzhen":

    if destino_visita == "Tsinghua":

        if nivel_carisma >= 90:

            if interesse_ful > interesse_ten:
                print("Todos os torcedores do Santa Cruz passam a ter acesso ao intercâmbio para a Tsinghua University.")

            elif interesse_ten >= interesse_ful:
                print("Os chineses gostam do Santa Cruz, mas preferem tênis de mesa e solicitam a criação do Santa Cruz Tênis de Mesa China.")

        else:
            print("Byte consegue fazer amigos na universidade, mas a paixão pelo Santa Cruz fica para a próxima.")    

    elif destino_visita == "Shenzhen":

        if interesse_ful >= 80:

            if nivel_carisma == 100:
                print("Todos os chineses passam a torcer para o Santa Cruz.")

            elif nivel_carisma < 100 and nivel_carisma >= 80:
                print("O Santa Cruz ganha um patrocínio de uma gigante de tecnologia de Shenzhen!")

            elif nivel_carisma < 80:
                print("Byte falha em converter os chineses ao Santa Cruz, mas aproveita a viagem visitando Shenzhen.")

else:
    print("Passaporte invalido. Byte deve retornar a Recife.")