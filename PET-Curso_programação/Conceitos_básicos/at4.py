"""Escreva um programa que receba o nome de uma pessoa e sua idade em anos. 
O programa deve calcular e exibir a idade da pessoa em meses e dias, 
considerando que um ano tem 12 meses e um mês tem 30 dias."""


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

conversao_mes = 12 * idade
conversao_dia = 365 * idade

print(f"{nome} tem {idade} anos ou {conversao_mes} meses ou {conversao_dia} dias!")