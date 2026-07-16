#função recursiva para a sequência 
def seuqncia_fun(dia):

    #caso base, será quando dia for 0 e dia for 1
    if dia == 0:
        dia = 0 
        return dia
    
    elif dia == 1:
        dia = 1
        return dia
    
    else:
        quantidade = seuqncia_fun(dia - 1) + seuqncia_fun(dia - 2)
        return quantidade

print("Espelho, espelho meu, quantas maçãs a árvore deu?")
dia_colheita = int(input())

quantidade_macas = seuqncia_fun(dia_colheita)
print(f"A árvore rendeu {quantidade_macas} maçãs no dia {dia_colheita}.")

#a divisão será relacionada a qtd de maçãs 
if quantidade_macas < 7:
    print("Oh não! A colheita não foi suficiente para os sete anões.")

else:
    if quantidade_macas >= 7:

        #divisão inteira por 7, para saber a qtd de maçãs para cada anão
        macas_anao = quantidade_macas // 7

        #resto da divisão por 7, para saber a qtd de maçãs que a Branca de Neve vai ficar 
        sobra_branca = quantidade_macas % 7

        print(f"Cada anão receberá {macas_anao} maçã(s) e Branca de Neve ficará com a sobra de {sobra_branca} maçã(s).")

        #caso especial
        if quantidade_macas % 7 == 0:
            print("A divisão foi perfeita! Nenhuma maçã sobrou para a torta da Branca de Neve.")

    