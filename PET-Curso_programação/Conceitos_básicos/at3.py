"""Faça um programa que, solicite a altura e o raio de um cilindro, calcule o volume 
total do cilindro (use π=3.14) e exiba esse valor."""


altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio da base do cilindro: "))

volume = (3.14 * raio**2) * altura
print(f"O volume do cilindro é: {volume:.1f}")