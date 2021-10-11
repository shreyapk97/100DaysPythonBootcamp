import turtle as t
import random
directions=[0,90,180,270,360]
tim=t.Turtle()
for _ in range(100):
    tim.forward(10)
    tim.setheading(random.choice(directions))
