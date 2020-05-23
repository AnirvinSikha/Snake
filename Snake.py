import turtle
import time
import random
import sys

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
snake.color("white")

snake.penup()
snake.goto(0, 0)
snake.direction = "stop"
snake.showturtle()

#Set up food
food = turtle.Turtle()
food.shape("square")
food.color("red")
food.penup()

def spawn_food():
    # food_x = random.randint(0 - w/2, w/2)
    # food_y = random.randint(0 - h/2, h/2)
    # while(food_x != snake.xcor() and food_y != snake.ycor()):
    #     food_x = random.randint(0 - w / 2, w / 2)
    #     food_y = random.randint(0 - h / 2, h / 2)

    food_x = random.randint(minX, maxX)
    food_y = random.randint(minY, maxY)
    while(food_x != snake.xcor() and food_y != snake.ycor()):
        food_x = random.randint(minX, maxX)
        food_y = random.randint(minY, maxY)
    food.goto(food_x, food_y)


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

    #Wall loss condition
    if not minX <= snake.xcor() <= maxX or not minY <= snake.ycor() <= maxY:
        end_text = turtle.Turtle()
        end_text.goto(0,0)
        end_text.color("white")
        end_text.write("You hit the wall!", font=("Arial", 24, 'normal'))
        break




wn.mainloop()