import turtle




screen = turtle.Screen()


screen.setup(800, 800)


screen.bgcolor('Cornflower blue')
t = turtle.Turtle()
t.showturtle()
t2 = turtle.Turtle()
t2.showturtle()
t2.penup()
t3 = turtle.Turtle()
t3.showturtle()
t3.hideturtle()


t.hideturtle()
t2.hideturtle()


t.speed(2000)
t.penup()
t.goto(-50,0)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


t2.penup()
t2.goto(0, 100)
t2.pendown()
t3.penup()
t3.goto(0, 200)
t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 30, "bold"), align="center")
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Zack Miller", font=("arial", 30, "bold"), align="center")
enter = input("press enter to begin")
t.showturtle()
t.clear()


t.penup()
t.goto(0,250)
t.write("My favorite food", font=("arial", 30, "bold"), align="center")

screen.bgcolor("red")

turtle.addshape("crableg.gif")
t.shape("crableg.gif")
t.goto(50,150)
a = t.stamp()
t.goto(70,200)
t.write("Crableg", font=("arial", 30, "bold"), align="center")


turtle.addshape("pizza.gif")
t.shape("pizza.gif")
t.goto(250,150)
b = t.stamp()
t.goto(250,200)
t.write("Pizza", font=("arial", 30, "bold"), align="center")


turtle.addshape("wings.gif")
t.shape("wings.gif")
t.goto(-150,150)
c = t.stamp()
t.goto(0,0)
t.goto(-150,200)
t.write("Wings", font=("arial", 30, "bold"), align="center")

t.goto(0,0)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(50)
t.end_fill()

enter = input("press enter to begin")
t.clear()
t.clearstamps()
t.penup()
t.goto(0,240)
t.write("My favorite hobbies", font=("arial", 30, "bold"), align="center")

screen.bgcolor("green")





turtle.addshape("basketball.gif")
t.shape("basketball.gif")
t.goto(0,50)
a = t.stamp()
t.hideturtle()
t.goto(0,100)
t.write("Basketball", font=("arial", 30, "bold"), align="center")



turtle.addshape("football.gif")
t.shape("football.gif")
t.goto(0,150)
b = t.stamp()
t.goto(0,180)
t.write("Football", font=("arial", 30, "bold"), align="center")

turtle.addshape("swimming.gif")
t.shape("swimming.gif")
t.goto(0,-70)
c = t.stamp()
t.goto(0,0)
t.goto(0,-30)
t.write("Swimming", font=("arial", 30, "bold"), align="center")


turtle.addshape("fishing.gif")
t.shape("fishing.gif")
t.goto(0,-170)
c = t.stamp()
t.goto(0,0)
t.goto(0,-120)
t.write("Fishing", font=("arial", 30, "bold"), align="center")

t.penup()
t.goto(-225,0)
t.pendown()
t.fillcolor("purple")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.end_fill()

enter = input("press enter to begin")
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite movie", font=("arial", 30, "bold"), align="center")





screen.bgcolor("orange")



turtle.addshape("waterboy.gif")
t.shape("waterboy.gif")
t.goto(0,-20)
b = t.stamp()
t.goto(0,40)
t.write("The Waterboy", font=("arial", 30, "bold"), align="center")



turtle.addshape("waterboy2.gif")
t.shape("waterboy2.gif")
t.goto(0,150)
b = t.stamp()

t.goto(0,150)

t.penup()
t.goto(250,0)
t.pendown()
t.fillcolor("cornsilk")
t.begin_fill()
t.setheading(45)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
t.end_fill()

enter = input("press enter to begin")
t.clear()
t.clearstamps()
t.penup()
t.goto(0,200)
t.write("My favorite Sport", font=("arial", 30, "bold"), align="center")



screen.bgcolor("blue")


turtle.addshape("lebron.gif")
t.shape("lebron.gif")
t.goto(0,-20)
b = t.stamp()
t.goto(0,40)
t.write("Basketball", font=("arial", 30, "bold"), align="center")



turtle.addshape("court.gif")
t.shape("court.gif")
t.goto(0,150)
b = t.stamp()
t.goto(0,-150)

t.penup()
t.goto(150,-100)
t.pendown()
t.color("Hot Pink")
t.pencolor("pink")
t.setheading(0)
t.begin_fill()
t.circle(30)
t.end_fill()


turtle.done()








