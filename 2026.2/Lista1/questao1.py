print("Nossa, que lindo cavalo! Mas deixe-me verificar apenas uma coisa...")


g = int(input())

if g > 0:
    print("ARMADILHA")

    if g % 2 == 0:

        qntd_duplas = g/2
        print(f"OS GUERREIROS FORMARAM {qntd_duplas:.0f} DUPLAS")

    else:
        qntd_duplas = g // 2
        print(f"OS GUERREIROS FORMARAM {qntd_duplas:.0f} DUPLAS E UM GUERREIRO FICOU SOZINHO")
else:
    print("ENTRADA LIBERADA")