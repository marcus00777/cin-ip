moedas_dia = 0
quant_moeda = 0

print("Ô promessa sem jeito…")
print()

#Arrecadação em 7 dias
for c in range(1,8):

    print(f"Dia {c}: Quantas moedas João Grilo conseguiu arrecadar hoje?")

    moedas_dia = int(input())

    quant_moeda += moedas_dia

    print(f"No dia {c}, o baú já tem R$ {quant_moeda}")

print()
print(f"Total arrecadado após o plano: R$ {quant_moeda}")
print()

if quant_moeda == 0:
    print("João Grilo não conseguiu arrecadar nada... direto para o plano B!!")
    print()
    print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
    print()
    quantidade_desculpa = int(input())


    for x in range(1,quantidade_desculpa + 1):
        print(f"Digite a {x}ª desculpa:")
        desculpa = input()
        print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")


else:
    print("João Grilo começa a despedida da cachorra:")
    print("'Canis Mortus, Dinherus no Bolsus'")
    print("'Caro nostra quae in patina eius est, canis.'")
    print()

    print("João Grilo, o padeiro acreditou?")

    sinal = input().lower()

    if sinal == "sim":
        print("O padeiro acreditou! Chicó pode se casar com Rosinha!")
        print("Como o padeiro acreditou?")

    elif sinal == "não" or sinal == "nao":
        print("O padeiro não acreditou... João Grilo parte para o Plano B!")
        print()
        print("Quantas desculpas João Grilo precisa inventar para o Padeiro?")
        print()
        quantidade_desculpa = int(input())

        for x in range(1,quantidade_desculpa + 1):
            print(f"Digite a {x}ª desculpa:")
            desculpa = input()
            print(f"João Grilo disse: '{desculpa}'... e o padeiro caiu na conversa!")

print("Chicó: 'Não sei, só sei que foi assim!'")











