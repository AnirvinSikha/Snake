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
xPoints = set()
yPoints = set()
score = 0

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
    while(food_x  in xPoints and food_y in yPoints):
        food_x = random.randint(minX, maxX)
        food_y = random.randint(minY, maxY)
    food.goto(food_x, food_y)
    xPoints.clear()
    yPoints.clear()

spawn_food()
#Set up body, add body parts when eating a food
body = []
body.append(snake)

#direction moves, then bind these functions to the actual keys
# then apply the position changes from the moves
def up():
    if snake.direction is not "down":
        snake.direction = "up"
def down():
    if snake.direction is not "up":
        snake.direction = "down"
def left():
    if snake.direction is not "right":
        snake.direction = "left"
def right():
    if snake.direction is not "left":
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
    #move()
    time.sleep(.02)
    wn.listen()
    wn.onkeypress(up, "Up")
    wn.onkeypress(down, "Down")
    wn.onkeypress(right, "Right")
    wn.onkeypress(left, "Left")

    #eating the food
    if(snake.distance(food) < 20):
        spawn_food()
        score += 1
        seg = turtle.Turtle()
        seg.penup()
        x = snake.xcor()
        y = snake.ycor()
        seg.goto(x, y)
        seg.shape("square")
        seg.color("white")
        body.append(seg)

    #Moving the entire snake along
    store = None
    for i in range(len(body) - 1, -1, -1):
        curr = body[i]
        if (i is not 0):
            prev = body[i - 1]
            x = prev.xcor()
            y = prev.ycor()
            curr.goto(x, y)
            xPoints.add(x)
            yPoints.add(y)
        else:
            move()

    #Wall loss condition
    if not minX <= snake.xcor() <= maxX or not minY <= snake.ycor() <= maxY:
        end_text = turtle.Turtle()
        end_text.goto(0,0)
        end_text.color("white")
        end_text.write("You hit the wall! Score = " + str(score), font=("Arial", 24, 'normal'))
        break

    #body colission loss condition
    head = body[0]
    loss = False
    for seg in body[1:]:
        if head.distance(seg) < 2:
            loss = True
            break
    if loss is True:
        end_text = turtle.Turtle()
        end_text.goto(0, 0)
        end_text.color("white")
        end_text.write("You hit yourself! Score = " + str(score), font=("Arial", 24, 'normal'))
        break

wn.mainloop()