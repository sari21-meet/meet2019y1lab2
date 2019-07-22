import turtle # imports the turtle library

yp7 = turtle.clone() #this creates a new turtle and stores it in a variable
t = 200
b = -200

#draw the letter ‘A’

turtle.hideturtle() # this hides the arrow of the turtle called turtle


yp7.pendown()


yp7.goto(-1000,0)


yp7.penup()

a,c = yp7.pos()

yp7.goto(a,c)

yp7.pendown()
yp7.goto(a+100, c+300)
yp7.goto(a+200, c)
yp7.goto(a+30, c+100)


yp7.goto(a+300, c+100)

turtle.mainloop() 
