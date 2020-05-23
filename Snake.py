import turtle

wn = turtle.Screen()
wn.title("SNAKE")
wn.bgcolor("black")
wn.setup(width=500, height=500)
wn.tracer(0)


#Set up snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("white")

snake.penup()
snake.goto(250, 250)
snake.direction = "up"
snake.showturtle()
snake.pendown()
#add win conditions later

def move():
    x = snake.xcor()
    y = snake.ycor()
    if snake.direction == "up":
        snake.sety(y + 10)
    # elif snake.direction == "left":
    #     snake.xcor = x - 10
    # elif snake.direction == "right":
    #     snake.xcor = x + 10
    # elif snake.direction == "down":
    #     snake.ycor = y - 10

while True:
    wn.update()
    move()

wn.mainloop()