import turtle
import random
import time
delay=0.1
###########
score=0
high_score=0
#########
wn=turtle.Screen()
wn.bgcolor("green")
wn.setup(width=600,height=600)
wn.title("snke game using pyhton")
wn.tracer(0)
########segments #######
segments=[]
#####head###########
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0,0)
head.direction="stop"
#####functions for moment in the head########
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20)
    if head.direction=="down":
        head.sety(head.ycor()-20)
    if head.direction=="left":
        head.setx(head.xcor()-20)
    if head.direction=="right":
        head.setx(head.xcor()+20)
def move_up():
    if head.direction!="down":head.direction="up"

def move_down():
    if head.direction != "up": head.direction = "down"


def move_left():
    if head.direction != "right": head.direction = "left"


def move_right():
    if head.direction != "left": head.direction = "right"


wn.listen()
wn.onkeypress(move_up,"w")
wn.onkeypress(move_down,"s")
wn.onkeypress(move_left,"a")
wn.onkeypress(move_right,"d")

#######food for snake####
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,260)
##########for pen##########
pen=turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.hideturtle()
pen.penup()
pen.goto((0,260))

pen.write("SCORE :{} HIGH SCORE :{}".format(score,high_score),align="center",font=("courier", 24, "normal"))







while True:
    wn.update()

   #####border boundaries######
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()<-290 or head.ycor()>290:
        time.sleep(1)
        head.goto((0,0))
        head.direction="stop"
        for segment in segments:
            segment.goto((2000,2000))
        segments.clear()
        score=0
        delay=0.2
        pen.clear()
        pen.write("SCORE :{} HIGH SCORE :{}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    ######food colision######
    if head.distance(food) <20 :
       x=random.randint(-300,300)
       y=random.randint(-300,300)
       food.goto((x, y))
       new_segment=turtle.Turtle()
       new_segment.speed(0)
       new_segment.shape("square")
       new_segment.penup()
       new_segment.color("grey")
       segments.append(new_segment)
       score=score+1
       delay-=0.01
       if score > high_score:
           high_score = score
    pen.clear()
    pen.write("SCORE :{} HIGH SCORE :{}".format(score, high_score), align="center",
                 font=("courier", 24, "normal"))

    for index in range(len(segments)-1,0,-1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move()
    for segmen in segments:
        if segmen.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            delay=0.2
            for segmen in segments:
                segmen.goto(1000, 1000)
            segments.clear()
            score=0

    time.sleep(delay)












wn.mainloop()
