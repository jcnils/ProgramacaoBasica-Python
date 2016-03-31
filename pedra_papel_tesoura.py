import random #aleatorio

print "Battletoads, Galerinha!"
print "##JOGO PEDRA, PAPEL E TESOURA##"
print 
#JOGO PEDRA, PAPEL E TESOURA#
NUM_OPCOES = 3

# TESOURA = 0
# PAPEL = 1
# PEDRA = 2

OPCAO0 = "tesoura"
OPCAO1 = "papel"
OPCAO2 = "pedra"
#OPCAO3 = "nnnn"
#OPCAON = "mmmm"

def nome_em_numero(nome):
    if   nome == OPCAO0 :	return 0
    elif nome == OPCAO1 : 	return 1
    elif nome == OPCAO2 : 	return 2
    else				:	return None
    
    
def numero_em_nome(numero):
    if   numero == 0	   :	return OPCAO0
    elif numero == 1 	   : 	return OPCAO1
    elif numero == 2 	   : 	return OPCAO2
    else				   :	return None
    
def imprimir_resultado(escolhajogador, escolhapc):
    print "O jogador escolheu :", escolhajogador
    print "O computador escolheu: ", escolhapc

    
    
def ppt(opcao):
    #converte o texto em numero
    numjogador = nome_em_numero(opcao)
    numcomputador = random.randrange(0, NUM_OPCOES)
    diferenca = (numjogador - numcomputador) % NUM_OPCOES
    
    imprimir_resultado(opcao, numero_em_nome(numcomputador))
                       
    #diferencas
    
    if(diferenca == 0)    : print "EMPATE"
    elif  diferenca == 2  : print "Parabens, voce venceu"
    else                  : print "O computador venceu"
    print
        
ppt("tesoura")
ppt("tesoura")
ppt("tesoura")
ppt("tesoura")
ppt("papel")
ppt("pedra")
