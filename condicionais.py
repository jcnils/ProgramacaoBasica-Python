# se ("condiçao 1 verdadeira") faça
#	açao 1 realizada
# senão se ("condiçao 2 verdadeira") faça
#	açao 2 realizada
# senão se ("condiçao 3 verdadeira") faça
#	açao 3 realizada
# senão se ("condiçao N verdadeira") faça
#	açao N realizada
# senão
#   açao senao
# acao que deve sempre ser realizada

# se = if
# senao se = elif
# senao = else

numA = 10
numB = 11

print numA > numB
if numA > numB :
    print "Numero A e maior que numero B"
else:
    print "Numero B e maior que numero A"
print   
    
temChave = False
temChave = True
if temChave:
    print "A porta abriu"
else:
    print "A porta continua fechada"
       
print
vida_do_personagem = -30

if vida_do_personagem <= 0:
    vida_do_personagem = 0
    print "game over"
    
    
def tomar_pocao(vida_do_personagem):
    if  (75 <= vida_do_personagem < 100):
        return 10
    elif (25 < vida_do_personagem < 75):
        return 25
    elif vida_do_personagem <= 25:
        return 50

print "Vida = ", vida_do_personagem
print 
#efeito de pocao
print "efeito da pocao"
vida_do_personagem = 50
print "Vida = ", vida_do_personagem
vida_do_personagem += tomar_pocao(vida_do_personagem)   
print "Vida = ", vida_do_personagem
