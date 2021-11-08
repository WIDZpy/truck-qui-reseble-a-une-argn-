import turtle
from math import *
tu = turtle
nombre_de_som = 20
cote = 10
tu.speed(0)
tu.pensize(2)
repetition = 30
tu.up()
tu.hideturtle()
tu.bgcolor('black')
tu.color('white')
def calcule2(N,C):
    V1 = (C/2)/(sin(radians(360/(N*2))))
    print(V1)



    return V1
def calcule(N,C):

    if N % 2 == 0:
            V1 = (C/2)/(cos((180*(N-2))/N))
    elif N % 2 == 1:
        V1 = (C/2)/(tan(360/(N-2)))
        print(V1)
    return V1

#print(calcule(5,4))



def formes(nbsomet,longeurcote,x = 0):
    tu.pendown
    if x == 0 :

        tu.right((360/nbsomet)/2)
        #tu.right(360/nbsomet)

    for forme in range(nbsomet + -x):
        tu.fd(longeurcote)
        tu.right(360/nbsomet)



def millieux(nbsomet,longeurcoté):
    V1 = 0
    formes(nbsomet,longeurcoté)
    if nbsomet % 2 == 0:

        formes(nbsomet, longeurcoté, int(nbsomet / 2))

    if nbsomet % 2 == 1:
        formes(nbsomet, longeurcoté, int((nbsomet-1) / 2)+1)

        tu.fd(longeurcoté / 2)
    tu.seth(0)
    y = tu.ycor()


    return y * -1

#print(millieux(4,100))
#print(calcule(4,100))


def final(nbs ,L , repete):

    for loop in range(repete):
        l = L + (L*10)/nbs * loop
        tu.sety(calcule2(nbs,l))
        tu.down()
        formes(nbs,l)
        tu.up()
        tu.seth(0)
        tu.sety(0)


tu.sety(calcule2(5,4))

def tre(N,C,repetition):
    tu.up()
    tu.setpos(0,0)
    tu.down()
    tu.seth(90)
    for loop in range(N):
        tu.setpos(0, 0)
        l = (C + (C*10)/N )* (repetition)
        tu.fd(l)
        tu.right(360/N)

final(nombre_de_som,cote,repetition)
tre(nombre_de_som,cote,repetition)
tu.mainloop()


