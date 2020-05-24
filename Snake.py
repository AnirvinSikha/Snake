import turtle
import time
import random
import sys

#Set up window
wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width=1000, height=700)
wn.tracer(0)

width, height = turtle.window_width(), turtle.window_height()
minX, maxX = -width/2, width/2
minY, maxY = -height/2, height/2


#Set up snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("yellow")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"
snake.showturtle()

#Set up food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()


#food spawn function, spawns in a random place in the map.
def spawn_food():
    food_x = random.randint(minX, maxX)
    food_y = random.randint(minY, maxY)
    while(food_x != snake.xcor() and food_y != snake.ycor()):
        food_x = random.randint(minX, maxX)
        food_y = random.randint(minY, maxY)
    food.goto(food_x, food_y)

spawn_food()
#Set up body, add body parts when eating a food
body = []

#direction moves, then bind these functions to the actual keys
# then apply the position changes from the moves
def up():
    snake.direction = "up"
def down():
    snake.direction = "down"
def left():
    snake.direction = "left"
def right():
    snake.direction = "right"

def move():
    x = snake.xcor()
    y = snake.ycor()
    factor = 10
    if snake.direction == "up":
        snake.sety(y + factor)
    elif snake.direction == "left":
        snake.setx(x - factor)
    elif snake.direction == "right":
        snake.setx(x + factor)
    elif snake.direction == "down":
        snake.sety(y - factor)

while True:
    wn.update()
    move()
    time.sleep(.02)
    wn.listen()
    wn.onkeypress(up, "Up")
    wn.onkeypress(down, "Down")
    wn.onkeypress(right, "Right")
    wn.onkeypress(left, "Left")
    if(snake.distance(food) < 20):
        spawn_food()
        seg = turtle.Turtle()
        seg.penup()
        x = snake.xcor()
        y = snake.ycor()
        seg.goto(x, y)
        seg.shape("square")
        seg.color("white")
        body.append(seg)

    for seg in body:
        x = seg.xcor()
        y = seg.ycor()
        factor = 10
        if snake.direction == "up":
            seg.sety(y + factor)
        elif snake.direction == "down":
            seg.sety(y - factor)
        elif snake.direction == "left":
            seg.setx(x - factor)
        elif snake.direction == "right":
            seg.setx(x + factor)

    #Wall loss condition
    if not minX <= snake.xcor() <= maxX or not minY <= snake.ycor() <= maxY:
        end_text = turtle.Turtle()
        end_text.goto(0,0)
        end_text.color("white")
        end_text.write("You hit the wall!", font=("Arial", 24, 'normal'))
        break




wn.mainloop()