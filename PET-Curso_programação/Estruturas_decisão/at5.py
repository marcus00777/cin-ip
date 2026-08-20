"""Faça um programa para ler dois número (n1 e n2) e uma operação da matemática 
(+, -, * ou /)
 e exiba o resultado dessa operação entre esses dois números."""


n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operacao = input("Digite uma operação matemática: ")

if operacao == "+":
    print(f"{n1} {operacao} {n2} = {n1+n2:.1f}")

elif operacao == "-":
    print(f"{n1} {operacao} {n2} = {n1-n2:.1f}")

elif operacao == "*":
    print(f"{n1} {operacao} {n2} = {n1*n2:.1f}")

elif operacao == "/":
    if n2 != 0:
        print(f"{n1} {operacao} {n2} = {n1/n2:.1f}")

    else:
        print("Operação não existe")