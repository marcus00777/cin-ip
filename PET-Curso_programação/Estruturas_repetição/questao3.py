#Faça um programa para ler números inteiros e positivos até o usuário não 
# desejar continuar informando um novo número.
#  Ao final, o programa deve exibir o total de números lidos.

continuar = ""
quantidade_informada = 0

while continuar != "N" and continuar != "n":

    num = int(input("Digite um numero: "))
    quantidade_informada += 1

    continuar = input("Quer continuar S/N: ")

print(f"Quantidade de numeros informados: {quantidade_informada}")