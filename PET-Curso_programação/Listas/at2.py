"""Faça um programa que leia uma lista de 10 letras 
e exiba-as em ordem alfabética decrescente."""

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ")
    lista.append(letras)

lista.sort()
lista.reverse()
print(lista)