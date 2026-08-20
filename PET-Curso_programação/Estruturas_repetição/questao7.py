"""Escreva um programa para você informar um número
inteiro e positivo entre 1 e 100, e peça para
um amigo informar o seu cubo. A cada tentativa deve-se
informar se o número informado pelo amigo é maior ou menor do que o cubo do número que você 
informou. Quando o seu amigo acertar, além da mensagem de parabéns, deve-se informar: quantos 
números ele digitou, quantos desses números eram
maiores e quantos eram menores do que o cubo do número que você informou. """

numero = 0
flag = True
quantidade_nu = 0
maiores = 0
menores = 0
p = ""

while numero <= 0 or numero > 100:
    numero = int(input("Digite um numero entre 0 e 100: "))

while flag:

    num_amigo = int(input("Digite um número: "))
    quantidade_nu += 1

    if num_amigo > numero ** 3:
        print(f"O número informado é maior que o cubo do {numero}")
        maiores += 1

    elif num_amigo < numero ** 3:
        print(f"O número informado é menor que o cubo do {numero}")
        menores += 1

    elif num_amigo == numero ** 3:
        p = "Parabéns"
        flag = False

print()
print(p)
print()
print(f"Você digitou {quantidade_nu} números!")
print(f"Quantidade de números maiores {maiores}")
print(f"Quantidade de números menores {menores}")

    