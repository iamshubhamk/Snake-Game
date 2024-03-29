from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
MOVE_SPEED = 0.1

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(MOVE_SPEED)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        MOVE_SPEED = MOVE_SPEED*0.9
        scoreboard.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        MOVE_SPEED = 0.1
            
    
    for segment in snake.segments:
        if segment != snake.head:
            if snake.head.distance(segment)<10:
                scoreboard.reset()
                snake.reset()


screen.exitonclick()