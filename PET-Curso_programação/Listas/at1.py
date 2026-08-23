"""Faça um programa que leia uma lista de 10 letras e 
exiba-as na ordem inversa à ordem de leitura."""

"""
#Utilizando a função reverse()

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ")
    lista.append(letras)

lista_original = lista.copy()
lista.reverse()
print(f"Lista original: {lista_original}")
print(f"Lista reversa: {lista}")

"""

#Outra maneira de ser feita
lista = []
lista_aux = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ")
    lista.append(letras)

lista_original = lista.copy()

for i in range(len(lista)):

    lista_aux.append(lista[-1])
    lista.remove(lista[-1])

print(f"Lista original: {lista_original}")
print(f"Lista reversa: {lista_aux}")