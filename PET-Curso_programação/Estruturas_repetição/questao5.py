#Faça um programa para ler o primeiro e último número de uma
#  sequência e depois exibir: a quantidade de números dessa sequencia,
#  quantos são pares e quantos são ímpares.

primeiro = int(input("Digite o primeiro numero: "))
ultimo = int(input("Digite o ultimo numero: "))

quantidade = 0
pares = 0
impares = 0

for i in range(primeiro, ultimo + 1):

    if i % 2 == 0:
        pares += 1

    else:
        impares += 1

quantidade = pares + impares
print(f"Quantidade de numeros informados: {quantidade}")
print(f"Quantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")
