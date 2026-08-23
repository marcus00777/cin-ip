"""Faça um programa que leia uma lista de 10 números inteiros e exiba
os pares e só depois os ímpares."""

lista = []
lista_pares = []
lista_impares = []

for i in range(10):

    num = int(input(f"Digite o {i+1}° número da lista: "))
    lista.append(num)

for i in range(10):

    if lista[i] % 2 == 0:

        lista_pares.append(lista[i])

    else:
        lista_impares.append(lista[i])

print(f"Pares: {lista_pares}")
print(f"Impares: {lista_impares}")
