#modelo da torre de hanoi, ou seja, 2**n - 1 é a quantidade de movimentos necessários
def mover_fun(base, num):

    if num == 0:
        return 1
    
    else:
        movimento = base * mover_fun(base, num-1)
        return movimento 

base = 2  #base que receberá o expoente(qtd de livros)
n = int(input())  #livros a serem movidos 

qtd_movimento = mover_fun(base, n) - 1    #calcula a quantos movimentos foram realizados 
print(f"Bela moveu os {n} livros em {qtd_movimento} movimentos para o Pedestal de Marfim.")