""" Considerando que um mês tem 26 dias úteis. 
Faça um programa que leia o valor da diária de um funcionário, 
a quantidade de dias que este faltou no mês e exiba o valor o 
valor do salário com desconto, o valor do salário integral, 
o valor do desconto e o percentual desse desconto com relação ao salário integral.
Atenção, caso o funcionário não tenha faltado no mês, substitua a exibição anterior
por uma mensagem informando o salário integral, o valor de um bônus correspondente a 
12,3% sobre o salário integral e o salário bonificado."""

valor_diaria = float(input("Digite sua diária: "))
dia_faltados = int(input("Digite quantos dias você faltou no mês: "))

if dia_faltados > 0:
    salario_integral = valor_diaria * 26
    salario_recebido = valor_diaria * (26-dia_faltados)
    desconto = salario_integral - salario_recebido

    percentual_desconto = (salario_recebido / salario_integral) * 100

    print(f"Salário com desconto: R$ {salario_recebido:.2f}\nSalário Integral: R$ {salario_integral:.2f}\nDesconto: R$ {desconto:.2f}\nPercentual de desconto: {percentual_desconto:.1f}%")

else:
    salario_integral = valor_diaria * 26
    bonus = salario_integral * 12.3/100
    salario_bonificado = salario_integral + bonus
    print(f"Salário Integral: R$ {salario_integral:.2f}\nBônus: R$ {bonus:.2f}\nSalário Bonificado: R$ {salario_bonificado:.2f}")