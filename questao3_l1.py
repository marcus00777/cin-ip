Alien = input()

print('Ben: Tá na hora de virar herói!')

if Alien == 'Chama' or Alien == 'XLR8' or Alien == 'Diamante' or Alien == 'Besta' or Alien == 'Ultra-T' :
    print(f'Ben: Bora lá, {Alien}!')
    print('Gwen: Boa, Ben, agora vamos, temos que encontrar Azmuth.')

    if Alien == "XLR8":
        print('Ben: Vamos encontrar ele bem rápido com o XLR8!')

    elif Alien == 'Chama':
        print('Ben: Eu tô pegando fogo!')

elif Alien == 'Insectoide' :
     print(f'Ben: Droga, Não consigo me transformar no {Alien}.')
     print('Gwen: Ben Tennyson! Pare com a Bobeira.')
     print('Gwen: Ben, de todos os seus bichos, você tentou escolher esse?')

elif Alien == 'Fantasmático':
     print(f'Ben: Droga, Não consigo me transformar no {Alien}.')
     print('Gwen: Ben Tennyson! Pare com a Bobeira.')
     print("Ben: Zs'skayr... Ainda bem que o relógio não funcionou.")

else:
    print(f'Ben: Droga, Não consigo me transformar no {Alien}.')
    print('Gwen: Ben Tennyson! Pare com a Bobeira.')
