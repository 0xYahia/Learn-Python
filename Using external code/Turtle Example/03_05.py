from turtle import *
import random;
colors= ['red','green', 'blue', 'priple', 'black']
color(colors[random.randint(0,4)], colors[random.randint(0,4)])
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


#  import turtle

# t = turtle.Turtle()

# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# turtle.done()