#funções
LADOA = 8
LADOB = 10


#funcao calcula area rectangulo
#def nome_funcao(par1,par2,par3,...,parN):
def area_rectangulo(largura,altura):
    area = largura * altura
    return area
    
def area_rectangulo_global():
    area = LADOA * LADOB
    return area    
    
    
rectangulo = area_rectangulo(4,3)
print rectangulo
print area_rectangulo(2,3)
print "######"
print

print area_rectangulo(LADOA,LADOB)
print area_rectangulo_global()

print "######"
print 
# Funções de idade
def imprime_idade():
    print nome, " tem ", idade, " anos"

def passou_umano(idade):
    #idade = idade + 1
    idade += 1
    print "Passou 1 ano"
    return idade

def envelhecer(idade, anos):
    idade += anos
    print "Passaram-se ", anos, " anos"
    return idade

def fonte_juventude(idade):
    idade -= 20
    print "Tomou um banho gostoso na fonte"
    return idade


nome = "ychuru"
idade = 16
imprime_idade()

idade = passou_umano(idade)

imprime_idade()

idade = envelhecer(idade,30)

imprime_idade()

idade = fonte_juventude(idade)

imprime_idade()


# Conversao de medidas
print "######"
print "Conversao de Medidas"
# Polegadas para centimetros: 1 polegada = 2,54 centimetros
POL_CEN_PESO = 2.54

def polegadas_p_centimetros(polegadas):
    centimetros = polegadas * POL_CEN_PESO
    return centimetros

# Centimetros para polegas
def centimetros_p_polegadas(centimetros):
    return centimetros / POL_CEN_PESO

polegadas = 6
centimetros = 15.24

print polegadas, " polegadas sao ",  polegadas_p_centimetros(polegadas), " centimetros"
print centimetros, " centimetros sao ",  centimetros_p_polegadas(centimetros), " polegadas"




#Conversao de temperatura
print "######"
print "Conversao de temperatura"
print 
#Converter de fahrenheit para celsius
def fahrenheit_p_celsius(temp_farrenheit):
    temp_celsius = (5.0 / 9.0) * (temp_farrenheit - 32)
    return temp_celsius

#Converter de celsius para fahrenheit
# c = (5.0 / 9.0) * (f - 32)
# 5/9*c = f - 32
# (5/9*c) + 32 = f
def celsius_p_fahrenheit(temp_celsius):
    return (9.0 / 5.0) * temp_celsius + 32

temp_celsius = 100
temp_farrenheit = 212
    
    
print temp_farrenheit, " farrenheit sao ", fahrenheit_p_celsius(temp_farrenheit), " celsius"
print temp_celsius, " celsius sao ", celsius_p_fahrenheit(temp_celsius), " farrenheit"
    
    
    
    
    
    
    
    
    
    

