import turtle
import winsound

wn=turtle.Screen()
wn.bgpic('background.png')
wn.setup(width=800,height=600)

####paddle a######
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto((-350,0))
#########paddle_b#####
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto((350,0))
######ball#########
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")

ball.penup()
ball.dx=6
ball.dy=-6
ball.goto((0,0))
def paddle_a_up():
    y=paddle_a.ycor()
    y=y+30
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y=y-30
    paddle_a.sety(y)
def paddle_b_up():
    y=paddle_b.ycor()
    y=y+30
    paddle_b.sety(y)
def paddle_b_down():
    y=paddle_b.ycor()
    y=y-30
    paddle_b.sety(y)
##########score#######3
score_a=0
score_b=0
####pen######
pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.color("white")
pen.goto(0,260)
pen.write("score a :0 score b:0 ",align="center",font=("Courier",20,"normal"))










wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')






while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy*=-1
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy*=-1
    if ball.xcor()>390:
        ball.goto((0,0))
        ball.dx*=-1
        pen.clear()
        score_a+=1
        pen.write("score a :{} score b:{} ".format(score_a,score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor()<-390:
        ball.goto((0,0))
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("score a :{} score b:{} ".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    if ball.xcor()>340 and(ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx*=-1
    if ball.xcor()<-340 and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx*=-1
    ########paddle boumdaries
    if paddle_a.ycor()+50 >300:
        paddle_a.sety(250)
    if paddle_a.ycor()-50 <-300:
        paddle_a.sety(-250)
    if paddle_b.ycor()+50 >300:
        paddle_b.sety(250)
    if paddle_b.ycor()-50 <-300:
        paddle_b.sety(-250)


