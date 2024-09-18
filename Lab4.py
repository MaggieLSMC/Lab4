#the authors' names are Maggie and Lily

#L41

##import turtle
##jack = turtle.Turtle()
##jack.color("yellow")
##
##for side in range(4):
##    if side == 3:
##        jack.color("blue")
##    jack.forward(100)
##    jack.right(90)
##
##import turtle
##jack = turtle.Turtle()
##jack.color("yellow")
##
##for side in range(4):
##    jack.forward(100)
##    jack.right(90)
##    if side == 3:
##        jack.color("blue")
##
##import turtle
##jack = turtle.Turtle()
##jack.color("yellow")
##
##for side in range(4):
##    if side == 2:
##        jack.color("blue")
##    jack.forward(100)
##    jack.right(90)
##
##
##L42

##import turtle
##jack = turtle.Turtle()
##jack.color("yellow")
##
##for side in range(4):
##        if side == 1:
##           jack.color("blue")
##        if side == 2:
##           jack.color("purple")
##        if side == 3:
##           jack.color("brown")
##        jack.forward(100)
##        jack.right(90)


#L43

##import turtle
##
##romeo = turtle.Turtle()
##juliet = turtle.Turtle()
##
##juliet.color("misty rose")
##juliet.width(3)
##
##romeo.color("violet")
##romeo.width(3)
##
##romeo_last_name = "montague"
##
##romeo.left(40)
##romeo.forward(100)
##for side in range(185):
##    romeo.forward(1)
##    romeo.left(1)
##romeo.hideturtle()
##
##if romeo_last_name == "montague":
##    juliet.left(140)
##    juliet.forward(100)
##    for side in range(185):
##        juliet.forward(1)
##        juliet.right(1)
##juliet.hideturtle()

#L44

sequence = ["paper", "rock", "paper", "scissor", "rock", "rock", "scissor", "paper"]
for x in sequence:
    if x == "scissor":
        print("scissor beats paper")
    if x == "paper":
        print("paper eats rock")
    if x == "rock":
        print("rock hits scissor")



