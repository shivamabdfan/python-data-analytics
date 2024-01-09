from turtle import*
speed(0)
def pentagon(size,color):
    fillcolor(color)
    begin_fill()
    for i in range(5):
        fd(size)
        lt(360/5)
    end_fill()
for i in  range(6):
    pentagon(100,"red")
    pentagon(75,"green")
    pentagon(50, "blue")
    lt(360/6)
hideturtle()
mainloop()
