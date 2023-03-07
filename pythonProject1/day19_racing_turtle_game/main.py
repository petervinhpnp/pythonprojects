from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=700, height=600)
user_guess = screen.textinput(title="Make your bet", prompt="Which turtle do you think will win the race:")
is_race_on = False
colors = ["red", "blue", "green", "orange", "purple", "yellow"]
y_coordinate = [-50, -10, 30, 70,  110, 150]
all_turtle = []
for turtle_num in range(0, 6):
    turtle_new = Turtle(shape='turtle')
    turtle_new.color(colors[turtle_num])
    turtle_new.penup()
    turtle_new.goto(x=-330, y=y_coordinate[turtle_num])
    all_turtle.append(turtle_new)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 300:
            is_race_on = False
            if user_guess == turtle.color()[0]:
                print(f"Nice job! You won the bet. The winner turtle is {turtle.color()[0]} turtle.")
            else:
                print(f"You lost! The winner turtle is {turtle.color()[0]} turtle.")
        distance = random.randint(0, 30)
        turtle.forward(distance)

screen.exitonclick()