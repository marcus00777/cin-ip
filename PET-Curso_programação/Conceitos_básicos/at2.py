"""Escreva um programa que, dado um dos lados de um 
quadrado, exiba a sua área e o seu perímetro."""

lado_quadrado = float(input("Digite o lada do quadrado: "))
area = lado_quadrado * lado_quadrado
perimetro = lado_quadrado * 4

print(f"Área do quadrado: {area:.1f}")
print(f"Perímetro do quadrado: {perimetro:.1f}")