import turtle as t
import random

#SCREEN SETUP AND MANAGEMENT
screen = t.Screen()
screen.setup(500,400)

user_bet = screen.textinput(title="MAKE YOUR BET!", prompt="Which turtle will win the race?(Red/Blue/Orange/Purple/Black)")

race_is_on = False

#TURTLE MANAGEMENT


mike = t.Turtle(shape="turtle")
mike.color("orange")
mike.penup()
mike.goto(-200,50)

leo = t.Turtle(shape="turtle")
leo.color("blue")
leo.penup()
leo.goto(-200,25)

raph = t.Turtle(shape="turtle")
raph.color("red")
raph.penup()
raph.goto(-200,0)

donnie = t.Turtle(shape="turtle")
donnie.color("purple")
donnie.penup()
donnie.goto(-200,-25)

splinter = t.Turtle(shape="turtle")
splinter.color("black")
splinter.penup()
splinter.goto(-200,-50)

if user_bet:
    race_is_on = True
while race_is_on:
    mike.forward(random.randint(0,10))
    if mike.xcor() >230:
        race_is_on = False
        print("Orange won the race")
        if user_bet == "Orange":
            print("You win! Orange is the winner")
        else:
            print("You lose")
    leo.forward(random.randint(0,10))
    if leo.xcor() > 230:
        race_is_on = False
        print("Blue won the race")
        if user_bet == "Blue":
            print("You win! Bluee is the winner")
        else:
            print("You lose")

    raph.forward(random.randint(0,10))
    if raph.xcor() > 230:
        race_is_on = False
        print("Red won the race")
        if user_bet == "Red":
            print("You win! Red is the winner")
        else:
            print("You lose")

    donnie.forward(random.randint(0,10))
    if donnie.xcor() > 230:
        race_is_on = False
        print("Purple won the race")
        if user_bet == "Purple":
            print("You win! Purple is the winner")
        else:
            print("You lose")

    splinter.forward(random.randint(0,10))
    if splinter.xcor() > 230:
        race_is_on = False
        print("Black won the race")
        if user_bet == "Black":
            print("You win! Black is the winner")
        else:
            print("You lose")








screen.exitonclick()