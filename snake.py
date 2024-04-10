import turtle
import random
import time

# Screen and game settings
WIDTH = 600
HEIGHT = 600
DELAY = 0.1

# Colors
BG_COLOR = "green"
FOOD_COLOR = "red"
SNAKE_HEAD_COLOR = "black"
SNAKE_BODY_COLOR = "grey"
FONT_COLOR = "white"

# Score
score = 0
high_score = 0

# Screen setup
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor(BG_COLOR)
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)  # Turn off screen updates for better performance

# Snake head
head = turtle.Turtle()
head.speed(0)  # Set animation speed to fastest
head.shape("square")
head.color(SNAKE_HEAD_COLOR)
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color(FOOD_COLOR)
food.penup()
random_x = random.randint(-WIDTH // 2 + 20, WIDTH // 2 - 20)
random_y = random.randint(-HEIGHT // 2 + 20, HEIGHT // 2 - 20)
food.goto(random_x, random_y)

# Snake body segments (initially empty)
segments = []

# Pen for score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color(FONT_COLOR)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}  High Score: {high_score}", align="center",
           font=("Courier", 24, "normal"))


# Function to move the snake based on its direction
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# Function to change direction (prevents going back on itself)
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


# Keyboard bindings for direction changes
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main game loop
while True:
    screen.update()

    # Check for border collision
    if head.xcor() > WIDTH // 2 - 20 or head.xcor() < -WIDTH // 2 + 20 or \
       head.ycor() > HEIGHT // 2 - 20 or head.ycor() < -HEIGHT // 2 + 20:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear segments
        segments.clear()

        # Reset score and delay
        score = 0
        DELAY = 0.1

        pen.clear()
        pen.write(f"Score: {score}  High Score: {high_score}", align="center",
                  font=("Courier", 24, "normal"))

    # Check for food collision
