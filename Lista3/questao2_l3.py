pedido = input()
itens = pedido.split(", ")
print("Pedido recebido! Vamos alocar os itens nos caminhões disponíveis.")

lista = ''
f = True 
itens_recebidos = []

while f:
    lista = input()

    if lista == "--":
        f = False

    else:
        itens2 = lista.split(", ")

        iguais =[]
        faltante = []

#analisar itens de acordo com o caminhão
        for c in itens2 :
            if c in itens:
                iguais.append(c)
                if c in itens and itens_recebidos.count(c) < itens.count(c):
                    itens_recebidos.append(c)
    
#analisar o que falta de acordo com o pedido
        for i in itens:
            if i not in faltante:     
                falta = itens.count(i) -  itens_recebidos.count(i)
                for x in range(falta):
                    faltante.append(i)

        if len(iguais) > 0:
            print(f"Ótimo, esse caminhão trouxe {iguais}!")

        if len(iguais) == 0:
            print("Não encontramos nada que a Carol pediu nesse caminhão.")

        if len(faltante) > 0:
            print(f"Ainda precisamos de {faltante}.")

#verificar se todos os pedidos foram entregue
todos_itens = True

for c in itens:
    if itens_recebidos.count(c) < itens.count(c):
        todos_itens = False

if todos_itens:
    print("Conseguimos! A Carol ficará muito feliz :)")
else:
    print("Não conseguimos reunir todos os itens que a Carol precisa :(")
    
