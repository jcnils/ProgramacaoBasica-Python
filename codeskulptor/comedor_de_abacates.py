
import simplegui

abacate = 0

# Handler for mouse click
def comer_abacate():
    global abacate
    abacate += 1

# Handler to draw on canvas
def draw(canvas):
    global abacate
    mensagem = 'Comeram {0} abacates'.format(abacate) 
    canvas.draw_text(mensagem, [50,112], 48, "Green")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Comedor de Abacates", 600, 300)
frame.add_button("Coma um abacate", comer_abacate)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
