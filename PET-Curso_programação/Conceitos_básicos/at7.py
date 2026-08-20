"""Escreva um programa que, leia um valor de custo e o percentual de lucro desejado, 
e na sequencia mostre o valor final do produto;"""

custo = float(input("Digite o custo: "))
percentual = float(input("Digite o percentual de lucro desejado: "))

preco = (custo * (percentual/100)) + custo

print(f"Valor do produto: R$ {preco:.2f}")