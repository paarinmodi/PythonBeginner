import turtle
t=turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 5
colors = ["blue","red","yellow","orange","green",
          "violet","red","pink","grey","light blue",
          "light yellow","light green"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 95)
    t.width(x*sides/200)
 
