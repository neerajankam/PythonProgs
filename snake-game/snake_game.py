#Import the necessary python modules
import turtle
import time
import random

delay = 0.05
#Variables to keep track of the game score
score = 0
high_score = 0

#Creating the screen object and setting the properties of the screen
scr = turtle.Screen()
scr.title("Snake Game by Neeraj Ankam")
scr.bgcolor("green")
scr.setup(width = 600,height= 600)
scr.tracer(0) #Turns off the screen updates

#Empty list used to denote the segments of the snake body(attached to the head as the snake consumes food)
segments = []

#Creating the snake head and setting its properties
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup() #penup does not leave traces on the screen when the snake is moving
head.goto(0,0)
head.direction = "stop"

#Creating the snake food and setting its properties

food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(100,10)

#Creating the Pen object and its settings to write the score and update the high score on the screen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High score: 0",align="center", font=("Courier", 24, "normal"))


#Functions to define the movement of the snake

def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx( x + 20)

#Keyboard bindings to make sure the program is listening to the pressed keys and is taking appropriate actions

scr.listen()
scr.onkeypress(go_up,"i")
scr.onkeypress(go_down,"k")
scr.onkeypress(go_left,"j")
scr.onkeypress(go_right,"l")

#Main game loop
while True:
    scr.update()

    #Check for border collisions
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        #Sending the segments off screen and clearing them off screen
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        #Setting the score to zero upon collision and updating the scores appropriately
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align = "center", font = ("Courier",24,"normal"))

    # Move the food to a random spot

    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.color("gray")
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)

        #Increase the score on consuming the food
        score += 10

        if score > high_score:
            high_score = score
        #Updating the score on eating the food
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score,high_score),align= "center", font = ("Courier",24,"normal"))

    #Move the end segments first in reverse order

    for index in range(len(segments)-1,0,-1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    #Check for head collision with body segments
    for segment in segments:
        if segment.distance(head) < 20 :
            time.sleep(1)
            score = 0
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000,1000)

            segments.clear()

            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align="center",font=("Courier", 24, "normal"))



    time.sleep(delay)

scr.mainloop()
