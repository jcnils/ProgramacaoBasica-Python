#Logica
a = True
print type(a)
b = False
c = False
d = True

print "A variavel a e ", a
print "A variavel b e ", b

print "A variavel a nao e ", not a
print "A variavel b nao e ", not b

print "A e B ", a and b
print "A ou B ", a or b

print ((a and b) or (c and (not d)))

print

#>  :  maior
#<  :  menor
#>= :  maior ou igual
#<= :  menor ou igual
#== :  comparar igual
#!= :  diferente

z = 10
x = 16
y = 7

print z > y
e = x > z
print e

pos_personagem = 1
print "continua andando ", pos_personagem < 1
print
#exemplos em jogo
print "comecou o jogo"
tem_chave = False

def abreporta(tem_chave):
    print "O jogador tenta abrir a porta"
    if tem_chave : print "A porta foi aberta"
    else         : print "A porta permanece fechada"
    print


abreporta(tem_chave)

tem_chave = True 

abreporta(tem_chave)

print "comecou o jogo"
exodia_tronco = False
exadia_perna_esquerda = False
exadia_perna_direita = False
exadia_braco_esquerdo = False
exadia_braco_direito = False

def ganhou_jogo():
    if exodia_tronco and exadia_perna_esquerda and exadia_perna_direita and exadia_braco_esquerdo and exadia_braco_direito:
        print "Ganhou o jogo"
    else:
        print "Proxima rodada"
    print

    
ganhou_jogo()
exodia_tronco = True
ganhou_jogo()
ganhou_jogo()
exadia_perna_esquerda = True
exadia_perna_direita = True
exadia_braco_esquerdo = True
exadia_braco_direito = True
ganhou_jogo()
