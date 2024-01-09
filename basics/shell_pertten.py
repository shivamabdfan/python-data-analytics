from turtle import*
pencolor("green")
pensize(3)
fillcolor("red")
begin_fill()
speed("fastest")
for i in range(10,0,-1):
    begin_fill()
    circle(i*10)
    lt(20)
    end_fill
mainloop()