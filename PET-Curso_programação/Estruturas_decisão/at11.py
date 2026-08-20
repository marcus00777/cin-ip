""" Faça um programa para ler dois números inteiros e positivos (n1 e n2) e 
depois exibir se o primeiro é divisível pelo segundo e se ambos são pares. 
Por exemplo, 
4 é divisível por 2 e ambos são pares. """

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 % n2 == 0:
    print(f"{n1} é divisível por {n2}")

else:
    print("Não é divisível")

if n1 % 2 == 0 and n2 % 2 == 0:
    print("Ambos são pares")

else:
    print("Algum ou ambos são ímpares")