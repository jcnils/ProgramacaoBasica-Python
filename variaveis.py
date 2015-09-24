pi = 3.14
r = 5
print 2*pi*r
print 2*3.14*10
print 2*3.14*5
print 2*3.14*1

# variavel é um recipiente para armazenarmos valores
# importantes para usarmos em nosso código, nomeando
# para facilitar o entendimento.

# o nome da variavel pode ser definido com letras, números,
# travessão (_)
# sempre começa com uma letra, ou _

#nomes possivels de variaveis.
#nils, goal, minha_mae, count, xpto, nils69, _asd, WIDTH

#nomes invalidos.
# 69nils, #partiu, x-man, 69dlç, 24Tsu

#Conveção Python: minha_idade

# use o =  para atribuir valores para a variavel

minha_mae = "Black-Red"
print minha_mae

minha_mae = "Black-Red Team"
print minha_mae

# idades, fazer operacoes com as variaveis
idade_minha_mae = 16
print idade_minha_mae

idade_minha_mae = idade_minha_mae + 1
print idade_minha_mae

idade_minha_mae += 1 
print idade_minha_mae

injecao_velhice = 30

idade_minha_mae = idade_minha_mae + injecao_velhice
print idade_minha_mae

fonte_junventude = 20
idade_minha_mae -= 2* fonte_junventude
print idade_minha_mae

# Conversao de medidas
# Polegadas para centimetros: 1 polegada = 2,54 centimetros
pol_cen_peso = 2.54

polegadas = 6
centimentros = polegadas * pol_cen_peso
print centimentros

# Centimetros para polegas
centimentros = 15.24
polegadas = centimentros / pol_cen_peso
print polegadas

#Conversao de temperatura
#Converter de fahrenheit para celsius

temp_farrenheit = 212
temp_celsius = (5.0 / 9.0) * (temp_farrenheit - 32)
print temp_celsius

#Converter de celsius para fahrenheit
# c = (5.0 / 9.0) * (f - 32)
# 5/9*c = f - 32
# (5/9*c) + 32 = f

temp_celsius = 100
temp_farrenheit = (9.0 / 5.0) * temp_celsius + 32
print temp_farrenheit
