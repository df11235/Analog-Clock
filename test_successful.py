import time
import turtle

sc= turtle.Screen()
sc.bgcolor("black")
sc.setup(width=500, height=400)
sc.title("Analog Clock")
sc.tracer(0)
#pen for secondhand
pens=turtle.Turtle()
pens.hideturtle()
pens.speed(0)
pens.pensize(5)
#pen for minutehand
penm=turtle.Turtle()
penm.hideturtle()
penm.speed(0)
penm.pensize(5)
#pen for hourhand
penh=turtle.Turtle()
penh.hideturtle()
penh.speed(0)
penh.pensize(5)
def secondhand(secs,pens):
    #seconds
    pens.penup()
    pens.goto(0,130)
    pens.setheading(360)
    pens.pencolor("white")
    a=(secs/60)*360
    pens.pendown()
    pens.circle(-130,a)
    if (secs==60):
        pens.clear()
        

def minutehand(mins,pens):
    #mins
    penm.penup()
    penm.goto(0,100)
    penm.setheading(360)
    penm.color("pink")
    a=(mins/60)*360
    penm.pendown()
    penm.circle(-100,a)
    if (mins==60):
        penm.clear()


def hourhand(hours,penh):
    #hours
    penh.penup()
    penh.goto(0,70)
    penh.setheading(360)
    penh.color("coral")
    a=(hours/12)*360
    penh.pendown()
    penh.circle(-70,a)
    if (hours==12):
        penh.clear()

while True:
    hours=int(time.strftime("%I"))
    mins=int(time.strftime("%M"))
    sec=int(time.strftime("%S"))
    secondhand(sec,pens)
    minutehand(mins,penm)
    hourhand(hours,penh)
    sc.update()
    pens.clear()  

sc.mainloop()