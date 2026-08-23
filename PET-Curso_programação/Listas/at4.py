"""Faça um programa que leia uma lista de 10 letras e exiba a 
letra e a quantidade de repetições de cada letra. """

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ") 
    lista.append(letras)

print(lista)

primeira = ""

for i in range(10):

    vezes = lista.count(lista[i])

    if primeira != lista[i]:
        print(f"A letra {lista[i]} apareceu {vezes} vezes")

    primeira = lista[i]