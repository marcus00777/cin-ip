"""Faça um programa para ler três números inteiros e positivos (n1, n2 e n3) 
e depois exibir estes números em ordem crescente. 
Considere que podem existir números iguais."""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 < n2:
    n1, n2 = n2, n1

if n2 < n3:
    n2, n3 = n3, n2

if n3 < n1:
    n3, n1 = n1, n3

if n1 < n2:
    n1, n2 = n2, n1

if n2 < n3:
    n2, n3 = n3, n2

print(n1, n2, n3)


