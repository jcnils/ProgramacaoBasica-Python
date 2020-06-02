# Para proxima live, fazer multiplicacao, divisao e subtracao

import simplegui

resultado = 0

# Handler for mouse click
def soma():
    global resultado
    resultado = float(inp1.get_text()) + float(inp2.get_text())
    
    
def input_handler1(text_input):
    pass
    
def input_handler2(text_input):
    pass

# Handler to draw on canvas
def draw(canvas):  
    canvas.draw_text(str(resultado), [112,112], 48, "White")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 300, 200)

inp1 = frame.add_input('Valor 1', input_handler1, 50)
inp2 = frame.add_input('Valor 2', input_handler2, 50)

inp1.set_text("0")
inp2.set_text("0")

frame.add_button("soma", soma)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()
