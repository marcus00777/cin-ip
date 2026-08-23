"""Faça um programa que leia uma lista de 10 letras e exiba-as sem repetição."""

lista = []

anterior = ""
for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ")

    if letras != anterior:
        lista.append(letras)

    anterior = letras


print(lista)