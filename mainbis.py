import turtle

tu = turtle
nombre_de_som = 10
cote = 100
tu.up()
tu.hideturtle()



def formes(nbsomet,longeurcoté,x = 0):

    if x == 0 :

        tu.right((360/nbsomet)/2)
        #tu.right(360/nbsomet)

    for forme in range(nbsomet + -x):
        tu.fd(longeurcoté)
        tu.right(360/nbsomet)



def millieux(nbsomet,longeurcoté):
    V1 = 0
    formes(nbsomet,longeurcoté)
    if nbsomet % 2 == 0:

        formes(nbsomet, longeurcoté, int(nbsomet / 2))

    if nbsomet % 2 == 1:
        formes(nbsomet, longeurcoté, (nbsomet-1) / 2)

        tu.fd(longeurcoté / 2)
    tu.seth(90)
    y = tu.ycor()


    return y * -1



def final(GG,nbs,L):
    tu.seth(0)
    tu.sety(GG/2)
    tu.down()
    formes(nbs,L)
    tu.up()
    tu.seth(0)



final(millieux(nombre_de_som,cote),nombre_de_som,cote)
tu.mainloop()


