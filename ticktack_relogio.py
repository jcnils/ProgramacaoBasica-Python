#Exemplo de programa orientado a eventos

#Importar o modulo de GUI - simpleGUI
import simplegui

segundos = 0

#definir controladores (handler)
def tick():
    global segundos
    segundos += 1
    #if(segundos%2==0):
        #print "tack"
    #else:
        #print "tick"
    
    
def horas():
    global segundos
    horas = segundos / 3600 
    minutos = ( segundos % 3600 )/ 60
    segundos_hora = ( segundos % 3600 )% 60
    
    print horas, ":" , minutos, ":", segundos_hora
    #print segundos
    
timer_tick = simplegui.create_timer(1000, tick)
timer_horas = simplegui.create_timer(5000, horas)

timer_tick.start()
timer_horas.start()
