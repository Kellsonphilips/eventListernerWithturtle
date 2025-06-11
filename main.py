
from turtle import Turtle, Screen


eventMaster = Turtle()
eventMaster.color("red")
screen = Screen()


def move_forward():
    eventMaster.forward(10)


def move_backward():
    eventMaster.backward(10)


def move_left():
    new_heading = eventMaster.heading() + 10
    eventMaster.setheading(new_heading)


def clear_drawing():
    eventMaster.clear()
    eventMaster.penup()
    eventMaster.home()
    eventMaster.pendown()


def move_right():
    new_heading = eventMaster.heading() - 10
    eventMaster.setheading(new_heading)


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_drawing)


screen.exitonclick()
