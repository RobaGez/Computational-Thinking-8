import turtle
t = turtle.Turtle()
# Where I made the points
t.penup()
t.goto(-70, 0)
t.pendown()
# this is where I added my color feedback
colors = ["pink","blue","red"]
for i in range(900):
    t.color( colors[ i % 3])
# this is where I made my shape
    t.forward(100)
    t.left(72)
    t.forward(20)
    t.left(44)

turtle.exitonclick()

