import random #aleatorio

print "Battletoads, Galerinha!"
print "##JOGO ADIVINHE O NUMERO##"
print 
#JOGO ADIVINHE O NUMERO
NUM_OPCOES = 2

def imprimir_resultado(numero_escolhido, num_pens):
    print "O numero escolhido foi :", numero_escolhido, " e o numero pensado foi: ", num_pens

def num_pensado():
    num = random.randrange(0,NUM_OPCOES)
    return num

def escolha_num(numero_escolhido):
    num_pens = num_pensado()
    imprimir_resultado(numero_escolhido, num_pens)
    if (numero_escolhido == num_pens):
        print "Parabens, voce venceu"
    else:
        print "Perdeu"
    print

        
escolha_num(0)
escolha_num(0)
escolha_num(0)
escolha_num(0)
