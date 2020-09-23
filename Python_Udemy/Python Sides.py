import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = eval ( input ("Enter a number of sides between 2 and 6: ") )
colors = ["blue","red","yellow","orange","green",
          "white","violet","pink","grey","light blue",
          "light yellow","light green"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
