"""Escreva um programa que leia o salário de uma pessoa, 
quantas horas ela trabalha por dia e quantos dias ela trabalhou no mês. Em seguida, 
calcule e exiba quanto essa pessoa recebe por hora."""

salario = float(input("Qual seu salário: "))
hora_dias = float(input("Quantas hora trabalha por dia: "))
dias_mes = int(input("Quantos dias trabalhou no mês: "))

salario_hora = salario / (hora_dias*dias_mes)

print(f"Ganhos por hora trabalhada: R$ {salario_hora:.2f}")