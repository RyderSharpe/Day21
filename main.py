# TODO 1: Create snake body-DONE
# TODO 2: Move the snake-DONE
# TODO 3: Control the snake-DONE

# TODO 4: Detect collision with food- DONE
# TODO 5: Create a scoreboard - DONE
# TODO 6: Detect collision with wall
# TODO 7: Detect collision with tail

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

game_is_on = True  # Declare game_is_on as global

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_speed = 0.1


while game_is_on:
    # Update the screen every 0.1 seconds.
    screen.update()
    time.sleep(game_speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 30:
        food.refresh()
        snake.extend()
        score.clear_score()
        score.update_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_is_on = False

    # Detect collision with any segment in tail.
    for segment in snake.segments[1:]: # [1:] is a 'slicing' technique.
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False
        ## Other code ##
        # if segment == snake.head:
        #     pass
        # elif snake.head.distance(segment) < 10:
        #     score.game_over()
        #     game_is_on = False








screen.exitonclick()