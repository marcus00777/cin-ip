"""Escreva um programa que receba a idade de uma pessoa em dias. 
Em seguida, converta essa idade para anos, meses e dias, e exiba o resultado. 
Para fazer essa conversão, assuma que um ano tem 365 dias e um mês tem 30 dias."""

idade = int(input("Digite sua idade em dia: "))

idade_anos = idade // 365
dias = idade % 365
idade_mes = dias // 30
idade_dia = dias % 30 
print(f"Idade: {idade_anos} anos, {idade_mes} meses e {idade_dia} dias")