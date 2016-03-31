import random #aleatorio

print "Battletoads, Galerinha!"
print "##JOGO SPRAY, ESCUDO, AGUA, VARINHA, BODE, ESPADA E FOGO##"
print 
#JOGO SPRAY, ESCUDO, AGUA, VARINHA, BODE, ESPADA E FOGO
NUM_OPCOES = 7

# SPRAY   = 0
# ESCUDO  = 1
# AGUA    = 2
# VARINHA = 3 
# BODE    = 4
# ESPADA  = 5
# FOGO    = 6

OPCAO0 = "spray"
OPCAO1 = "escudo"
OPCAO2 = "agua"
OPCAO3 = "varinha"
OPCAO4 = "bode"
OPCAO5 = "espada"
OPCAO6 = "fogo"

def nome_em_numero(nome):
    if   nome == OPCAO0 :	return 0
    elif nome == OPCAO1 : 	return 1
    elif nome == OPCAO2 : 	return 2
    elif nome == OPCAO3 : 	return 3
    elif nome == OPCAO4 : 	return 4
    elif nome == OPCAO5 : 	return 5
    elif nome == OPCAO6 : 	return 6
    else				:	return None
    
    
def numero_em_nome(numero):
    if   numero == 0	   :	return OPCAO0
    elif numero == 1 	   : 	return OPCAO1
    elif numero == 2 	   : 	return OPCAO2
    elif numero == 3 	   : 	return OPCAO3
    elif numero == 4 	   : 	return OPCAO4
    elif numero == 5 	   : 	return OPCAO5
    elif numero == 6 	   : 	return OPCAO6
    else				   :	return None
    
def imprimir_resultado(escolhajogador, escolhapc):
    print "O jogador escolheu :", escolhajogador
    print "O computador escolheu: ", escolhapc

    
    
def seavbef(opcao):
    #converte o texto em numero
    numjogador = nome_em_numero(opcao)
    numcomputador = random.randrange(0, NUM_OPCOES)
    diferenca = (numjogador - numcomputador) % NUM_OPCOES
    
    imprimir_resultado(opcao, numero_em_nome(numcomputador))
                       
    #diferencas
    
    if(diferenca == 0)    : print "EMPATE"
    elif  diferenca <= 3  : print "Parabens, voce venceu"
    else                  : print "O computador venceu"
    print
        
seavbef(OPCAO0)
seavbef(OPCAO0)
seavbef(OPCAO0)
seavbef(OPCAO0)
seavbef(OPCAO1)
seavbef(OPCAO2)
seavbef(OPCAO3)
seavbef(OPCAO4)
seavbef(OPCAO5)
seavbef(OPCAO6)
