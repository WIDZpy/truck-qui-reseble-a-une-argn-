import turtle
from math import *
import random
class programe:
    def __init__(self):
        turtle.screensize(100,100)
        self.color = ['white']
        self.t = turtle
        self.t.delay(1)
        self.t.speed(0)
        self.t.pensize(50)
        self.t.up()
        #self.t.hideturtle()
        self.t.bgcolor('black')
        self.t.color('white')
        self.couches = 30
        #self.nds = 8
        #self.L = 10
    def calcule(self,nds,L):
        V1 = (self.l / 2) / (sin(radians(360 / (nds * 2))))
        return V1
    def poliguon(self,nds,L):
        self.t.right((360 / nds) / 2)
        for loop in range(nds):
            self.t.fd(self.l)
            self.t.right(360 / nds)
    def tre(self,nds,L):

        self.t.color('white')
        self.t.pensize(1)
        self.t.up()
        self.t.setpos(0, 0)
        self.t.down()
        self.t.seth(90)
        for loop in range(nds):
            self.t.setpos(0, 0)
            self.l = (L + (self.l * 10) / nds) * (self.couches)
            self.t.fd(l)
            self.t.right(360 / nds)

    def run(self,nds,L):
        for loop in range(self.couches):
            self.color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
            self.t.color(self.color)
            self.l = L + (L*10)/nds * loop
            self.t.sety(self.calcule(nds,L))
            self.t.down()
            self.poliguon(nds,L)
            self.t.up()
            self.t.seth(0)
            self.t.sety(0)
        self.t.clear()

        #self.tre()

        #self.t.down
    def mainloop(self):
        self.t.mainloop()

self = programe()
V3= 2
while V3 <= 10:
    self.run(V3,10)




    V3 += 1

self.mainloop()