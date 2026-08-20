""" Faça um programa para ler a média salarial dos funcionários e, na sequência, 
o nome e o salário de um dos funcionários dessa empresa. Ao terminar a leitura, 
exibir o nome do funcionário e se o seu salário é maior, 
menor ou igual a média salarial."""

media_salarial = float(input("Digite a média salarial dos funcionários: "))
nome_funcionario = input("Digite o nome do funcionário: ")
salario_funcionario = float(input("Digite o salário do funcionário: "))

if salario_funcionario > media_salarial:
    print(f"O funcionário {nome_funcionario} possui um salário de R$ {salario_funcionario:.2f} maior que a média salarial R$ {media_salarial:.2f}")

elif salario_funcionario == media_salarial:
    print(f"O funcionário {nome_funcionario} possui um salário de R$ {salario_funcionario:.2f} igual que a média salarial R$ {media_salarial:.2f}")

else:
    print(f"O funcionário {nome_funcionario} possui um salário de R$ {salario_funcionario:.2f} menor que a média salarial R$ {media_salarial:.2f}")
    
        
