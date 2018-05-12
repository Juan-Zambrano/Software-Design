#  File: Art.py

#  Description: The type of art you get tatooed.

#  Student Name: Juan Zambrano

#  Student UT EID: jez346

#  Course Name: CS 313E

#  Unique Number:51335 

#  Date Created: March,2,2018

#  Date Last Modified: March,2,2018
import os
import turtle

# draw field recursively
def draw_field (ttl,order):
  if(order > 0):
    for i in range(order + 1):
      ttl.circle(order*40,steps = 3)
      ttl.left(60)
    if (order >= 4):
      ttl.color('purple')
      ttl.setheading(0)
      ttl.circle(40,steps = 4)
      ttl.circle(60,steps = 4)
      ttl.circle(64,steps = 4)
      ttl.circle(150,steps = 4)
      draw_field (ttl, order - 1)
    elif(order >= 3):
      ttl.penup()
      ttl.setheading(180)
      ttl.goto(0,-100)
      ttl.color('red')
      ttl.pendown()
      ttl.circle(40,steps = 4)
      ttl.circle(60,steps = 4)
      ttl.circle(64,steps = 4)
      ttl.circle(150,steps = 4)
      draw_field(ttl,order - 1)
    elif(order >= 2):
      ttl.penup()
      ttl.setheading(270)
      ttl.goto(0,-100)
      ttl.color('green')
      ttl.pendown()
      ttl.circle(40,steps = 4)
      ttl.circle(60,steps = 4)
      ttl.circle(64,steps = 4)
      ttl.circle(150,steps = 4)
      draw_field(ttl,order - 1)
    elif(order >= 1):
      ttl.penup()
      ttl.setheading(90)
      ttl.goto(0,-100)
      ttl.color('blue')
      ttl.pendown()
      ttl.circle(40,steps = 4)
      ttl.circle(60,steps = 4)
      ttl.circle(64,steps = 4)
      ttl.circle(150,steps = 4)
      draw_field(ttl,order - 1)

def main():
  turtle.tracer(10000)
  order = int(input ('Enter a level of recursion between 1 and 6: '))
  # put label on top of page
  turtle.title ('Recursive Art')
  # setup screen size
  turtle.bgcolor('lime')
  turtle.setup (800, 800, 0, 0)
  # create a turtle object
  ttl = turtle.Turtle()
  ttl.penup()
  ttl.goto(0,-100)
  ttl.pendown()
  draw_field (ttl, order)
  outName = os.path.basename(__file__)[:-2]+'eps'
  turtScrn = turtle.getscreen()
  turtScrn.getcanvas().postscript(file=outName)
main()






