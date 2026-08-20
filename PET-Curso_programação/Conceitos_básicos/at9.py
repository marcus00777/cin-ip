"""Considerando que o valor do m² para concretar um piso é R$50. 
Escreva um programa que leia as medidas de um terreno retangular e 
informe quanto custa para concretá-lo por inteiro. """

lado1 = float(input("Digite o comprimento do terreno: "))
lado2 = float(input("Digite a largura do terreno: "))

area = lado1 * lado2
preco = area * 50

print(f"Para concretar seu terreno o custo será de: R$ {preco:.2f}")