import turtle
t=turtle.Pen()
turtle.bgcolor('black')
t.speed(0)
colors = ["green","orange","blue","red","yellow"]
for x in range(100):
    t.pencolor(colors[ x%5] )
    t.circle(x)
    t.left(78)

                       
            
    
