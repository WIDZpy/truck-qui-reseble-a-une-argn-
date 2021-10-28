import turtle

tu = turtle
nombre_de_som = 5
cote = 10
tu.speed(0)
tu.pensize(2)
repetition = 100
tu.up()
tu.hideturtle()
tu.bgcolor('black')
tu.color('white')



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
        formes(nbsomet, longeurcoté, int((nbsomet-1) / 2)+1)

        tu.fd(longeurcoté / 2)
    tu.seth(0)
    y = tu.ycor()


    return y * -1



def final(nbs ,L , repete):

    for loop in range(repete):
        l = L + 45 * loop
        tu.sety(millieux(nbs, l) /2)
        print('CA')
        tu.down()
        formes(nbs,l)
        tu.up()
        tu.seth(0)
        tu.sety(0)



final(nombre_de_som,cote,repetition)
tu.mainloop()


