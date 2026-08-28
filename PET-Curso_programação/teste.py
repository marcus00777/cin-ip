lista_nomes = []
lista_notas = []

nome_aluno = ""

while nome_aluno != "fim":

  nome_aluno = input()
  lista_nomes.append(nome_aluno)

  if nome_aluno != "fim":
    nota_aluno = float(input())
    lista_notas.append(nota_aluno)

for i in range(len(lista_nomes) - 1):

  for j in range(len(lista_nomes) - 1):

    if lista_notas[j] < lista_notas[j+1]:
      lista_notas[j], lista_notas[j+1] = lista_notas[j+1], lista_notas[j]

      lista_nomes[j], lista_nomes[j+1] = lista_nomes[j+1], lista_nomes[j]

print(lista_notas) 
print(lista_nomes)
    
