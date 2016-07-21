from turtle import *

nurk = 60
kordaja = 0.45

def frak(tase, pikkus):
    if tase > 0:
        forward(pikkus)
        left(nurk)
        frak(tase-1, pikkus * kordaja)
        right(nurk)
        frak(tase-2, pikkus * kordaja)
        right(nurk)
        frak(tase-1, pikkus * kordaja)
        left(nurk)
        backward(pikkus)


speed(10)
delay(0)


left(90)
frak(5, 100)