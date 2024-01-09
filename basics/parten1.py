from turtle import *
pensize(6)
pencolor("black")
speed(0)
for i in range(6):
    fd(100)
    lt(360/6)
    circle(60)
    write(i+1)
    for j in range(6):
        fd(60)
        lt(360/6)
hideturtle()
mainloop()