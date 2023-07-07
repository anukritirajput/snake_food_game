import time
from turtle import Screen
from snake import Snake
from food import Food
from Scoreborard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
Scoreboard = ScoreBoard()
snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food of thw snake
    # distance function to return the distance between two turtles
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        Scoreboard.inc_score()
    #detect collision with wall
    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:

        Scoreboard.reset()
        snake.reset()

#detect collision with tail
#if the segemnt[0] collide with any part of the snake then game over

    for segment in snake.segments:
        if segment==snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<10:

            Scoreboard.reset()
            snake.reset()


screen.exitonclick()
