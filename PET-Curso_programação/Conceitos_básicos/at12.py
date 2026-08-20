"""Considerando que em um show: 1) 45% dos ingressos vendidos foram meia-entrada; 
2) 55% dos ingressos vendidos foram inteiros; 
3)O valor do ingresso inteiro custava R$123,45 e 
4) o total de ingressos vendidos foi 6.789. Escreva um programa que calcule e exiba:
    1. A quantidade de ingressos meia-entrada e inteira vendidos.
    2. O valor faturado com cada tipo de ingresso.
    3. O valor total faturado."""


meia_entrada = (6789 * 45/100)
inteira = (6789 * 55/100)

valor_meia = 123.45/2 * meia_entrada
valor_inteira = 123.45 * inteira
valor_total = valor_inteira + valor_meia

print(f"Ingressos meia-entrada e inteira: {int(meia_entrada)} e {int(inteira)}")
print(f"Valor faturado na meia-entrada e inteira: R$ {valor_meia:.2f} e R$ {valor_inteira:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")