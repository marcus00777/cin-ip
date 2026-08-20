"""Escreva um programa para ler o tamanho de três segmentos de retas e informar se 
estas podem formar um triângulo (a soma de dois lados sempre deve ser menor que o 
terceiro lado). Caso sim, também deve-se informar se este é equilátero (tem os três 
lados iguais), escaleno (tem os três lados diferentes) ou isósceles 
(tem apenas dois lados iguais)."""

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 + n2 > n3 and n1 + n3 > n2 and n3 + n2 > n1:
    print("Esses segmentos podem formar um triângulo")

    if n1 == n2 and n1 == n3 and n2 == n3:
        print("Lados iguais equilátero")

    elif n1 != n2 and n1 != n3 and n3 != n2:
        print("Lados diferente escaleno")

    else:
        print("Dois lados iguais isósceles")

else:
    print("Os segmentos não formam um triângulo")