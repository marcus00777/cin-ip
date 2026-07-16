def recursao(matriz, i, j, m, n, espinhos, visitados):

    #se saiu da matriz
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0

    #parede, não pode passar
    if matriz[i][j] == "|":
        return 0

    #verifica se já foi visitado
    if visitados[i][j]:
        return 0

    #conta os espinhos
    if matriz[i][j] == ",":
        espinhos += 1

    # limite de espinhos, se pisar em 3 morre
    if espinhos >= 3:
        return 0

    #encontra saída possível
    if matriz[i][j] == "S":
        return 1

    visitados[i][j] = True

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    total = 0

    for d in range(4):
        total += recursao(matriz, i + dx[d], j + dy[d], m, n, espinhos, visitados)

    visitados[i][j] = False

    return total


# linhas e colunas
m = int(input())
n = int(input())

matriz = []

posicao_ini = 0
posicao_inj = 0

#adicionando os elementos na matriz
for i in range(m):

    linha = list(input())
    matriz.append(linha)

    #encontrar a posição inicial
    for j in range(n):

        if linha[j] == "J":
            posicao_ini = i
            posicao_inj = j

visitados = []

for _ in range(m):
    visitados.append([False] * n)

resultado = recursao(matriz, posicao_ini, posicao_inj, m, n, 0, visitados)

print(f"Existem {resultado} maneira(s) de sair do labirinto!")

if resultado == 0:
    print("Pelo visto Jafar conseguiu tudo que ele sempre quis, Jasmine ficara calada para sempre, ouvi dizer que ele vai espandir o reino até Ababwa")
elif resultado == 1:
    print("Ufa! Jasmine consegue escapar, mas agora precisam tirar Jafar do poder, é melhor pedirem ajuda ao gênio!")
else:
    print("Ninguém me cala! Jasmine derruba Jafar sozinha sem a ajuda de ninguém.")