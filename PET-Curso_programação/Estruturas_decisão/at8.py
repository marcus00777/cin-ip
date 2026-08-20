"""  Faça um programa que leia o valor da diária de um funcionário, 
a quantidade de dias que este trabalhou no mês e exiba o salário bruto, 
o Imposto de Renda (IR) a ser pago e o salário líquido. 
O cálculo do IR deve considerar os seguintes percentuais: 
1) Salário até R$2.000,00 é isento de IR; 2) Salário entre R$2.000,00 e R$5.000,00 
deve pagar 15% de IR e salário superior a R$5.000,00 deve pagar 27,5% de IR."""

valor_diaria = float(input("Digite quanto recebe por dia: "))
dias_trabalhados = int(input("Digite quantos dias trabalhou: "))
salario_bruto = dias_trabalhados * valor_diaria

if salario_bruto > 2000 and salario_bruto <= 5000:
    imposto = salario_bruto * 15/100
    salario_liquido = salario_bruto - imposto
    print(f"Salário Bruto: R$ {salario_bruto:.2f}\nImposto de Renda: R$ {imposto:.2f}\nSalário Líquido: R$ {salario_liquido:.2f}")

elif salario_bruto > 5000 :
    imposto = salario_bruto * 27.5/100
    salario_liquido = salario_bruto - imposto
    print(f"Salário Bruto: R$ {salario_bruto:.2f}\nImposto de Renda: R$ {imposto:.2f}\nSalário Líquido: R$ {salario_liquido:.2f}")

else:
    print(f"Salário Bruto: R$ {salario_bruto:.2f}\nImposto de Renda: Isento\nSalário Líquido: R$ {salario_bruto:.2f}")
    