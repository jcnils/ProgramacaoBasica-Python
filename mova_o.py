# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, and Safari.

# https://py3.codeskulptor.org/

# esse programa move o "o" quando você clica nos botões.

import simplegui

message = "o"
# [x, y]
posicao = [50,112]


# Handler for mouse click
def cima():
    global posicao
    posicao[1] -= 5
    
def baixo():
    global posicao
    posicao[1] += 5
    
def esquerda():
    global posicao
    posicao[0] -= 5
    
def direita():
    global posicao
    posicao[0] += 5



# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, posicao, 48, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("cima", cima)
frame.add_button("baixo", baixo)
frame.add_button("esquerda", esquerda)
frame.add_button("direita", direita)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
