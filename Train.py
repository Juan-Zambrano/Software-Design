
#File: Train.py

#  Description:

#  Student Name:Juan Zambrano

#  Student UT EID: jez346

#  Course Name: CS 313E

#  Unique Number: 51335

#  Date Created:

#  Date Last Modified:
import turtle
import math

def line_func(ttl,x,y,x2,y2):
	ttl.penup()
	ttl.goto(x,y)
	ttl.pendown()
	ttl.goto(x2,y2)
	ttl.penup()

def rectangle(ttl,x,y,w,h,color):
	ttl.penup()
	ttl.goto(x,y)
	ttl.color(color)
	ttl.setheading(0)
	ttl.pendown()
	ttl.forward(w)
	ttl.right(90)
	ttl.forward(h)
	ttl.right(90)
	ttl.forward(w)
	ttl.right(90)
	ttl.forward(h)
	ttl.penup()

def window(ttl,x,y,w,h,color):
	ttl.penup()
	ttl.goto(x,y)
	ttl.color(color)
	ttl.setheading(0)
	ttl.pendown()
	ttl.fillcolor('grey')
	ttl.forward(w)
	ttl.right(90)
	ttl.forward(h)
	ttl.right(90)
	ttl.forward(w)
	ttl.right(90)
	ttl.forward(h)
	ttl.end_fill()
	ttl.penup()
	
def trapezoid(ttl,x ,y ,top,side1,bot,side2):
	ttl.penup()
	ttl.goto(x,y)
	ttl.color('blue')
	ttl.pendown()
	ttl.setheading(0)
	ttl.forward(top)
	ttl.right(60)
	ttl.forward(side1)
	ttl.right(120)
	ttl.forward(bot)
	ttl.right(120)
	ttl.forward(side2)
	ttl.penup()
	

def cone(ttl,x,y,top,side1,bot,side2):
	ttl.penup()
	ttl.goto(x,y)
	ttl.color('blue')
	ttl.pendown()
	ttl.setheading(0)
	ttl.forward(top)
	ttl.right(120)
	ttl.forward(side1)
	ttl.right(60)
	ttl.forward(bot)
	ttl.right(60)
	ttl.forward(side2)
	ttl.right(120)
	ttl.goto(x,y)
	ttl.penup()

def halfPentagon(ttl,x,y,top,side1,bot):
	ttl.penup()
	ttl.goto(x,y)
	ttl.color('blue')
	ttl.pendown()
	ttl.setheading(0)
	ttl.forward(top)
	ttl.right(60)
	ttl.forward(side1)
	ttl.right(120)
	ttl.forward(bot)
	ttl.right(90)
	ttl.goto(x,y)
	ttl.penup()

	

def draw_wheels(ttl, x, y, larger_r, smaller_r):
	inside_circle = turtle.Turtle()
	inside_circle.pensize(2)
	
	inside_circle.penup()
	inside_circle.goto(x, y + larger_r - smaller_r)

	inside_circle.color('red')
	ttl.color('red')
	ttl.pensize(2)

	
	ttl.penup()
	ttl.setheading(0)
	
	ttl.goto(x, y)
	ttl.pendown()
	ttl.circle(larger_r)
	ttl.penup()


	spoke_angle = 5
	for r in range(2):
		for q in range(9):
			inside_circle.goto(x, y + larger_r - smaller_r)
			inside_circle.pendown()
			inside_circle.circle(smaller_r, q * 45)
			ttl.goto(x, y + smaller_r)
			ttl.pendown()
			ttl.circle(larger_r - smaller_r, spoke_angle)
			ttl.goto(inside_circle.position())
			inside_circle.penup()
			ttl.penup()
			spoke_angle += 45
			inside_circle.setheading(0)
			ttl.setheading(0)
		spoke_angle = -5

	inside_circle.ht()
	ttl.ht()

def bottomTrain(ttl,x0,y0,x1,y1,radius,x2,y2,x3,y3):
	ttl.penup()
	ttl.color('blue')
	ttl.pendown()
	ttl.setheading(0)
	ttl.goto(x0,y0)
	ttl.goto(x1,y1)
	ttl.circle(-radius,180)
	ttl.goto(x2,y2)
	ttl.circle(-radius,180)
	ttl.goto(x3,y3)
	ttl.circle(-radius,180)
	ttl.goto(x3+30,y3+30)
	ttl.pendown()

def dots_side(ttl,x,y,number):
	ttl.penup()
	ttl.goto(x,y)
	ttl.setheading(0)
	ttl.color('black', 'black')
	for i in range (number):
		ttl.forward(20)
		ttl.pendown()
		ttl.begin_fill()
		ttl.circle(3)
		ttl.end_fill()
		ttl.penup()

def dots_top(ttl,x,y,number):
	ttl.penup()
	ttl.goto(x,y)
	ttl.setheading(270)
	ttl.color('black', 'black')
	for i in range (number):
		ttl.forward(15)
		ttl.pendown()
		ttl.begin_fill()
		ttl.circle(3)
		ttl.end_fill()
		ttl.penup()
  

def drawPolygon(ttl, x, y, num_side, radius):
	sideLen = 2 * radius * math.sin (math.pi / num_side)
	angle = 360 /num_side
	ttl.penup()
	ttl.color('blue')
	ttl.goto (x, y)
	ttl.pendown()
	for iter in range (num_side//2):
		ttl.forward (sideLen)
		ttl.left (angle)  


def main():
	ttl = turtle.Turtle()
	turtle.setup(800,800,0,0)
	ttl.speed(0)
	#line_func(ttl,0,0,20,40)
	window(ttl,-290,225,30,30,'blue')
	window(ttl,-250,225,30,30,'blue')
	#trapezoid(ttl,x,y,top,side1,bot,side2)
	trapezoid(ttl,130,380,60,40,100,40)

	#cone(ttl,x,y,top,side1,bot,side2)
	cone(ttl,180,340,40,100,30,100)

	#halfPentagon(ttl,x,y,top,side1,bot)
	halfPentagon(ttl,250,0,70,100,120)

	#draw_wheels(ttl, x, y, larger_r, smaller_r)
	
	draw_wheels(ttl, -200, -100, 50, 8)
	draw_wheels(ttl, 0, -95, 40, 6)
	draw_wheels(ttl, 200, -95, 40, 6)

	#bottomTrain(ttl,x0,y0,x1,y1,radius,x2,y2,x3,y3)
	
	#rectangle(ttl,x,y,w,h,color)
	rectangle(ttl,-300,300,200,300,'blue')
	rectangle(ttl,-100,200,350,200,'blue')
	rectangle(ttl,-100,120,350,20,'blue')
	rectangle(ttl,-100,250,100,50,'blue')
	rectangle(ttl,-20,250,160,50,'blue')
	rectangle(ttl,160,250,90,50,'blue')

	#dots(ttl,x,y,number)
	dots_side(ttl,-97,110,17)
	dots_top(ttl,-15,250,9)
	dots_top(ttl,144,250,9)


	turtle.done()
	
main()

