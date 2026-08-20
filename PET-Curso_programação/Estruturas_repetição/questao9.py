"""Faça um programa para ler os salários dos funcionários e das funcionárias de uma loja
e depois informar a quantidade de funcionários e funcionárias, o total pago de salários
para funcionários e funcionárias e as médias salariais dos funcionários e das funcionárias.
Atenção: considere que o usuário apenas informará gêneros e salários válidos e após a leitura
de cada salário, o programa deve perguntar se
outro salário deve ser lido."""


soma_H = 0
soma_M = 0
quant_h = 0
quant_m = 0

flag = ""

while flag != "N" and flag != "n":

    genero = input("Qual seu gênero F/M: ")

    if genero == "M":
        salario_h = float(input("Digite seu salário: "))
        soma_H += salario_h
        quant_h += 1

    elif genero == "F":
        salario_f = float(input("Digite seu salário: "))
        soma_M += salario_f
        quant_m += 1

    continuar = input("Deseja continuar S/N: ")
    print()
    if continuar == "N":
        flag = "N"

    elif continuar == "n":
        flag = "n"

if quant_h > 0:
    media_h = soma_H / quant_h
else:
    media_h = 0

if quant_m > 0:
    media_m = soma_M / quant_m
else:
    media_m = 0

print("--------------------------------------------------")
print(f"Total pago para os funcionários: R$ {soma_H:.2f}")
print(f"Total pago para os funcionárias: R$ {soma_M:.2f}")
print(f"Média salarial dos funcionários: R$ {media_h:.2f}")
print(f"Média salarial dos funcionárias: R$ {media_m:.2f}")