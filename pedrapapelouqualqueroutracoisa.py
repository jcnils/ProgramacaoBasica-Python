import random

# aguia      = 0
# cobra      = 1
# borracha   = 2
# esqueiro   = 3
# grafite    = 4

OPCAO0_STR = "aguia"
OPCAO1_STR = "cobra"
OPCAO2_STR = "borracha"
OPCAO3_STR = "esqueiro"
OPCAO4_STR = "grafite"

NUMERO_OPCOES = 5

#funcao que retorna um nome dado um numero
def numero_em_nome(numero):	
    if   numero == 0: return OPCAO0_STR
    elif numero == 1: return OPCAO1_STR
    elif numero == 2: return OPCAO2_STR
    elif numero == 3: return OPCAO3_STR
    elif numero == 4: return OPCAO4_STR
    else:             return None

#funcao que retorna um numero dado um nome
def nome_em_numero(nome):
    if   nome == OPCAO0_STR  : return 0
    elif nome == OPCAO1_STR  : return 1
    elif nome == OPCAO2_STR  : return 2
    elif nome == OPCAO3_STR  : return 3
    elif nome == OPCAO4_STR  : return 4
    else:             return None
    return 0


def ppt(nome):
    #converter o nome em numer
    numero_jogador = nome_em_numero(nome)
    numero_computador = random.randrange(0,NUMERO_OPCOES)
    diferenca = (numero_jogador - numero_computador) % NUMERO_OPCOES
    
    print "Escolha do jogador: ", nome
    print "Escolha do computador: ", numero_em_nome(numero_computador)
    
    #print diferenca
    
    if diferenca == 0  : print "EMPATE"        
    elif diferenca > 2: print "Jogador venceu"
    else: 			     print "Computador venceu"
  
    print
    
    
#testar o nosso codigo
#print numero_em_nome(2)
#print nome_em_numero(TESOURA_STR)


#execucao do jogo

ppt(OPCAO0_STR)
ppt(OPCAO1_STR)
ppt(OPCAO2_STR)
ppt(OPCAO3_STR)
ppt(OPCAO4_STR)

ppt(OPCAO0_STR)
ppt(OPCAO1_STR)
ppt(OPCAO2_STR)
ppt(OPCAO3_STR)
ppt(OPCAO4_STR)

ppt(OPCAO0_STR)
ppt(OPCAO1_STR)
ppt(OPCAO2_STR)
ppt(OPCAO3_STR)
ppt(OPCAO4_STR)

ppt(OPCAO0_STR)
ppt(OPCAO1_STR)
ppt(OPCAO2_STR)
ppt(OPCAO3_STR)
ppt(OPCAO4_STR)


#ppt("tesoura")
#ppt("pedra")
#ppt("papel")
