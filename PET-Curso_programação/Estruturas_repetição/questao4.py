#Faça um programa para ler 10 números inteiros e positivos
#  e depois exibir a somatória dos números lidos.

soma = 0

for i in range(10):

    num = int(input("Digite um numero: "))
    soma += num

print(f"A soma dos numeros informados é: {soma}")