"""Faça um programa que leia uma lista de 10 letras, procure por uma letra específica e troque-a por uma nova 
letra (em todas as suas ocorrências)."""

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ") 
    lista.append(letras)

print(lista)

letra_analisada = input("Qual letra você quer trocar? ")

if letra_analisada in lista:

    letra_tro = input("Por qual letra vai trocar? ")

    for i in range(len(lista)):

        if letra_analisada == lista[i]:

            lista[i] = letra_tro

print(lista)