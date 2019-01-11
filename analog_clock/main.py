#Import the necessary modules
import turtle
import time

#Setup the background screen and its properties
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Analog clock by Neeraj")
wn.setup(height = wn.window_height(), width = wn.window_width())
wn.tracer(0)

#Make a turtle object named pen. Set its width and speed
pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.width(5)
pen.penup()

#Function used to take the current time and draw it using the pen object configured above
def drawclock(h,m,s,pen):
    pen.setheading(180)
    pen.color("gold")
    pen.goto(0, 210)
    pen.pendown()
    pen.circle(210)
    pen.penup()
    pen.goto(0,0)
    # Draw the twelve divisions on the clock each one denoting an hour
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)

    #Draw the hour hand and set its properties
    pen.penup()
    pen.goto(0,0)
    pen.color("white")
    pen.setheading(90)
    pen.width(7)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(120)

    #Draw the minute hand and set its properties
    pen.penup()
    pen.goto(0,0)
    pen.color("blue")
    pen.setheading(90)
    angle = (m/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(170)

    #Draw the second hand and set its properties
    pen.penup()
    pen.goto(0,0)
    pen.color("green")
    pen.setheading(90)
    angle = (s/60) * 360
    pen.rt(angle)
    pen.pendown()
    pen.fd(180)
    pen.penup()

#Infinite loop which updates the time constantly and only the updated drawing is shown on the screen(once every second)
while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%H"))
    s = int(time.strftime("%S"))
    drawclock(h,m,s,pen)
    wn.update()
    # time.sleep(1)
    pen.clear()

#This calls the underlying tkinter's main loop used for graphics
wn.mainloop()