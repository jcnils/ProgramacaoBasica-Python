import random #aleatorio

print "Battletoads, Galerinha!"
print "##JOGO PAR OU IMPAR##"
print 
#JOGO PAR OU IMPAR
NUM_OPCOES = 999

OPC_PAR = "par"
OPC_IMPAR = "impar"

def nome_em_numero(nome):
    if nome == OPC_PAR	   :	return 0
    elif nome == OPC_IMPAR : 	return 1
    else				   :	return None
    
def numero_em_nome(numero):
    if   numero == 0	   :	return OPC_PAR
    elif numero == 1 	   : 	return OPC_IMPAR
    else				   :	return None

def imprimir_resultado(escolhajogador, valorjogador, escolhapc):
    print "O jogador escolheu :", escolhajogador
    print "Valor do Jogador: ", valorjogador, " - Valor do computador: ", escolhapc


def escolha_do_computador():
    num = random.randrange(0,NUM_OPCOES)
    return num

def par_ou_impar(escolhajogador, valorjogador):
    escolhapc = escolha_do_computador()
    #qual a escolha do player
    num_comparacao = nome_em_numero(escolhajogador)
    imprimir_resultado(escolhajogador, valorjogador, escolhapc)   
    #checa se o resultado é do jogador    
    if ( (valorjogador + escolhapc) % 2 == num_comparacao ):
        
        print "Parabens, voce venceu! O resultado foi ", numero_em_nome(num_comparacao)
    else :

        print "Perdeu! O resultado foi ", numero_em_nome((num_comparacao+1)%2)
        
    print    
        
par_ou_impar("par", 4)    
par_ou_impar("par", 4)
par_ou_impar("par", 4)
par_ou_impar("par", 4)
par_ou_impar("par", 4)
par_ou_impar("par", 5)
par_ou_impar("impar", 4)
par_ou_impar("impar", 3)
