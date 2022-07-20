#!/usr/bin/env python3

from turtle import *
import subprocess
from cuadrilatero import *

subprocess.call(["/usr/bin/clear"]) # borrar pantalla

# ***********************************************
# **** Configurar No modificar ******************
# ***********************************************
d=0 # d=0 ->No debug, d=1 ->debug
xTamañoVentana=800
yTamañoVentana=600
xTamañoScreen=700
yTamañoScreen=500
moverEjeX=300
moverEjeY=200

# ***********************************************
# ** Vertices ->(x1,y1),(x2,y2),(x3,y3),(x4,y4)**
# ***********************************************
x1=-300
y1=-190
x2=285
y2=100
x3=320
y3=-140
x4=-220
y4=200
# ***********************************************
# ****x5,y5 ->punto de situación ****************
# ***********************************************
x5=100
y5=100
# ***********************************************
# ***********************************************
# ***********************************************

# ***********************************************
# *************funciones*************************
# ***********************************************


def OK(n):
    try: 
        n=float(n)
    except:
        n=OK(input("Caracter no valido"))
    return n

def OKI(n):
    try: 
        n=int(n)
    except:
        n=OK(Iinput("Caracter no valido"))
    return n

def ns(c):
    while c!=("s") and c!=("n"):
        print(chr(7));c=input("Escribe solo \'n\' o \'s\' segun su opcion: ")
    return c

def strpunto(m,n):
    return "("+str(round(m,3))+" , "+str(round(n,3))+")"

def strrecta(r):
    return "recta: "+str(r) 

def recta(nRecta,m1,n1,m2,n2,mMoverEjeX,nMoverEjeY):
    t.pencolor("yellow")
    t.penup()
    t.goto(m1-mMoverEjeX,n1-nMoverEjeY)
    t.write(strpunto(round(m1,3),round(n1,3)), align="center", font=('Verdana', 12, 'bold'))  
    t.pendown()
    t.dot(10,"green")
    t.goto(m2-mMoverEjeX,n2-nMoverEjeY)
    t.write(strpunto(round(m2,3),round(n2,3)), align="center", font=('Verdana', 12, 'bold'))
    t.dot(10,"green")
    t.pencolor("blue")
    t.penup()
    if m1<m2:
      xParaEscribirRecta=m1+(abs(m1-m2)/2)- mMoverEjeX
    else:
      xParaEscribirRecta=m2+(abs(m1-m2)/2)- mMoverEjeX
    
    if n1<n2:
      yParaEscribirRecta=n1+(abs(n1-n2)/2)- nMoverEjeY
    else:
      yParaEscribirRecta=n2+(abs(n1-n2)/2)- nMoverEjeY

    t.goto(xParaEscribirRecta,yParaEscribirRecta)
    t.pendown()
    t.write("Recta"+str(nRecta), align="center", font=('Verdana', 12, 'bold')) 
    t.penup()


# ***********************************************
# **************principal************************
# ***********************************************

qc="n"
#qc=ns(input("Especificar coordenadas?: "))
if qc==("s"):
    x1=OK(input("Introduce eje X ordenada punto 1 \'x1\': "))    
    y1=OK(input("Introduce eje Y ordenada punto 1 \'y1\': "))    
    x2=OK(input("Introduce eje X ordenada punto 2 \'x2\': "))    
    y2=OK(input("Introduce eje Y ordenada punto 2 \'y3\': "))    
    x3=OK(input("Introduce eje X ordenada punto 3 \'x3\': "))    
    y3=OK(input("Introduce eje Y ordenada punto 3 \'y3\': "))    
    x4=OK(input("Introduce eje X ordenada punto 4 \'x4\': "))    
    y4=OK(input("Introduce eje Y ordenada punto 4 \'y4\': "))    
    x5=OK(input("Introduce eje X ordenada punto 5 \'x5\': "))    
    y5=OK(input("Introduce eje Y ordenada punto 5 \'y5\': "))    

# ***********************************************
# ************ calculos *************************
# ***********************************************
x5i=x5
y5i=y5

figura=[]
micuadrilatero1=Cuadrilatero([[x1,y1],[x2,y2]],[[x2,y2],[x3,y3]],[[x3,y3,],[x4,y4]],[[x4,y4],[x1,y1]]) # c1234
moverX,moverY,zoom,Xmin,Ymin,Xmax,Ymax=micuadrilatero1.transformarCuadrilatero()
if micuadrilatero1.esUnCuadrilatero():
    figura=micuadrilatero1
    print("Cuadrilatero 1 seleccionado  ")
else:
    micuadrilatero2=Cuadrilatero([[x1,y1],[x2,y2]],[[x2,y2],[x4,y4]],[[x4,y4,],[x3,y3]],[[x3,y3],[x1,y1]]) # c1243
    moverX,moverY,zoom,Xmin,Ymin,Xmax,Ymax=micuadrilatero2.transformarCuadrilatero()
    if micuadrilatero2.esUnCuadrilatero():
        print("Cuadrilatero 2 seleccionado  ")
        figura=micuadrilatero2
    else:
        del micuadrilatero2
        micuadrilatero3=Cuadrilatero([[x1,y1],[x3,y3]],[[x3,y3],[x2,y2]],[[x2,y2,],[x4,y4]],[[x4,y4],[x1,y1]]) # c1324
        moverX,moverY,zoom,Xmin,Ymin,Xmax,Ymax=micuadrilatero3.transformarCuadrilatero()
        if micuadrilatero3.esUnCuadrilatero():
            print("Cuadrilatero 3 seleccionado  ")
            figura=micuadrilatero3
        else:
            del micuadrilatero3
            print("No es un Cuadrilatero  ")
            figura=micuadrilatero1
            del micuadrilatero1

moverX,moverY,zoom,Xmin,Ymin,Xmax,Ymax=figura.transformarCuadrilatero()
x1,y1,x2,y2,x3,y3,x4,y4=figura.verticesf()
x1i,y1i,x2i,y2i,x3i,y3i,x4i,y4i=figura.vertices()
resultado = figura.estePuntoPerteneceAlCuadrilatero(x5,y5)


# ***********************************************
# ************ gráfica **************************
# ***********************************************

#qc=ns(input("Dibujar?: "))
qc="s"
if qc==("s"):
    setup(xTamañoVentana,yTamañoVentana,0,0)
    screensize(xTamañoScreen,yTamañoScreen)
    
    t=Turtle()
    title("Ejem")
    t.shape("turtle")
    t.shape("classic")
    t.hideturtle()
    
    t.speed(0)
    t.pensize(1)
    canvas = Screen()
    canvas.bgcolor ("purple")
    t.color('blue')
    
    t.home()
    t.penup()
    t.goto(-380,0-moverEjeY)
    t.pendown()
    t.goto(380,0-moverEjeY)
    t.penup()  
    t.goto(0-moverEjeX,-280)
    t.pendown()
    t.goto(0-moverEjeX,280)
    t.penup()

    recta(1,x1, y1, x2, y2, moverEjeX, moverEjeY)    
    recta(2,x2, y2, x3, y3, moverEjeX, moverEjeY)    
    recta(3,x3, y3, x4, y4, moverEjeX, moverEjeY)    
    recta(4,x4, y4, x1, y1, moverEjeX, moverEjeY)    
    

    t.penup()
    t.goto(250,-80)
    t.pendown()
    t.color("white", "black")
    t.write("Vertice p1="+strpunto(x1i,y1i), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-100)
    t.pendown()
    t.write("Vertice p2="+strpunto(x2i,y2i), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-120)
    t.pendown()
    t.write("Vertice p3="+strpunto(x3i,y3i), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-140)
    t.pendown()
    t.write("Vertice p4="+strpunto(x4i,y4i), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-170)
    t.pendown()
    t.write("- Punto p5="+strpunto(x5i,y5i), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-200)
    t.pendown()
    t.write("TraslaciónX= - "+str(moverX), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-220)
    t.pendown()
    t.write("TraslaciónY= - "+str(moverY), align="center", font=('Verdana', 12, 'bold'))
    t.penup()
    t.goto(250,-240)
    t.pendown()
    t.write("Escala por    ="+str(round(zoom,5)), align="center", font=('Verdana', 12, 'bold'))
    
    t.penup()
    t.goto(((x5-moverX)*zoom) - moverEjeX,((y5-moverY)*zoom)-12 - moverEjeY)
    t.pendown()
    t.color("black", "yellow")
    t.begin_fill()
    t.circle(12)
    t.end_fill()
    t.goto(((x5-moverX)*zoom) - moverEjeX,((y5-moverY)*zoom) - moverEjeY)
    t.write(strpunto(((x5-moverX)*zoom),((y5-moverY)*zoom)), align="center", font=('Verdana', 12, 'bold'))
    t.dot(5,"white")

    t.penup()
    t.goto(0 - moverEjeX + 150,0 - moverEjeY-40)
    t.pendown()
    t.write("El punto "+resultado+" al cuadrilatero.", align="center", font=('Verdana', 12, 'bold'))  

    print("\nSondeo de puntos interiores:")

    numeroDePuntos=100
    if d: print("Nuevos máximos y mínimos. Xmax= ",Xmax,"  Xmin=",Xmin,"  Ymax=",Ymax,"  Ymin=",Ymin)
    for x in range(int(round(Xmin,0)),int(round(Xmax,0)),numeroDePuntos):
        for y in range(int(round(Ymin,0)),int(round(Ymax,0)),numeroDePuntos):
            #resultado = pertenece(((x/zoom)+moverX),((y/zoom)+moverY))
            resultado = figura.estePuntoPerteneceAlCuadrilatero(((x/zoom)+moverX),((y/zoom)+moverY))
            t.penup()
            t.goto(x- moverEjeX,y-12 - moverEjeY)
            t.pendown()
            if (resultado=="PERTENECE"):
                t.color("black", "green")
            else:
                t.color("black", "red")
            t.begin_fill()
            t.circle(12)
            t.end_fill()
            t.goto(x - moverEjeX,y - moverEjeY)
            t.write(strpunto(x,y), align="center", font=('Verdana', 12, 'bold'))
            t.dot(5,"white")
            t.penup()
    else:
        print("Finally finished!") 
     

mainloop()
