import turtle
import random
from math import sqrt

def domek(a):
    b = sqrt((a**2) * 2)
    c = b / 2
    
    turtle.backward(a)
    turtle.right(90)
    turtle.backward(a)
    turtle.right(90)
    turtle.backward(a)
    turtle.right(90)
    turtle.backward(a)

    turtle.right(135)
    turtle.backward(b)
    turtle.right(90)
    turtle.backward(c)
    turtle.right(90)
    turtle.backward(c)
    turtle.right(90)
    turtle.backward(b)
    turtle.right(45)

def mesto(velikost):
    a = 0
    while(velikost > a):
        domek(random.randint(25, 250))
        a = a + 1

turtle.penup()
turtle.goto(500, 0)
turtle.pendown()

mesto(random.randint(5, 50))

turtle.exitonclick()
