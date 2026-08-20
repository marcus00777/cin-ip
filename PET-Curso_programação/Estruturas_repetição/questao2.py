#Faça um programa para, a partir de 10, escrever a contagem regressiva
#  para o lançamento de um foguete. Isto é,
#  o programa deve imprimir: 10, 9, 8, ... , 1, 0, Fogo! 

for i in range(10, -1, -1):

    print(i)

    if i == 0:
        print("Fogo!")