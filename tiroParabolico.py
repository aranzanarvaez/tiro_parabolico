#tiroParabolico.py
#Carla Perez, Aranza Garcia 
#juego de lanzamiento de proyectiles

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []
score=0 #puntaje
writer = Turtle(visible=False)
sp=7 #velocidad

def tap(x, y):
    #Responde la tap de la pantalla
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x*sp+ 200) / 25
        speed.y = (y*sp + 200) / 25

def inside(xy):
    #Devuelve True si xy esta dentro de la pantalla
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    #Dibuja la pelota y los objetivos
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')
       

    if inside(ball):
        goto(ball.x, ball.y)
        dot(10, 'red')
    goto(0,190)
    write(score,font=("Arial",20))
        
    update()



def move():
    #Mueve la pelota y los objetivos

    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)
        

    for target in targets:
        target.x -= 0.5*sp #aumenta la veolocidad 
        
    if inside(ball):
        speed.y -= 0.35*sp #aumenta la velocidad
        ball.move(speed)
       
    dupe =targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)
        else: #si choca suma 1 al puntaje
            global score
            score+=1
            
    draw()

    for target in targets:
        if not inside(target):
            targets[targets.index(target)].x = 200       

    ontimer(move, 50)




setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
