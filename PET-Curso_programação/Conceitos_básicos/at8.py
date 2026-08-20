"""Escreva um programa que, leia um valor de venda e um percentual de desconto, 
e depois apresente o valor a ser pago 
pelo produto e o valor do desconto que foi concedido;"""


venda = float(input("Digite o valor da venda: "))
desconto = float(input("Percentual de desconto: "))

valor_pagar = venda - (venda * (desconto/100))

print(f"Valor à pagar pelo produto: R$ {valor_pagar:.2f}, desconto de {desconto:.1f}%")