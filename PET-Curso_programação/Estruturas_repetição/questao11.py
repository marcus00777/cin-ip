"""Faça um programa para exibir a tabuada de multiplicação (operação = M)
ou adição (operação = A). Atenção: só permita exibir a
tabuada quando for informado “M” ou “A”."""


escolha = input("Escolha 'M' para opção de Multiplicação ou 'A' para Adição: ")

if escolha == "M":

   for i in range(1, 11):

      print(f"Tabuada do número {i}")
      for j in range(1, 11):

         resposta = i * j
         print(f"{i} x {j} = {resposta}")

elif escolha == "A":

   for i in range(1, 11):

      print(f"Tabuada do número {i}")
      for j in range(1, 11):

         resposta = i + j
         print(f"{i} + {j} = {resposta}")

else:
   print("Operação inválida")