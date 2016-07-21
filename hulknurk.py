from turtle import *

n=int(input("Mitu külge on hulknurgal? "))
a=int(input('Kui pikk on külg? '))
joonistatud_kylgi = 0

while joonistatud_kylgi < n:
    forward(a)
    left(360/n)
    joonistatud_kylgi += 1 

exitonclick()