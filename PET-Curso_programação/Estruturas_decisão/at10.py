""" Escreva um programa para ler a descrição, 
o tipo e o valor de um produto e depois exibir o valor do reajuste e o valor 
reajustado, considerando os seguintes percentuais: 
1) produtos dos tipos “A” ou “B“ têm reajuste de 12,3%; 
2) produtos do tipo “C” têm reajuste de 14% e produtos dos tipos “D” ou “E” 
têm reajustes de 15,7%. Atenção, faça uma validação para informar um 
erro caso o tipo informado pelo usuário não seja um dos tipos acima."""

descricao = input("Descrição do produto: ")
tipo = input("Qual o tipo do produto: ")
valor_produto = float(input("Digite o valor do produto: "))


if tipo == "A" or tipo == "B":
    valor = valor_produto + (valor_produto * 12.3/100)
    

elif tipo == "C":
    valor = valor_produto + (valor_produto * 14/100)

elif tipo == "D" or tipo == "E":
    valor = valor_produto + (valor_produto * 15.7/100)

else:
    print("Escolha um tipo válido!")


print("Descrição do Produto:", descricao)
print("Valor do Produto: R$", valor_produto)
print(f"Valor do reajuste: R$ {valor - valor_produto:.2f}\nValor reajustado: R$ {valor:.2f}")





