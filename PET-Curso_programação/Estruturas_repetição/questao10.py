"""Faça um programa para ler os salários dos funcionários e das funcionárias de uma loja. O
programa deve validar os salários para aceitar apenas valores entre 1000 e 10000. Após a
leitura de cada salário, pergunte ao usuário se deseja informar outro salário. No final,
exiba o maior e o
menor salário informados."""


maior = 0
menor = 10000
salario = 1000

flag = ""

eh_valido = True

while flag != "N" and flag != "n":

    genero = input("Qual seu gênero F/M: ")
    salario = float(input("Digite seu salário: "))

    if salario < 1000 or salario > 10000:
        eh_valido = False
        break

    if genero == "M":
        salario_h = salario

        if salario_h > maior:
            maior = salario_h

        if salario_h < menor:
            menor = salario_h

    elif genero == "F":
        salario_m = salario

        if salario_m > maior:
            maior = salario_m
        
        if salario_m < menor:
            menor = salario_m

    continuar = input("Deseja continuar S/N: ")
    print()
    if continuar == "N":
        flag = "N"

    elif continuar == "n":  
        flag = "n"


if eh_valido:
    print(f"O maior salário foi: R$ {maior:.2f}")
    print(f"O menor salário foi: R$ {menor:.2f}")