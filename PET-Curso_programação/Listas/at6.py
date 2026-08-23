"""Faça um programa que leia uma lista de 10 letras, procure por uma letra específica e 
exiba o primeiro índice que esta letra aparece."""

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ") 
    lista.append(letras)

print(lista)

letra_analisada = input("Qual letra você que analisar o índice: ")

if letra_analisada in lista:

    a = lista.index(letra_analisada)

    print(f"A letra {letra_analisada} está no índice {a} da lista")