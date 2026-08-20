#Faça um programa para ler o primeiro e último número de uma sequência
#  e depois exibir: a somatória desses números,
#  a somatória dos números pares e a somatória dos números ímpares.

primeiro = int(input("Digite o primeiro numero: "))
ultimo = int(input("Digite o ultimo numero: "))

somatorio = 0
pares = 0
impares = 0

for i in range(primeiro, ultimo + 1):

    somatorio += i

    if i % 2 == 0:
        pares += i

    else:
        impares += i

print(f"Quantidade de numeros informados: {somatorio}")
print(f"Quantidade de numeros pares: {pares}")
print(f"Quantidade de numeros impares: {impares}")
