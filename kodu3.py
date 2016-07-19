from turtle import *

def lihtsamfraktal(tase, pikkus):
    if tase == 1:
        forward(pikkus)
        left(85)
        forward(pikkus)
        right(170)
        forward(pikkus)
        left(85)
        forward(pikkus)
    else:
        lihtsamfraktal(tase-1, pikkus*0.7)
        left(85)
        lihtsamfraktal(tase-1, pikkus*0.7)
        right(170)
        lihtsamfraktal(tase-1, pikkus*0.7)
        left(85)
        lihtsamfraktal(tase-1, pikkus*0.7)

def fraktal(tase, pikkus):
    for i in range(0,4):
        lihtsamfraktal(tase,pikkus)
        left(90)
        
fraktal(3,40)