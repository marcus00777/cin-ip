print("Avenida Brasil: A Vingança de Nina!")

tentativa = 0

total_pendrive = 0
quantidade_pendrive = int(input())
total_pendrive += quantidade_pendrive
pendrive_aberto = 0

for x in range(1, quantidade_pendrive + 1):
    print(f"Descriptografando pendrive {x} de {total_pendrive}...")
    senha = input()

    letras_usa = ""
    palavra = ""

# Removendo espaços
    senha_s = ""
    for c in senha:
         if c != " ":
             senha_s += c
    tentativa = 2 * len (senha_s)

    for b in senha: 
        if b == " ":
            palavra += " "

        else:
            palavra += "_"

#Pedindo letra 
    for e in range(tentativa):
      if "_" in palavra:  
        letra = input()

        if letra in letras_usa:
            print("Max: Ele já tentou isso, Carminha...")
            tentativa -= 1

        elif letra in senha:
            print("Nina: Boa, Tufão! Menos uma mentira da Carminha.")
        
            nova_letra = ""
            for s, p in zip(senha,palavra):
                if s == letra:
                    nova_letra += letra
                else:
                    nova_letra += p

            palavra = nova_letra
            letras_usa += letra

        else:
            print("Carminha: Você é um idiota, Tufão! Isso não faz sentido.")
            tentativa -= 1
            letras_usa += letra
        
        print(f"Senha: {palavra}")       
    
    if "_" not in palavra:  
        pendrive_aberto += 1
        print(f"Tufão: Agora eu sei de toda a verdade! O pendrive {x} está aberto.")
        
    else:
        print(f"Carminha: Consegui! As fotos do pendrive {x} estão a salvo comigo.")

print(f"Conseguimos abrir {pendrive_aberto} de {total_pendrive} pendrives!") 

# Taxa
taxa = 0    

if quantidade_pendrive != 0:
    taxa = (pendrive_aberto / quantidade_pendrive) * 100

    if taxa == 0:
        print("Tufão continuará sendo enganado para sempre...")

    elif 0 < taxa <= 50:
        print("Tufão descobriu algumas coisas, mas Carminha ainda tem poder.")

    elif 50 < taxa < 100:
        print("A casa caiu para a Carminha! Quase todas as provas foram recuperadas.")

    elif taxa == 100:
        print("Justiça por Rita! Todas as provas estão nas mãos de Tufão.") 

else:
    taxa == 0 
    print("Tufão continuará sendo enganado para sempre...")

