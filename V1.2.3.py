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
        self.t.hideturtle()
        self.t.bgcolor('black')
        self.t.color('white')
        self.nds = 8
        self.couches = 30
        self.L = 10
    def calcule(self):
        V1 = (self.l / 2) / (sin(radians(360 / (self.nds * 2))))
        return V1
    def poliguon(self):
        self.t.right((360 / self.nds) / 2)
        for loop in range(self.nds):
            self.t.fd(self.l)
            self.t.right(360 / self.nds)
    def tre(self):

        self.t.color('white')
        self.t.pensize(1)
        self.t.up()
        self.t.setpos(0, 0)
        self.t.down()
        self.t.seth(90)
        for loop in range(self.nds):
            self.t.setpos(0, 0)
            l = (self.L + (self.l * 10) / self.nds) * (self.couches)
            self.t.fd(l)
            self.t.right(360 / self.nds)

    def run(self):
        for loop in range(self.couches):
            self.color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
            self.t.color(self.color)
            self.l = self.L + (self.L*10)/self.nds * loop
            self.t.sety(self.calcule())
            self.t.down()
            self.poliguon()
            self.t.up()
            self.t.seth(0)
            self.t.sety(0)

        #self.tre()
        self.t.mainloop()

self = programe()



self.run()

