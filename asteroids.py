# program template for Spaceship
import simplegui
import math
import random

#THANK YOU FOR REVIEWING MY CODE! 
#I LEARNED A LOT FROM YOUR COMMENTS DURING THIS COURSE,
#AND THEY KEPT ME MOTIVATED!

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
SCREEN_SIZE = [ WIDTH, HEIGHT]

#SHIP
SHIP_ACC = 0.09
SHIP_ANG_ACC = 0.01
SPACE_ANG_FRI = 0.93
SPACE_FRI = 0.99
NOSE = 35

#ROCK
ROCK_RANGE_MIN = 1
ROCK_VEL_MAX = 0.9
ROCK_ANG_ST = 6.28318531
ROCK_ANG_MAX = 0.1888

#WEAPONS
MISSILE_SPEED = 5
WEAPONSLIST = {0: "BLUEPLASMA",
              1: None
              }

#SECRET MESSAGE
S_MESSAGE = "THANK YOU FOR REVIEWING MY CODE! I LEARNED A LOT FROM YOUR COMMENTS DURING THIS COURSE, AND THEY KEPT ME MOTIVATED!"

class RGBcolor:
    
    # create color with specified intensities
    def __init__(self, red, green, blue, alpha = 1):
        self.red = red
        self.green = green
        self.blue = blue
        self.alpha = alpha

    # make HTML color string
    def make_html(self):
        return "rgba(" + str(self.red) + ", " + str(self.green) + ", " + str(self.blue) + ", " + str(self.alpha) + ")"
    
    # print out readable representation
    def __str__(self):
        return "Red: " + str(self.red) + ", Green: " + str(self.green) + ", Blue: " + str(self.blue) + ", Alpha: " + str(self.alpha)
    
    # brighten towards white
    def brighten(self):
        self.red += 1
        self.green += 1
        self.blue += 1



#GUI
SCORE_POS = [SCREEN_SIZE[0]-300,50]
LIVES_POS = [10,50]
TEXT_SIZE = 40
TEXT_COLOR = RGBcolor(100,100,100).make_html()
TEXT_SERIF = "monospace"
PNAME_POS = [(SCREEN_SIZE[0]/3)-30,SCREEN_SIZE[1]-40]



class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.s2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blend.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


class GameGUI:
    
    def __init__(self, lives = 5, score = 0,  player_name = "Jogando com Nils"):
        self.player_name = player_name
        self.lives = lives
        self.score = score
    

    def draw(self,canvas):
        #LIVES        
        canvas.draw_text("lives: "+ str(self.lives), LIVES_POS, TEXT_SIZE, TEXT_COLOR, TEXT_SERIF)
        
        
        #SCORE
        canvas.draw_text("score: "+ str(self.score), SCORE_POS, TEXT_SIZE, TEXT_COLOR, TEXT_SERIF)
        
        #NAME
        canvas.draw_text(self.player_name, PNAME_POS, TEXT_SIZE, TEXT_COLOR, TEXT_SERIF)
    
    def update(self):
        pass


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.POSAXIS = 2
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.acc = [0, 0]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0.0
        self.angle_acc = 0.0
        self.rotation = False
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.nose = [0,0]
        
        
    def update_nose(self):        
        fa = angle_to_vector(self.angle)
        for i in range(self.POSAXIS):
            self.nose[i] = self.pos[i]+(fa[i]*NOSE)
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0]+self.image_size[0],self.image_center[1]], self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def __move_variation(self):
        if self.rotation:
            self.angle_vel += self.angle_acc
            
        self.angle += self.angle_vel
        self.angle_vel *= SPACE_ANG_FRI
        
        if self.thrust:
            self.acc = angle_to_vector(self.angle)
        else:
            self.acc = [0, 0]
            
        for i in range(self.POSAXIS):
            self.vel[i] += self.acc[i]*SHIP_ACC
            self.pos[i] = (self.pos[i]+self.vel[i]) % SCREEN_SIZE[i]
            self.vel[i] *= SPACE_FRI
        
        
        
            
            #position[d] = (position[d] + vector[d]) % SCREEN_SIZE[d]
    
    def thrust_on(self, f_acc):
        global ship_thrust_sound
        ship_thrust_sound.play()
        #ship_thrust_sound.set_volume(0.7)
        self.thrust = True
        self.acc = f_acc
    
    def thrust_off(self):
        global ship_thrust_sound
        ship_thrust_sound.rewind()
        self.thrust = False
        
    
    def update_angle(self, angle_acc):
        if angle_acc == 0:
            self.stop_rotation()
        else:
            self.rotation = True
            self.angle_acc = angle_acc
            
        
    def stop_rotation(self):
        self.rotation = False
    
    def update(self):
        self.__move_variation()
        self.update_nose()        
        
    #weapons
    def shoot_missile(self, weapon_mode):
        global a_missile
        missile_speed = angle_to_vector(self.angle)
        for i in range(self.POSAXIS):
            missile_speed[i]= self.vel[i]+(MISSILE_SPEED*missile_speed[i])
        a_missile = Sprite(self.nose,
                           missile_speed,
                           self.angle,
                           0,
                           missile_image, missile_info, missile_sound)
        
    
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.POSAXIS = 2
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        
        for i in range(self.POSAXIS):        
            self.pos[i] = ( self.pos[i] + self.vel[i]) % SCREEN_SIZE[i]
               

           
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    gui.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    derection_size = 3
    direction = [1,1,1]
    for i in range(derection_size):
        direction[i] = 1 if random.random()>.5 else -1
    
    a_rock = Sprite([random.random() * (WIDTH - ROCK_RANGE_MIN) + ROCK_RANGE_MIN,
                     random.random() * (HEIGHT - ROCK_RANGE_MIN) + ROCK_RANGE_MIN],
                    [direction[0]*random.random()*ROCK_VEL_MAX, direction[1]* random.random()*ROCK_VEL_MAX],
                    random.random()*ROCK_ANG_ST,
                    direction[2]*random.random()*ROCK_ANG_MAX,
                    asteroid_image, asteroid_info)

def donada():
    pass
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize gameui
gui = GameGUI(lives,score)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 4, HEIGHT / 4], [1, -1], 1,0.1888, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

#inputs
inputs = {"up": [my_ship.thrust_on,[SHIP_ACC,SHIP_ACC],my_ship.thrust_off],
          #"down": [1, 2],
          "space": [my_ship.shoot_missile,WEAPONSLIST[0],donada],
          "left": [my_ship.update_angle,-SHIP_ANG_ACC,my_ship.stop_rotation],
          "right": [my_ship.update_angle,SHIP_ANG_ACC,my_ship.stop_rotation]
          }


def keydown(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i][0](inputs[i][1])

def keyup(key):
    for i in inputs:
        if key == simplegui.KEY_MAP[i]:
            inputs[i][2]()

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
