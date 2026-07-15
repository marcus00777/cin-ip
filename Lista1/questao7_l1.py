# Máquina 1
nome_in1 = input()
tamanho_nome_inv1 = len(nome_in1)
quantid_pecas1 = int(input())
pontuacao_in1 = tamanho_nome_inv1 + quantid_pecas1
reacao1 = input()

# Máquina 2
nome_in2 = input()
tamanho_nome_inv2 = len(nome_in2)
quantid_pecas2 = int(input())
pontuacao_in2 = tamanho_nome_inv2 + quantid_pecas2
reacao2 = input()

# Máquina 3
nome_in3 = input()
tamanho_nome_inv3 = len(nome_in3)
quantid_pecas3 = int(input())
pontuacao_in3 = tamanho_nome_inv3 + quantid_pecas3
reacao3 = input()

# Máquina 4
nome_in4 = input()
tamanho_nome_inv4 = len(nome_in4)
quantid_pecas4 = int(input())
pontuacao_in4 = tamanho_nome_inv4 + quantid_pecas4
reacao4 = input()

frase1 = "MÃE! O PHINEAS E O FERB ESTÃO CONSTRUINDO UMA MÁQUINA GIGANTE!"
frase2 = "EU SABIA QUE ELES ESTAVAM APRONTANDO ALGUMA COISA!"
frase3 = "OK... ISSO É BEM ESTRANHO."
frase4 = "AH, NEM É TÃO IMPRESSIONANTE ASSIM."
frase5 = "SÉRIO? SÓ ISSO?"
frase6 = "MÃE! A MÁQUINA SUMIU DE NOVO!"
frase7 = "AH, ESQUECE…"

ina1 = 'i' in nome_in1.lower() and 'n' in nome_in1.lower() and 'a' in nome_in1.lower() and 't' in nome_in1.lower() and 'o' in nome_in1.lower() and 'r' in nome_in1.lower()

pe1 = 'p' in nome_in1.lower() and 'e' in nome_in1.lower() and 'r' in nome_in1.lower() and 'y' in nome_in1.lower()

ina2 = 'i' in nome_in2.lower() and 'n' in nome_in2.lower() and 'a' in nome_in2.lower() and 't' in nome_in2.lower() and 'o' in nome_in2.lower() and 'r' in nome_in2.lower()

pe2 = 'p' in nome_in2.lower() and 'e' in nome_in2.lower() and 'r' in nome_in2.lower() and 'y' in nome_in2.lower()

ina3 = 'i' in nome_in3.lower() and 'n' in nome_in3.lower() and 'a' in nome_in3.lower() and 't' in nome_in3.lower() and 'o' in nome_in3.lower() and 'r' in nome_in3.lower()

pe3 = 'p' in nome_in3.lower() and 'e' in nome_in3.lower() and 'r' in nome_in3.lower() and 'y' in nome_in3.lower()

ina4 = 'i' in nome_in4.lower() and 'n' in nome_in4.lower() and 'a' in nome_in4.lower() and 't' in nome_in4.lower() and 'o' in nome_in4.lower() and 'r' in nome_in4.lower()

pe4 = 'p' in nome_in4.lower() and 'e' in nome_in4.lower() and 'r' in nome_in4.lower() and 'y' in nome_in4.lower()

if ina1:
    pontuacao_in1 = pontuacao_in1 - 50
if pe1:
    pontuacao_in1 = pontuacao_in1 + 20
if reacao1 == frase1:
    pontuacao_in1 = pontuacao_in1 + 30
elif reacao1 == frase2:
    pontuacao_in1 = pontuacao_in1 + 20
elif reacao1 == frase3:
    pontuacao_in1 = pontuacao_in1 + 10 
elif reacao1 == frase4:
    pontuacao_in1 = pontuacao_in1 + 0
elif reacao1 == frase5:
    pontuacao_in1 = pontuacao_in1 - 5
elif reacao1 == frase6:
    pontuacao_in1 = pontuacao_in1 - 10
elif reacao1 == frase7:
    pontuacao_in1 = pontuacao_in1 - 15

if nome_in1 == "HidromassagemAutomáticaDoPerry":
    pontuacao_in1 = pontuacao_in1 * 2

if nome_in1 == "MáquinaDeBanhoForçado":
    pontuacao_in1 = pontuacao_in1 - 20

m1 = pontuacao_in1

# Máquina 2
if ina2:
    pontuacao_in2 = pontuacao_in2 - 50
if pe2:
    pontuacao_in2 = pontuacao_in2 + 20
if reacao2 == frase1:
    pontuacao_in2 = pontuacao_in2 + 30
elif reacao2 == frase2:
    pontuacao_in2 = pontuacao_in2 + 20
elif reacao2 == frase3:
    pontuacao_in2 = pontuacao_in2 + 10
elif reacao2 == frase4:
    pontuacao_in2 = pontuacao_in2 + 0
elif reacao2 == frase5:
    pontuacao_in2 = pontuacao_in2 - 5
elif reacao2 == frase6:
    pontuacao_in2 = pontuacao_in2 - 10
elif reacao2 == frase7:
    pontuacao_in2 = pontuacao_in2 - 15

if nome_in2 == "HidromassagemAutomáticaDoPerry":
    pontuacao_in2 = pontuacao_in2 * 2

if nome_in2 == "MáquinaDeBanhoForçado":
    pontuacao_in2 = pontuacao_in2 - 20

m2 = pontuacao_in2

# Máquina 3
if ina3:
    pontuacao_in3 = pontuacao_in3 - 50
if pe3:
    pontuacao_in3 = pontuacao_in3 + 20
if reacao3 == frase1:
    pontuacao_in3 = pontuacao_in3 + 30
elif reacao3 == frase2:
    pontuacao_in3 = pontuacao_in3 + 20
elif reacao3 == frase3:
    pontuacao_in3 = pontuacao_in3 + 10
elif reacao3 == frase4:
    pontuacao_in3 = pontuacao_in3 + 0
elif reacao3 == frase5:
    pontuacao_in3 = pontuacao_in3 - 5
elif reacao3 == frase6:
    pontuacao_in3 = pontuacao_in3 - 10
elif reacao3 == frase7:
    pontuacao_in3 = pontuacao_in3 - 15

if nome_in3 == "HidromassagemAutomáticaDoPerry":
    pontuacao_in3 = pontuacao_in3 * 2

if nome_in3 == "MáquinaDeBanhoForçado":
    pontuacao_in3 = pontuacao_in3 - 20

m3 = pontuacao_in3

# Máquina 4
if ina4:
    pontuacao_in4 = pontuacao_in4 - 50
if pe4:
    pontuacao_in4 = pontuacao_in4 + 20
if reacao4 == frase1:
    pontuacao_in4 = pontuacao_in4 + 30
elif reacao4 == frase2:
    pontuacao_in4 = pontuacao_in4 + 20
elif reacao4 == frase3:
    pontuacao_in4 = pontuacao_in4 + 10
elif reacao4 == frase4:
    pontuacao_in4 = pontuacao_in4 + 0
elif reacao4 == frase5:
    pontuacao_in4 = pontuacao_in4 - 5
elif reacao4 == frase6:
    pontuacao_in4 = pontuacao_in4 - 10
elif reacao4 == frase7:
    pontuacao_in4 = pontuacao_in4 - 15

if nome_in4 == "HidromassagemAutomáticaDoPerry":
    pontuacao_in4 = pontuacao_in4 * 2

if nome_in4 == "MáquinaDeBanhoForçado":
    pontuacao_in4 = pontuacao_in4 - 20

m4 = pontuacao_in4


if m1 < m2:
    m1,m2 = m2,m1
    nome_in1,nome_in2 = nome_in2,nome_in1
    tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1
    quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1

if m2 < m3:
    m2,m3 = m3,m2
    nome_in2,nome_in3 = nome_in3,nome_in2
    tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2
    quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2

if m3 < m4:
    m3,m4 = m4,m3
    nome_in3,nome_in4= nome_in4,nome_in3
    tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3
    quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3

if m1 < m2:
    m1,m2 = m2,m1
    nome_in1,nome_in2 = nome_in2,nome_in1
    tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1
    quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1

if m2 < m3:
    m2,m3 = m3,m2
    nome_in2,nome_in3 = nome_in3,nome_in2
    tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2
    quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2

if m1 < m2:
    m1,m2 = m2,m1
    nome_in1,nome_in2 = nome_in2,nome_in1
    tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1
    quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1

#Casos de empates
#m1 == m2
if m1 == m2:

    parametro1 = 0
    parametro2 = 0

    if quantid_pecas1 > 25:
        parametro1 = parametro1 + 1

    if tamanho_nome_inv1 > 15:
        parametro1 = parametro1 + 1

    if quantid_pecas2 > 25:
        parametro2 = parametro2 + 1

    if tamanho_nome_inv2 > 15:
        parametro2 = parametro2 + 1

    if parametro1 < parametro2:
        m1,m2 = m2,m1
        nome_in1,nome_in2 = nome_in2,nome_in1
        quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1
        tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1

    elif parametro1 == parametro2:

        if quantid_pecas1 < quantid_pecas2:
            m1,m2 = m2,m1
            nome_in1,nome_in2 = nome_in2,nome_in1
            quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1
            tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1

        else:
            if tamanho_nome_inv1 < tamanho_nome_inv2:
                m1,m2 = m2,m1
                nome_in1,nome_in2 = nome_in2,nome_in1
                quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1
                tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1

    if m2 < m3:
        m2,m3 = m3,m2
        nome_in2,nome_in3 = nome_in3,nome_in2
        quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
        tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

    if m3 < m4:
        m3,m4 = m4,m3
        nome_in3,nome_in4 = nome_in4,nome_in3
        quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3
        tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3

    if m1 < m2:
        m1,m2 = m2,m1
        nome_in1,nome_in2 = nome_in2,nome_in1
        quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1
        tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1

    if m2 < m3:
        m2,m3 = m3,m2
        nome_in2,nome_in3 = nome_in3,nome_in2
        quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
        tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

    if m1 < m2:
        m1,m2 = m2,m1
        nome_in1,nome_in2 = nome_in2,nome_in1
        quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1
        tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1


#m2 == m3
if m2 == m3:

    parametro2 = 0
    parametro3 = 0

    if quantid_pecas2 > 25:
        parametro2 = parametro2 + 1

    if tamanho_nome_inv2 > 15:
        parametro2 = parametro2 + 1

    if quantid_pecas3 > 25:
        parametro3 = parametro3 + 1

    if tamanho_nome_inv3 > 15:
        parametro3 = parametro3 + 1

    if parametro2 < parametro3:
        m2,m3 = m3,m2
        nome_in2,nome_in3 = nome_in3,nome_in2
        quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
        tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

    elif parametro2 == parametro3:

        if quantid_pecas2 < quantid_pecas3:
            m2,m3 = m3,m2
            nome_in2,nome_in3 = nome_in3,nome_in2
            quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
            tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

        else:
            if tamanho_nome_inv2 < tamanho_nome_inv3:
                m2,m3 = m3,m2
                nome_in2,nome_in3 = nome_in3,nome_in2
                quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
                tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

    if m3 < m1:
        m3,m1 = m1,m3
        nome_in3,nome_in1 = nome_in1,nome_in3
        quantid_pecas3,quantid_pecas1 = quantid_pecas1,quantid_pecas3
        tamanho_nome_inv3,tamanho_nome_inv1 = tamanho_nome_inv1,tamanho_nome_inv3

    if m1 < m4:
        m1,m4 = m4,m1
        nome_in1,nome_in4 = nome_in4,nome_in1
        quantid_pecas1,quantid_pecas4 = quantid_pecas4,quantid_pecas1
        tamanho_nome_inv1,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv1

    if m2 < m3:
        m2,m3 = m3,m2
        nome_in2,nome_in3 = nome_in3,nome_in2
        quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
        tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

    if m3 < m1:
        m3,m1 = m1,m3
        nome_in3,nome_in1 = nome_in1,nome_in3
        quantid_pecas3,quantid_pecas1 = quantid_pecas1,quantid_pecas3
        tamanho_nome_inv3,tamanho_nome_inv1 = tamanho_nome_inv1,tamanho_nome_inv3

    if m2 < m3:
        m2,m3 = m3,m2
        nome_in2,nome_in3 = nome_in3,nome_in2
        quantid_pecas2,quantid_pecas3 = quantid_pecas3,quantid_pecas2
        tamanho_nome_inv2,tamanho_nome_inv3 = tamanho_nome_inv3,tamanho_nome_inv2

#m3 == m4
if m3 == m4:

    parametro3 = 0
    parametro4 = 0

    if quantid_pecas3 > 25:
        parametro3 = parametro3 + 1

    if tamanho_nome_inv3 > 15:
        parametro3 = parametro3 + 1

    if quantid_pecas4 > 25:
        parametro4 = parametro4 + 1

    if tamanho_nome_inv4 > 15:
        parametro4 = parametro4 + 1

    if parametro3 < parametro4:
        m3,m4 = m4,m3
        nome_in3,nome_in4 = nome_in4,nome_in3
        quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3
        tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3

    elif parametro3 == parametro4:

        if quantid_pecas3 < quantid_pecas4:
            m3,m4 = m4,m3
            nome_in3,nome_in4 = nome_in4,nome_in3
            quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3
            tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3

        else:
            if tamanho_nome_inv3 < tamanho_nome_inv4:
                m3,m4 = m4,m3
                nome_in3,nome_in4 = nome_in4,nome_in3
                quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3
                tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3

    if m4 < m1:
        m4,m1 = m1,m4
        nome_in4,nome_in1 = nome_in1,nome_in4
        quantid_pecas4,quantid_pecas1 = quantid_pecas1,quantid_pecas4
        tamanho_nome_inv4,tamanho_nome_inv1 = tamanho_nome_inv1,tamanho_nome_inv4

    if m1 < m2:
        m1,m2 = m2,m1
        nome_in1,nome_in2 = nome_in2,nome_in1
        quantid_pecas1,quantid_pecas2 = quantid_pecas2,quantid_pecas1
        tamanho_nome_inv1,tamanho_nome_inv2 = tamanho_nome_inv2,tamanho_nome_inv1

    if m3 < m4:
        m3,m4 = m4,m3
        nome_in3,nome_in4 = nome_in4,nome_in3
        quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3
        tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3

    if m4 < m1:
        m4,m1 = m1,m4
        nome_in4,nome_in1 = nome_in1,nome_in4
        quantid_pecas4,quantid_pecas1 = quantid_pecas1,quantid_pecas4
        tamanho_nome_inv4,tamanho_nome_inv1 = tamanho_nome_inv1,tamanho_nome_inv4

    if m3 < m4:
        m3,m4 = m4,m3
        nome_in3,nome_in4 = nome_in4,nome_in3
        quantid_pecas3,quantid_pecas4 = quantid_pecas4,quantid_pecas3
        tamanho_nome_inv3,tamanho_nome_inv4 = tamanho_nome_inv4,tamanho_nome_inv3

print(f'1º lugar - {nome_in1} : {m1} pontos\n2º lugar - {nome_in2} : {m2} pontos\n3º lugar - {nome_in3} : {m3} pontos\n4º lugar - {nome_in4} : {m4} pontos')

    


    



    












































               
        
        
            

            
