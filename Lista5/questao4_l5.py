def recursao(matriz, palavra, i, j, m, n, maxima, erros, visitados):

    #se sair da matriz
    if i < 0 or i >= m or j < 0 or j >= n:
        return 0
    #se a posição for 0
    if matriz[i][j] == "0":
        return 0
    
    if visitados[i][j]:
        return 0
    
    #se letras não pertencerem a palavra-chave 
    if matriz[i][j] != "2" and matriz[i][j] not in palavra:
        erros += 1

    #se pisar mais do que permitido em letras que não estejam na palavra-chave
    if erros > maxima:
        return 0
    
    #se chegou ao destino
    if matriz[i][j] == "2":
        return True
    
    visitados[i][j] = True

    dx = [1, -1 ,0, 0]
    dy = [0, 0, -1, 1]

    for d in range(4):
       if recursao(matriz, palavra, i + dx[d], j + dy[d], m, n, maxima, erros, visitados):
           return True
       
    visitados[i][j] = False
    return False

print("Eu te amo tanto agora quanto da primeira vez em que eu vi você...")
print("O mapa da floresta me parece esquisito, certo Pascal?")
tamanho_matriz = int(input())

print("Minha querida Rapunzel, a palavra-chave é?")
palavra = input().upper()

m, n = input().split()
m, n = int(m), int(n)
print("Vamos por aqui, esse deve ser o local certo para se descer!")

matriz = []
print("Segundo o mapa essas são as informações da floresta:")
for i in range(tamanho_matriz):
    linha = list(input().replace(' ', ''))
    matriz.append(linha)   

print("Eu não tenho todo o tempo do mundo!")
quantidade_maxima = int(input())

visitados = [] 
for _ in range(tamanho_matriz):
    visitados.append([False] * tamanho_matriz)

resultado = recursao(matriz, palavra, m, n, tamanho_matriz, tamanho_matriz, quantidade_maxima, 0, visitados)

#se conseguir chegar ao destino 
if resultado == True:
    print("A CAÇADA TERMINOU! O SOL BRILHA NO HORIZONTE E O PIQUE-NIQUE REAL ESTÁ SERVIDO! JOSÉ FINALMENTE PODE DESCANSAR ENQUANTO PASCAL VIGIA A TORTA DE MAÇÃ.")

else:
    print("O SOL SE PÔS NO REINO DE CORONA E AS ÚLTIMAS LANTERNAS SE APAGARAM. JOSÉ BEZERRA VAGOU POR HORAS, MAS O DESTINO FOI CRUEL: ELE NÃO CHEGOU AO PIQUE-NIQUE. ENQUANTO O CAVALO MAXIMUS SE DELICIA COM A ÚLTIMA FATIA DE TORTA DE MAÇÃ, JOSÉ TERÁ QUE SE CONTENTAR EM DIVIDIR UMA FRUTA SILVESTRE AZEDA COM O PASCAL. A CAÇADA FOI UM FRACASSO E A FOME VENCEU DESTA VEZ.")



