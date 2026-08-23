"""Faça um programa que leia uma lista de 10 letras e exiba a letra que foi menos 
repetida e a letra  que foi mais repetida."""

lista = []

for i in range(10):

    letras = input(f"Digite a {i+1}° letra: ") 
    lista.append(letras)

print(lista)


maior = 0
menor = 99

for i in range(10):

    vezes = lista.count(lista[i])

    if vezes > maior:
        maior = vezes
        a = lista[i]

    if vezes < menor:
        menor = vezes
        b = lista[i]

print(f"A letra {a} foi a que mais se repetiu: {maior} vezes")
print(f"A letra {b} foi a que menos se repetiu: {menor} vezes")