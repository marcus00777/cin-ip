dinheiro_in = int(input())
compra = ""
custo = 0
modelo = ""
quantidade = 0
custo_total = 0

print(f"A família possui {dinheiro_in} ainda, talvez ele fique tranquilo hoje")

while dinheiro_in > 0:
    compra = str(input())

    if compra == 'Amauri':
            print("Sabia que vocês estão loucos, hora de encerrar essa loucura!")
            dinheiro_in -= dinheiro_in

    else: 
        custo = int(input())
        if compra == "carro":
            modelo = str(input())

        falido = custo > dinheiro_in
        
        if not falido :
            custo_total += custo
            dinheiro_in -= custo 
            quantidade += 1
            
            if custo > 500000:
                print(f"Enlouqueceram de vez {custo} reais num(a) {compra}")

            elif custo < 1000:
                print(f'Será que se acalmaram?! {compra} por "somente" {custo} reais')

            else:
                print(f"Gastaram {custo} reais para comprar um(a) {compra}")

            if compra == "carro":
                if modelo == "chevette":
                    print('chevette : Relembrando as origens será?')

                if modelo == "jeep":
                    print('jeep : Será que ele tá se preparando para outra aventura que não irá?')

                if modelo == "bmw":
                    print('bmw : Já to vendo o facebook dele cheio de foto me marcando 🙁')

            if dinheiro_in == 0:
              print("Enlouqueceram? Vocês estão falidos")


        if falido :
           print("Enlouqueceram? Vocês estão falidos")
           dinheiro_in = 0
  
   

print (f"{quantidade} - {custo_total} reais")


