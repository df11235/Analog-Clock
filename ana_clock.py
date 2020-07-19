import time
import turtle

sc= turtle.Screen()
sc.bgcolor("black")
sc.setup(width=500, height=400)
sc.title("Analog Clock")
sc.tracer(0)

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
def clock(hours,mins,secs,pen):
    pen.up()
    pen.goto(0,150)
    pen.setheading(180)
    pen.color("white")
    pen.pendown()
    pen.circle(150)
    pen.penup()
    pen.goto(0,0)
    i=1
    for i in range(12):
        pen.fd(130)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)
        i=i+1
    pen.penup()
    pen.goto(0,0)
    pen.color("cyan")
    pen.setheading(90)
    a=(hours/12)*360
    pen.rt(a)
    pen.pendown()
    pen.fd(60)
    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    a=(mins/60)*360
    pen.rt(a)
    pen.pendown()
    pen.fd(90)
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    a=(secs/60)*360
    pen.rt(a)
    pen.pendown()
    pen.fd(120)
while True:
    hours=int(time.strftime("%I"))
    mins=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))
    clock(hours,mins,sec,pen)
    sc.update()
    pen.clear()  

sc.mainloop()