"""Faça um programa para ler quatro números inteiros (n1, n2, n3 e n4) e 
depois exibir todos que são pares e positivos, pares e negativos, ímpares e positivos, 
ímpares e negativo e zero, 
nesta ordem """

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite outro número: "))
n4 = int(input("Digite outro número: "))

print("Pares positivos:")
if n1 > 0 and n1 % 2 == 0:
    print(n1)

if n2 > 0 and n2 % 2 == 0:
    print(n2)

if n3 > 0 and n3 % 2 == 0:
    print(n3)

if n4 > 0 and n4 % 2 == 0:
    print(n4)

print("Pares negativos:")
if n1 < 0 and n1 % 2 == 0:
    print(n1)

if n2 < 0 and n2 % 2 == 0:
    print(n2)

if n3 < 0 and n3 % 2 == 0:
    print(n3)

if n4 < 0 and n4 % 2 == 0:
    print(n4)

print("Ímpares positivos:")
if n1 > 0 and n1 % 2 != 0:
    print(n1)

if n2 > 0 and n2 % 2 != 0:
    print(n2)

if n3 > 0 and n3 % 2 != 0:
    print(n3)

if n4 > 0 and n4 % 2 != 0:
    print(n4)

print("Ímpares negativos:")
if n1 < 0 and n1 % 2 != 0:
    print(n1)

if n2 < 0 and n2 % 2 != 0:
    print(n2)

if n3 < 0 and n3 % 2 != 0:
    print(n3)

if n4 < 0 and n4 % 2 != 0:
    print(n1)

print("Zero:")
if n1 == 0:
    print(n1)

if n2 == 0:
    print(n2)

if n3 == 0:
    print(n3)

if n4 == 0:
    print(n4)