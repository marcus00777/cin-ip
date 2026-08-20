"""Escreva um programa que, a partir de um valor de custo e de um valor de venda, 
mostre o valor do lucro obtido com a venda do produto;"""


custo = float(input("Digite o custo: "))
venda = float(input("Digite a venda: "))
lucro = venda - custo

print(f"Lucro: {lucro:.1f}")