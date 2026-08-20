"""Faça um programa que leia a quantidade de departamentos de uma empresa e,
para cada  departamento, leia o seu nome, a quantidade de funcionários e o
salário de cada um destes. Depois disso, para cada departamento, informe 
a sua média salarial.  Atenção: considere que o usuário apenas
informará salários válidos."""

departamentos = int(input("Quantos departamentos possui na sua empresa: "))
soma_salrio = 0

for i in range(departamentos):

    nome_dep = input("Digite o nome do departamento? ")
    quant_fun = int(input(f"Quantos funcionário no departamento {nome_dep}? "))

    for j in range(quant_fun):

        salario_fun = float(input(f"Digite salário do {j+1}° funcionário: "))
        soma_salrio += salario_fun

    media = soma_salrio / quant_fun

    print()
    print(f"O departamento {nome_dep} possui {quant_fun} funcionários")
    print(f"Média salarial dos funcionários do departamento {nome_dep}: R$ {media:.2f}")
    print()