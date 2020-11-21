#SpiralMyName.py-prints a colorful spiral of the user's name
                         # Set up turtle graphics

import turtle
t=turtle.Pen()
t.speed (0)
turtle.bgcolor("black")
colors= [ "orange" , "yellow" , "blue" , "red" ]

#Ask the user's name using turtle's textinput pop-p window
your_name = turtle.textinput ("Enter your name","What is your name?")

#Draw a spiral of the name on the screen, written 100 times
for x in range (100):
    t.pencolor( colors[x % 4] )
    t.penup()
    t.forward(x * 4 )
    t.pendown()
    t.write (your_name, font = ("Arial", int( (x + 4) / 4), "bold") )
    t.left(92)
