velocidade_IJ = int(input())
velocidade_LR = int(input())
dificuldade_inimigos = int(input())
pj = (velocidade_IJ*velocidade_LR)/dificuldade_inimigos

if pj < 65000:
    print('BRUTAL! Ninguém jamais conseguiu alcançar as pontuações fantásticas do Jorel.')

if 65000<pj<=99000:
    print('INCRÍVEL! A dupla conseguiu alcançar o top 10 nas pontuações do jogo.')

if 99000<pj<=153000:
    print('SENSACIONAL!! Os jogadores conseguiram alcançar o pódio do jogo ao lado das outras pontuações do Jorel.') 

if pj > 153000:
    print('IMPOSSÍVEL!!! A DUPLA IMPLACÁVEL FOI CAPAZ DE QUEBRAR O RECORDE INALCANÇÁVEL DO JOREL!')   
    
