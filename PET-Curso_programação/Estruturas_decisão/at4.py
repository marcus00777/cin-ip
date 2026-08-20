"""Escreva um programa para ler um ÚNICO caractere e depois informar se este é uma vogal, 
um número ou uma operação matemática (+, -, * ou /)."""


caractere = input("Digite um caractere: ")

if caractere in "a,e,i,o,u":
    print(f"{caractere} é vogal")

elif caractere in "+,-,*,/,":
    print(f"{caractere} é uma operação matemática")

elif caractere in "0,1,2,3,4,5,6,7,8,9":
    print(f"{caractere} é um número")

else:
    print("O caractere não é uma vogal, um número ou uma operação matemática.")
