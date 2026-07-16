#função de rescursão
def calculo_fun(pontos, *nomes):

    lista = list(nomes)

    if pontos < 1:
        print("A correnteza está muito forte... não consigo continuar.")
        return 0
    
    if lista == []:
        return pontos
    
    elemento = lista[0]
    if elemento == "Linguado":
        pontos += 1
        print("Obrigada, Linguado! Vamos rápido!")

    if elemento == "Polvo":
        pontos -= 3
        print("Cuidado com os servos da bruxa!")

    if elemento == "~":
        pontos -= 1

    if elemento.isnumeric():
        pontos -= 1

    return calculo_fun(pontos, *lista[1:])


entrada = input().split()

pontos_resistencia = 6   #vai ser usado na função

#encontrar o número dentro da lista, se ela sobreviver
soma = 0
for i in entrada:
    if i.isnumeric():
        bungigangas = int(i)
        soma += bungigangas

resultado = calculo_fun(pontos_resistencia, *entrada)
if resultado > 0:
    print(f"Eric foi salvo! E Ariel ainda guardou {soma} bugigangas na sua gruta.")

else:
    print("O príncipe afundou... Úrsula venceu desta vez.")