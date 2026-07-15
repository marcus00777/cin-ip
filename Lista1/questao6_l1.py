#Disponibilidade
robin_disponibilidade = (input())
estelar_disponibilidade = (input())
ciborgue_disponibilidade = (input())
ravena_disponibilidade = (input())
mutano_disponibilidade = (input())

ravena = 'Ravena'
estelar = 'Estelar'
mutano = 'Mutano'
robin = 'Robin'
ciborgue = 'Ciborgue'

a = 2
b = 3
c = 4

#Ninguém se candidatar
#NNNNN
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print('Parece que ninguém quer participar da Liga da Justiça, o Batman vai ter que ouvir um Super-Esculacho do Super-Homem por não ter conseguido ninguém super forte!')
   print('Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT.')
   print('Que bom que tudo deu certo, sem dificuldades!')

#Candidatos solitários
#Disp. de Robin
#SNNNN
if robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
   print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#Disp. de Estelar
#NSNNN
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
     print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
     print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
     print('Que bom que tudo deu certo, sem dificuldades!')

#Disp. de Ravena
#NNNSN
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
   print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#Disp. de Mutano
#NNNNS
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
   print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
   print('O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#Disp. de ciborgue
#NNSNN
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print('Através de um processo seletivo rigoroso, o mais novo integrante da Liga da Justiça foi escolhido!')
   print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
   print('Que bom que tudo deu certo, sem dificuldades!')

#Dilemas amorosos
#se robin e estelar
#SSNNN
if robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {estelar} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {estelar}!')
   print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
   print('Parece que o cavalherismo ainda não morreu não é mesmo?')

#SNSNN
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
   print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#SNNSN
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
   print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#SNNNS
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
   print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#NSNSN
elif robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#NNSSN
elif robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#NSSNN
elif robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {a} candidatos, o(a) {estelar} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {estelar}!')
   print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#NSNNS
elif robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {a} candidatos, o(a) {estelar} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {estelar}!')
   print('Com a fúria de Tamaran e o brilho das suas rajadas, a Estelar vai iluminar o caminho da Liga da Justiça!')
   print('Que bom que tudo deu certo, sem dificuldades!')



#se ravena e mutano
# NNNSS
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {a} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Parece que o cavalherismo ainda não morreu não é mesmo?')

#Disputa do tofu
#NNSNS
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
   quantidade_mutano = int(input())
   quantidade_ciborgue = int(input())
   if quantidade_ciborgue > quantidade_mutano:
      print(f'Mesmo com {a} candidatos, o(a) {ciborgue} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ciborgue}!')
      print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
      print('Nem uma competição árdua assim pode abalar a amizade desses caras!')

   elif quantidade_mutano > quantidade_ciborgue:
      print(f'Mesmo com {a} candidatos, o(a) {mutano} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {mutano}!')
      print('O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
      print('Nem uma competição árdua assim pode abalar a amizade desses caras!')

   elif quantidade_ciborgue == quantidade_mutano:
      nome_escolhido = str(input())
      if nome_escolhido == mutano:
         print(f'Mesmo com {a} candidatos, o(a) {mutano} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {mutano}!')
         print('O herói mais versátil da torre está pronto para mostrar que tamanho não é documento, especialmente se ele virar um tiranossauro!')
         print('Nem uma competição árdua assim pode abalar a amizade desses caras!')
      elif nome_escolhido == ciborgue:
         print(f'Mesmo com {a} candidatos, o(a) {ciborgue} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ciborgue}!')
         print('BOOYAH! A tecnologia de ponta do Ciborgue agora faz parte do arsenal da Liga. Até parece que já foi antes...')
         print('Nem uma competição árdua assim pode abalar a amizade desses caras!')

#liderança inquestionável
#SSSNN
if robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {b} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
   print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!') 
   print('Que bom que tudo deu certo, sem dificuldades!')
  
#SSNNS     
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
    print(f'Mesmo com {b} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
    print('Que bom que tudo deu certo, sem dificuldades!')

#SNNSS
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
    print(f'Mesmo com {b} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
    print('Que bom que tudo deu certo, sem dificuldades!')
  
#SNSNS
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
    print(f'Mesmo com {b} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!') 
    print('Que bom que tudo deu certo, sem dificuldades!')

#SNSSN
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
    print(f'Mesmo com {b} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!') 
    print('Que bom que tudo deu certo, sem dificuldades!')


#Ravena não se candidatar e for escolhida
#NSSSS
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {b} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#NSSSN
elif robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {b} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#NSNSS
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {b} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')

#SSNSN
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
    print(f'Mesmo com {b} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!') 
    print('Que bom que tudo deu certo, sem dificuldades!')


#NNSSS
elif robin_disponibilidade == 'N' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {b} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('Que bom que tudo deu certo, sem dificuldades!')


#liderança inquestionável
#SSSSN
if robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'N':
   print(f'Mesmo com {c} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
   print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
   print('Que bom que tudo deu certo, sem dificuldades!')
  
#SSSNS     
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
    print(f'Mesmo com {c} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
    print('Que bom que tudo deu certo, sem dificuldades!')

#SSNSS
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'N' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
    print(f'Mesmo com {c} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!') 
    print('Que bom que tudo deu certo, sem dificuldades!')
 
#SNSSS
elif robin_disponibilidade == 'S' and estelar_disponibilidade == 'N' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
    print(f'Mesmo com {c} candidatos, o(a) {robin} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {robin}!')
    print('Finalmente, Batman e Robin lado a lado, agora como iguais na Liga, será que o Menino Prodígio se provar digno do cargo?!')
    print('Que bom que tudo deu certo, sem dificuldades!')
 

#Ravena não se candidatar, robin não se candidatar e ravena for escolhida
#NSSNS
if robin_disponibilidade == 'N' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'N' and mutano_disponibilidade == 'S':
   print(f'Mesmo com {b} candidatos, o(a) {ravena} foi selecionado(a)! O Superman ficaria impressionado com o novo SUPER membro da Liga! Seja bem-vindo(a) {ravena}!')
   print('Não tinha como a filha de Trigon não ser a escolhida, a mais forte dos Titãns vai botar os inimigos da Liga para correr!')
   print('O Batman não iria perder a chance de ter um dos seres mais poderosos do Universo DC no time, o preparo dele não permite isso!')
  

#Diponibilidade geral
if robin_disponibilidade == 'S' and estelar_disponibilidade == 'S' and ciborgue_disponibilidade == 'S' and ravena_disponibilidade == 'S' and mutano_disponibilidade == 'S':
   print('Em toda a vida do Batman, ele nunca viu um lugar tão caótico quanto a torre dos titãns depois da notícia, nem mesmo Gotham, com isso ele percebe que não seria ali o local ideal para encontrar o novo salvador da terra!')
   print('Poxa, mas que pena, os Titãns vão ter que esperar mais um pouco antes de darem mais um passo na carreira, se continuar assim, vão assinar a CLT.')
   print('Que bom que tudo deu certo, sem dificuldades!')         
                  
         
      
      





