from turtle import *

def spiraal(külg):
    if külg!=0:
        forward(külg)
        right(90)
        forward(külg)
        right(90)
        spiraal(külg-5)
    else:
        forward(0)

spiraal(100)