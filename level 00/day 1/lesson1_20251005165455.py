from turtle import *

#we want to paint a house

#step 1: draw a square
shape("turtle")
speed(30)
width(7)
color("purple")
begin_fill()

forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing the windows
color("blue")
penup()
goto(120, 120)
pendown()
left(120)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(30)
left(90)
forward(60)

penup()
goto(70, 120)
pendown()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(180)
forward(30)
right(90)
forward(60)

penup()
goto(70, 60)
pendown()
right(90)
forward(20)

#drawing a garden
color("green")
begin_fill()
penup()
goto(0, 0)
pendown()
left(180)
forward(800)
left(90)
forward(800)
left(90)
forward(1600)
left(90)
forward(800)
left(90)
forward(800)
end_fill()

exitonclick()


