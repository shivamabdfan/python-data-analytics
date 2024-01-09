from turtle import *
def pentagon(side_length):
    for i in range(5):
        forward(side_length)
        right(72)
speed(2)
pentagon(100)
mainloop()
