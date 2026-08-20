"""Escreva um programa que leia as 2 notas de um aluno
 em uma disciplina, depois exiba quantos pontos o aluno ficou distante da nota 10 
 para cada avaliação, sua média e quantos pontos a média do aluno ficou distante da 
 nota 10."""


nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

print(f"Na primeira avaliação para o 10 faltou: {10 - nota1:.1f}")
print(f"Na segunda avaliação para o 10 faltou: {10 - nota2:.1f}")
print()
media = (nota1+nota2)/2
print(f"Sua média foi de: {media:.1f}")
print()
print(f"Para a média 10 faltou: {10 - media:.1f}")