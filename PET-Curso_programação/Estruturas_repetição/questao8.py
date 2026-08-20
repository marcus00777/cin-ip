"""Faça um programa para ler os salários dos 10 funcionários de uma
loja e depois informar o valor gasto para pagar a folha de todos os funcionários e qual é
a média salarial geral. Atenção: considere
que o usuário apenas informará salários válidos."""

soma = 0
for i in range(10):

    salario_fun = float(input("Digite o valor do seu salário: "))
    soma += salario_fun

media = soma / 10

print()
print(f"O valor gasto para pagar os funcionários será de: R$ {soma:.2f}")
print(f"A média salrial foi de: R$ {media:.2f}")