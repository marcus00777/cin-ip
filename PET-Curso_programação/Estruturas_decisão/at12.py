""" Faça um programa para ler três números inteiros e positivos (n1, n2, n3) e 
depois exibir todos que são pares e 
todos que são ímpares, nesta ordem """

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))

if n1 % 2 == 0:
    print(f"{n1} é par")

else:
    print(f"{n1} é ímpar")

if n2 % 2 == 0:
    print(f"{n2} é par")

else:
    print(f"{n2} é ímpar")

if n3 % 2 == 0:
    print(f"{n3} é par")

else:
    print(f"{n3} é ímpar")