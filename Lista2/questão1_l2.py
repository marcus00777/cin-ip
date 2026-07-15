quant = 0 
musica = input("")
b = "Voa, Voa Brabuleta"
lista = "Setlist de músicas: "

while musica.lower() != b.lower():   
   
    quant += 1
    if quant == 1:
        lista = lista + musica 
    elif quant > 1:
        lista = lista + " - " + musica 
    musica = input("")
    
    

print('Bom dia, dona Maria! Aqui vão as músicas mais pedidas de hoje!')
print(f"A quantidade de músicas selecionadas foi {quant}")
print(lista)

