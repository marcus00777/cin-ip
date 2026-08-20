"""Escreva um programa que permute(troque) o valor de duas variáveis inteiras. 
DICA: use uma terceira variável para armazenar 
temporariamente o valor a ser trocado."""

a = int(input("Digite um número: "))
b = int(input("Digite outro número: "))

aux = a
a = b
b = aux
print(f"Valor de a após a permutação: {a}")
print(f"Valor de b após a permutação: {b}")