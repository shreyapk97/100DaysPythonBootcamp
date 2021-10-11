from turtle import Turtle, Screen, exitonclick

timmy_the_turtle=Turtle()
#screen=Screen()
#screen.exitonclick()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
for _ in range(4):
    timmy_the_turtle.forward(100)
    #timmy_the_turtle.done()
    timmy_the_turtle.right(90) #90 degrees
#timmy_the_turtle.forward(100) #100 m forward
exitonclick()