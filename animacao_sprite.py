import simplegui

#Dados da imagem do player
LARGURA_SPLAYER = 	120
ALTURA_SPLAYER	=	24
PEDACOSH_SPLAYER=	5
PEDACOSV_SPLAYER=	1
ALTURA_LARGURA_PLAYER = (LARGURA_SPLAYER/PEDACOSH_SPLAYER, ALTURA_SPLAYER/PEDACOSV_SPLAYER)

i = 0
#CENTRO_SPRITE_PLAYER = (((LARGURA_SPLAYER/PEDACOSH_SPLAYER+(i*48) )// 2),
#                       (ALTURA_SPLAYER/PEDACOSV_SPLAYER // 2))


def timer_handler():
    global i
    i += 1




def draw_handler(canvas):
  global i
  i = i % 5
  canvas.draw_image(image, (((LARGURA_SPLAYER/PEDACOSH_SPLAYER+(i*48) )// 2),
                       (ALTURA_SPLAYER/PEDACOSV_SPLAYER // 2)),
                            ALTURA_LARGURA_PLAYER, (250, 250), (240, 240))

image = simplegui.load_image('http://i.imgur.com/vZvMeuH.png')

frame = simplegui.create_frame('Testing', 500, 500)
frame.set_draw_handler(draw_handler)
frame.start()


timer = simplegui.create_timer(100, timer_handler)
timer.start()



