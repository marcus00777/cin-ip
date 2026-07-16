#"fase de grupos" → "oitavas" → "quartas" → "semifinal" → "final"
#fase para verificar em cada seleção e analisar a pontuação

numero_selecao = int(input())
selecao = dict()

for i in range(numero_selecao):

    nome_selecao = str(input())

    selecao[nome_selecao] = {}    #cria um dicionário dentro de outro dicionário, para armazenar as fases das seleções


    frase = ''
    while frase != "*":
        frase = str(input())

        if frase != "*":
            texto, numero = frase.rsplit(" ", 1)
            numero = int(numero)

            selecao[nome_selecao][texto] = numero

pontosf = 0     #pontuação da fase de grupo
pontosO = 0     #pontuação das oitavas
pontosQ = 0     #pontuação das quartas
pontosS = 0     #pontuação das semis
pontosFi = 0    #pontuação da final

mediaf = 0     #media da fase de grupo
mediaO = 0     #media das oitavas
mediaQ = 0     #media das quartas
mediaS = 0     #media das semis
mediaFi = 0    #media da final

#percorrendo o dicionário das seleções para somar os pontos e calcular a média
for nome in selecao:
    pontuacao = selecao[nome]

    pontosf += pontuacao.get("fase de grupos", 0)
    mediaf = pontosf / len(selecao)

    pontosO += pontuacao.get("oitavas", 0)
    mediaO = pontosO / len(selecao)

    pontosQ += pontuacao.get("quartas", 0)
    mediaQ = pontosQ / len(selecao)

    pontosS += pontuacao.get("semifinal", 0)
    mediaS = pontosS / len(selecao)

    pontosFi += pontuacao.get("final", 0)
    mediaFi = pontosFi / len(selecao)

#encontrando a maior média entre as fases
maior_media = mediaf
fase = "fase de grupos"

if mediaO > maior_media:
    maior_media = mediaO
    fase = "oitavas"

if mediaQ > maior_media:
    maior_media = mediaQ
    fase = "quartas"

if mediaS > maior_media:
    maior_media = mediaS
    fase = "semifinal"

if mediaFi > maior_media:
    maior_media = mediaFi
    fase = "final"

print(fase)
print()

#tupla com as fases 
fase = ("fase de grupos", "oitavas", "quartas", "semifinal", "final")
primeira = True             #para controlar o print no inicio das fases

for f in fase:

    existe_fase = False             #verifica se as seleções possuem as fases antes de printar

    for nome in selecao:
        informac = selecao[nome]

        if f in informac:           #verifica se a fase existe em alguma seleção
            existe_fase = True

    if existe_fase:  #caso exista printa

        if not primeira:
            print()

        print(f)

        for nome_sel in selecao:
            informac = selecao[nome_sel]

            if f in informac:
                print(nome_sel, "-", informac[f])

        primeira = False
