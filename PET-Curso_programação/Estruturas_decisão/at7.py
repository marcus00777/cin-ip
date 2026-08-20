""" Faça um programa que leia o nome, o sobrenome e a idade de um atleta e
exiba seu nome completo e se ele está na categoria infantil (menor de 12 anos), 
juvenil (entre 12 e 17 anos), 
adulto (entre 18 e 35 anos) ou master (acima de 35 anos)."""

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
idade = int(input("Digite sua idade: "))

if idade < 12:
    categoria = "infantil"

elif idade >= 12 and idade <= 17:
    categoria = "juvenil"

elif idade >= 18 and idade <= 35:
    categoria = "adulto"

else:
    categoria = "master"

print(f"{nome} {sobrenome} está na categoria {categoria}")