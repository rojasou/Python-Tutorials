#import the turtle package
import turtle

turtle.bgcolor("black") #background color
turtle.pensize("2") # size of pen
turtle.color("green") # color of drawing
turtle.speed(0) # changes the speed it draws

# draw a square
#turtle.forward(50) # moves forward
#turtle.left(90) # moves 90 degrees left
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.forward(50)
#turtle.left(90)
#turtle.backward(50) # moves backwards
#turtle.done() # allows turtle to stay on screen

# make a sun shape
#from turtle import *
#color('yellow', 'orange')
#begin_fill()
#while True:
#    forward(200)
#      left(170)
#    if abs(pos()) < 1:
#        break
#end_fill()
#done()

# make a rainbow of circles
#for colors in ["red","orange","yellow","green","blue","purple"]:
#    turtle.color(colors)
#    turtle.circle(150)
#    turtle.left(10)
#turtle.done()

# make it better
for i in range(12):
    for colors in ["red", "orange", "yellow", "green", "blue", "purple"]:
        turtle.color(colors)
        turtle.circle(150)
        turtle.left(5)
turtle.done()
