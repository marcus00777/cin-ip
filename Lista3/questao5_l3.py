numero_secao = int(input())
n = 2
primos = []
ocorrencia = []

if numero_secao < 9:
    print("Essa seção foi excluída por motivos que não podem ser revelados. Entre no labirinto e corra novamente.")

else:

    while n < numero_secao + 1:

        #Bertrand
        for i in range(n+1, 2*n):
            primo = True

            #encontrar primos
            for x in range(2, int(i**0.5)+1):
                if i % x == 0:
                    primo = False

            if primo:
                if i not in primos:
                    primos.append(i)

                ac = False

                for j in ocorrencia:
                    if j[0] == i:
                        j[1] += 1
                        ac = True

                if not ac:
                    ocorrencia.append([i,1])

        n = n + 1

    #bubble sort primos
    trocou = True

    while trocou:
        trocou = False

        for i in range(len(primos) - 1):
            if primos[i] < primos[i+1]:
                primos[i], primos[i+1] = primos[i+1], primos[i]
                trocou = True
    
    #bubble sort ocorrencia
    trocou = True

    while trocou:
        trocou =False

        for s in range(len(ocorrencia) - 1):
            if ocorrencia[s][0] > ocorrencia[s+1][0]:
                ocorrencia[s], ocorrencia[s+1] = ocorrencia[s+1], ocorrencia[s]
                trocou = True

      #cálculo do destino
    m = (primos[0]+1)/2

    print(*primos)

    for p, q in ocorrencia:
        print(f"O número {p} apareceu {q} vezes.")

    print()

    if m == numero_secao:
        print("Thomas: O cálculo apontou para a seção que você estava! Isso é uma armadilha.")
        print("Minho: O Thomas tem razão.")

    elif numero_secao - m == 1:
        print("Thomas: A decodificação diz que a saída está na seção imediatamente anterior a que você estava.")
        print("Minho: Se isso realmente for válido, então restam 2 opções de saída.")

    elif numero_secao - m > 1:
        print("De todos os cálculos feitos, a única seção que apresentou diferença maior do que 1 foi essa.")


