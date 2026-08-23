"""Faça um programa que leia uma lista de 10 letras únicas (sem repetição) 
e as exiba em ordem alfabética crescente."""

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ")

    if letras in lista:
        print("Já possui essa letra na lista")

    else:
        lista.append(letras)

lista.sort()
print(lista)