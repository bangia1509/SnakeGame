#snake game
import turtle
import time
import random

delay=0.005
headlog=[]
bodylog=[]

#setting up a screen
window=turtle.Screen()
window.title("Ansh Bangia's SNAKE GAME")
window.bgcolor('lightblue')
window.setup(width=600, height=600)
window.tracer(0) #turns off screen updates

#snake head
head=turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('purple')
head.penup()
head.goto(0,0)
head.direction='stop'

#food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(random.randrange(-280,280,20),random.randrange(-280,220,20))

snakebod=[]

#to write on screen
name=turtle.Turtle()
name.speed(0)
name.color('darkred')
name.penup()
name.hideturtle()
name.goto(0,250)
name.write("ANSH BANGIA'S SNAKE GAME",align='center',font=('Times New Roman',27,'underline'))
pen=turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('darkblue')
pen.penup()
pen.hideturtle()
pen.goto(0,220)
pen.write('SCORE: 0   HIGH SCORE: 0',align='center', font=('Courier',24,'normal'))

score=0
high_score=0

#move head
def moveup():
    if head.direction!='down':
        head.direction='up'
def moveleft():
    if head.direction!='right':
        head.direction='left'
def moveright():
    if head.direction!='left':
        head.direction='right'
def movedown():
    if head.direction!='up':
        head.direction='down'
def move():
    if head.direction=='up':
        head.sety(head.ycor()+1)

    if head.direction=='down':
        head.sety(head.ycor()-1)

    if head.direction=='left':
        head.setx(head.xcor()-1)

    if head.direction=='right':
        head.setx(head.xcor()+1)
    if len(headlog)<20:
        headlog.append([head.xcor(),head.ycor()])
    else:
        del headlog[0]
        headlog.append([head.xcor(),head.ycor()])

#keyboard input
window.listen()
window.onkeypress(moveup,'Up')
window.onkeypress(movedown,'Down')
window.onkeypress(moveleft,'Left')
window.onkeypress(moveright,'Right')
window.onkeypress(moveup,'w')
window.onkeypress(movedown,'s')
window.onkeypress(moveleft,'a')
window.onkeypress(moveright,'d')
#main game loop
while True:
    window.update()
    

##    #collision border
##    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
##        #delay=0.1
##        score=0
##        pen.clear()
##        pen.write('SCORE %d   HIGH SCORE: %d'%(score, high_score),align='center', font=('Courier',24,'normal'))
##        time.sleep(1)
##        head.goto(0,0)
##        head.direction='stop'
##        for j in snakebod:
##            j.hideturtle()
##        snakebod.clear()
##        headlog.clear()
##        bodylog.clear()

    #collision border
    if head.xcor()>315 or head.xcor()<-315:
        head.setx(head.xcor()-615 if head.xcor()>0 else head.xcor()+615)
    if head.ycor()>315 or head.ycor()<-315:
        head.sety(head.ycor()-615 if head.ycor()>0 else head.ycor()+615)
        
    
    #collision food
    if head.distance(food)<20:
        #delay-=0.002
        x=random.randrange(-280,280,20)
        y=random.randrange(-280,220,20)
        food.goto(x,y)
        newbod=turtle.Turtle()
        newbod.speed(0)
        newbod.shape('circle')
        newbod.color('black')
        newbod.penup()
        snakebod.append(newbod)
        bodylog.append([])
        score+=5
        if score>high_score:
            high_score=score
        pen.clear()
        pen.write('SCORE %d   HIGH SCORE: %d'%(score, high_score),align='center', font=('Courier',24,'normal'))

    #moving body    
    for i in range(len(snakebod)-1,0,-1):
        x=bodylog[i-1][0][0]
        y=bodylog[i-1][0][1]
        snakebod[i].goto(x,y)
        if len(bodylog[i])<20:
            bodylog[i].append([x,y])
        else:
            del bodylog[i][0]
            bodylog[i].append([x,y])
    if len(snakebod)>0:
        x=headlog[0][0]
        y=headlog[0][1]
        snakebod[0].goto(x,y)
        if len(bodylog[0])<20:
            bodylog[0].append([x,y])
        else:
            del bodylog[0][0]
            bodylog[0].append([x,y])
        

    move()

    #collision body
    for bod in snakebod:
        if bod.distance(head)<10:
            #delay=0.1
            score=0
            pen.clear()
            pen.write('SCORE %d   HIGH SCORE: %d'%(score, high_score),align='center', font=('Courier',24,'normal'))
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for j in snakebod:
                j.hideturtle()
            snakebod.clear()
            headlog.clear()
            bodylog.clear()
            break
    
    time.sleep(delay)

window.mainloop()
