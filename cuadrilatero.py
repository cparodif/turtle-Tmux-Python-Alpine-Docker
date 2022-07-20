#!/usr/bin/env python3

class Cuadrilatero:
    
    def __init__(self, segmento1, segmento2,segmento3,segmento4):
        self.segmento1 = segmento1
        self.segmento2 = segmento2
        self.segmento3 = segmento3
        self.segmento4 = segmento4

        self.Xmax=0.0
        self.Xmin=0.0
        self.Ymax=0.0
        self.Ymin=0.0

        self.moverX=0.0
        self.moverY=0.0
        self.zoom=0 #zoom=0 ->Recalcular, zoom!=0 -> No recalcular, valor habitual zoom=75937
    
        self.segmentof1 = segmento1
        self.segmentof2 = segmento2
        self.segmentof3 = segmento3
        self.segmentof4 = segmento4

        self.Xmaxf=0.0
        self.Xminf=0.0
        self.Ymaxf=0.0
        self.Yminf=0.0

        self.d=0 # d=0 ->No debug, d=1 ->debug


    def vertices(self):
        x1=self.segmento1[0][0]
        x2=self.segmento2[0][0]
        x3=self.segmento3[0][0]
        x4=self.segmento4[0][0]

        y1=self.segmento1[0][1]
        y2=self.segmento2[0][1]
        y3=self.segmento3[0][1]
        y4=self.segmento4[0][1]
        if self.d: print("vertices",x1,y1,x2,y2,x3,y3,x4,y4)
        return(x1,y1,x2,y2,x3,y3,x4,y4)

    def verticesf(self):
        x1=self.segmentof1[0][0]
        x2=self.segmentof2[0][0]
        x3=self.segmentof3[0][0]
        x4=self.segmentof4[0][0]

        y1=self.segmentof1[0][1]
        y2=self.segmentof2[0][1]
        y3=self.segmentof3[0][1]
        y4=self.segmentof4[0][1]
        if self.d: print("verticesf",x1,y1,x2,y2,x3,y3,x4,y4)
        return(x1,y1,x2,y2,x3,y3,x4,y4)

    def strpunto(m,n):
        return "("+str(round(m,3))+" , "+str(round(n,3))+")"

    def strrecta(r):
        return "recta: "+str(r) 

    def pendientef(self,i):
        retornar=0
        # de Ecuación de la recta que pasa por (m1, n1) (m2, n2)
        if i==1: retornar=(self.segmentof1[1][1]-self.segmentof1[0][1])/(self.segmentof1[1][0]-self.segmentof1[0][0])
        if i==2: retornar=(self.segmentof2[1][1]-self.segmentof2[0][1])/(self.segmentof2[1][0]-self.segmentof2[0][0])
        if i==3: retornar=(self.segmentof3[1][1]-self.segmentof3[0][1])/(self.segmentof3[1][0]-self.segmentof3[0][0])
        if i==4: retornar=(self.segmentof4[1][1]-self.segmentof4[0][1])/(self.segmentof4[1][0]-self.segmentof4[0][0])
        if self.d: print("*** segmento=",i," - pendiente=",retornar)
        return retornar

    def terminoIndependientef(self,i):
        retornar=0
        #de la Ecuación de la recta que pasa por (m1, n1) (m2, n2)
        if i==1: retornar=self.segmentof1[0][1] - (self.segmentof1[0][0] * self.pendientef(1))
        if i==2: retornar=self.segmentof2[0][1] - (self.segmentof2[0][0] * self.pendientef(2))
        if i==3: retornar=self.segmentof3[0][1] - (self.segmentof3[0][0] * self.pendientef(3))
        if i==4: retornar=self.segmentof4[0][1] - (self.segmentof4[0][0] * self.pendientef(4))
        if self.d: print("*** segmento=",i," - terminoIndependiente=",retornar)
        return retornar

    def pendienteRInversaf(self,i):
        retornar=0
        # de Ecuación de la recta que pasa por (m1, n1) (m2, n2)
        if i==1: retornar=(self.segmentof1[1][0]-self.segmentof1[0][0])/(self.segmentof1[1][1]-self.segmentof1[0][1])
        if i==2: retornar=(self.segmentof2[1][0]-self.segmentof2[0][0])/(self.segmentof2[1][1]-self.segmentof2[0][1])
        if i==3: retornar=(self.segmentof3[1][0]-self.segmentof3[0][0])/(self.segmentof3[1][1]-self.segmentof3[0][1])
        if i==4: retornar=(self.segmentof4[1][0]-self.segmentof4[0][0])/(self.segmentof4[1][1]-self.segmentof4[0][1])
        if self.d: print("*** segmento=",i," - pendienteRInversa=",retornar)
        return retornar

    def terminoIndependienteRInversaf(self,i):
        retornar=0
        #de la Ecuación de la recta que pasa por (m1, n1) (m2, n2)
        if i==1: retornar=self.segmentof1[0][0] - (self.segmentof1[0][1] * self.pendienteRInversaf(1))
        if i==2: retornar=self.segmentof2[0][0] - (self.segmentof2[0][1] * self.pendienteRInversaf(2))
        if i==3: retornar=self.segmentof3[0][0] - (self.segmentof3[0][1] * self.pendienteRInversaf(3))
        if i==4: retornar=self.segmentof4[0][0] - (self.segmentof4[0][1] * self.pendienteRInversaf(4))
        if self.d: print("*** segmento=",i," - terminoIndependienteRInversa=",retornar)
        return retornar  

    def valorFuncionRectaf(self,i,x5):
        retornar=0
        if i==1: retornar=self.pendientef(1)*x5 + self.terminoIndependientef(1)
        if i==2: retornar=self.pendientef(2)*x5 + self.terminoIndependientef(2)
        if i==3: retornar=self.pendientef(3)*x5 + self.terminoIndependientef(3)
        if i==4: retornar=self.pendientef(4)*x5 + self.terminoIndependientef(4)
        if self.d: print("*** segmento=",i," x5=",x5," - valorFuncionRecta=",retornar)
        return retornar 

    def valorFuncionRInversaf(self,i,y5):
        retornar=0
        if i==1: retornar=self.pendienteRInversaf(1)*y5 + self.terminoIndependienteRInversaf(1)
        if i==2: retornar=self.pendienteRInversaf(2)*y5 + self.terminoIndependienteRInversaf(2)
        if i==3: retornar=self.pendienteRInversaf(3)*y5 + self.terminoIndependienteRInversaf(3)
        if i==4: retornar=self.pendienteRInversaf(4)*y5 + self.terminoIndependienteRInversaf(4)
        if self.d: print("*** segmento=",i," ",y5," - valorFuncionRInversa=",retornar)
        return retornar 

    def ajustarEscala(self,x):
        global d
        n = 0
        x= abs(x)
        a=x
        while x < 600:
            n = n + 1
            x = x * 10
            if self.d: print("n=",n,"  x=",x)
        y = a*(10**(n-1)) 
        if self.d: print("x , y ",x,y)
        m=0
        while y < 600:
        #while abs(x - int(x)) >0:
            m=m+1
            y = y * 1.5
            if self.d: print("m=",m," y=",y)
        if self.d: print("Seleccionar n=",n-1,"Seleccionar m=",m-1)
        if self.d: print("\n*****************************************************************")
        if self.d: print("Escala(zoom)=(10**(",n-1,"))*(1.5**(",m-1,"))=",(10**(n-1))*(1.5**(m-1) ))
        if self.d: print("*****************************************************************")
        #xReducirEscala = (10**(n-1))*(1.5**(m-1))
        #xReducirEscala = 10**(n-1)
        #if self.d: print("xReducirEscala",xReducirEscala)
        return (10**(n-1))*(1.5**(m-1))



    #def transformarCuadrilatero(segmento1, segmento2,segmento3,segmento4):
    def transformarCuadrilatero(self):
        x1,y1,x2,y2,x3,y3,x4,y4=self.vertices()
        if self.d: print("\nPuntos iniciales de cuadrilatero (1):")
        if self.d: print("Vertice ..... (x1,y1)= ",x1,y1)
        if self.d: print("Vertice ..... (x2,y2)= ",x2,y2)
        if self.d: print("Vertice ..... (x3,y3)= ",x3,x3)
        if self.d: print("Vertice ..... (x4,y4)= ",x4,y4)

        self.Xmax = max(x1,x2,x3,x4)
        self.Xmin = min(x1,x2,x3,x4) 
        self.Ymax = max(y1,y2,y3,y4)
        self.Ymin = min(y1,y2,y3,y4)
        
        Xmini=self.Xmin; Ymini=self.Ymin; Xmaxi=self.Xmax; Ymaxi=self.Ymax
        if self.d: print("Máximos y mínimos. Xmax= ",self.Xmax,"  Xmin=",self.Xmin,"  Ymax=",self.Ymax,"  Ymin=",self.Ymin)

        self.moverX= self.Xmin 
        self.moverY= self.Ymin 
        if self.d: print("\n*****************************************************************")
        if self.d:print("Traslación en eje X= +(", -self.Xmin ,")  Traslación en eje Y= +(", -self.Ymin ,")")
        if self.d: print("*****************************************************************")
        
        #  Muevo el cuadrilatero al origen de coordenadas: 
        x1 = x1 - self.moverX
        x2 = x2 - self.moverX
        x3 = x3 - self.moverX
        x4 = x4 - self.moverX

        y1 = y1 - self.moverY
        y2 = y2 - self.moverY
        y3 = y3 - self.moverY
        y4 = y4 - self.moverY

        self.Xmaxf = max(x1,x2,x3,x4)
        self.Xminf = min(x1,x2,x3,x4)
        self.Ymaxf = max(y1,y2,y3,y4)
        self.Yminf = min(y1,y2,y3,y4)
        if self.d: print("Nuevos máximos y mínimos. Xmax= ",self.Xmaxf,"  Xmin=",self.Xminf,"  Ymax=",self.Ymaxf,"  Ymin=",self.Yminf)

        # Ampliamos el cuadrilatero para empezar a trabajar con menos y reducir los errores de precision en los cálculos 
        if (self.zoom > 0):
            if self.d: print("\nNo se cambia la escala utilizada. self.zoom = x",self.zoom)
        else:
            self.zoom=min(self.ajustarEscala(self.Xmaxf),self.ajustarEscala(self.Ymaxf))
            if self.d: print("\nzoom. Escala utilizada= x",self.zoom)
        if self.d: print("Escala utilizada (zoom) = x",self.zoom)
        # ampliamos al escala para todos los puntos para evitar errores de precisión 
        x1 = x1 * self.zoom
        x2 = x2 * self.zoom
        x3 = x3 * self.zoom
        x4 = x4 * self.zoom

        y1 = y1 * self.zoom
        y2 = y2 * self.zoom
        y3 = y3 * self.zoom
        y4 = y4 * self.zoom


        if self.d: print("\nNuevos puntos. Paso 3. Aplico el zoom. Cambio de escala:")
        if self.d: print("Vertice (x1,y1)= ",x1,y1)
        if self.d: print("Vertice (x2,y2)= ",x2,y2)
        if self.d: print("Vertice (x3,y3)= ",x3,y3)
        if self.d: print("Vertice (x4,y4)= ",x4,y4)
        
        self.Xmaxf = max(x1,x2,x3,x4)
        self.Xminf = min(x1,x2,x3,x4)
        self.Ymaxf = max(y1,y2,y3,y4)
        self.Yminf = min(y1,y2,y3,y4)
        if self.d: print("Nuevos máximos y mínimos. Xmax= ",self.Xmaxf,"  self.Xminf=",self.Xminf,"  Ymax=",self.Ymaxf,"  Ymin=",self.Yminf)

        self.segmentof1=[[x1,y1],[x2,y2]]
        self.segmentof2=[[x2,y2],[x3,y3]]
        self.segmentof3=[[x3,y3],[x4,y4]]
        self.segmentof4=[[x4,y4],[x1,y1]]

        if self.d: print("\nSegmentos transformados:")
        if self.d: print("recta 1",  self.segmentof1)
        if self.d: print("recta 2",  self.segmentof2)
        if self.d: print("recta 3",  self.segmentof3)
        if self.d: print("recta 4",  self.segmentof4)

        return(self.moverX,self.moverY,self.zoom,self.Xminf,self.Yminf,self.Xmaxf,self.Ymaxf)


    def tieneUnPuntoDeCorteInterno(self,segmentoA, segmentoB):
        retornar=0
        descartarEstaPareja=1
        px1= segmentoA[0][0]
        px2= segmentoA[1][0]
        px3= segmentoB[0][0]
        px4= segmentoB[1][0]

        py1= segmentoA[0][1]
        py2= segmentoA[1][1]
        py3= segmentoB[0][1]
        py4= segmentoB[1][1]

        if ((px2-px1)!=0 and (px4-px3)!=0):
            m1=(py2-py1)/(px2-px1)
            m3=(py4-py3)/(px4-px3)
            px01= round( (px1*m1-py1+py3-px3*m3)/(m1-m3) ,8)
            py01= round(m1*(px01-px1)+py1,8)
            px03= round( (px3*m3-py3+py1-px1*m1)/(m3-m1) ,8)
            py03= round(m3*(px03-px3)+py3,8)
            if abs(px03)==0.0:px03=0.0
            if abs(px01)==0.0:px01=0.0
            if abs(py03)==0.0:py03=0.0
            if abs(py01)==0.0:py01=0.0
            #El punto de corte es (px01,py01)
            px01=round(px01,2)
            py01=round(py01,2)
            px03=round(px03,2)
            py03=round(py03,2)
            px1=round(px1,2)
            py1=round(py1,2)
            px2=round(px2,2)
            py2=round(py2,2)
            px3=round(px3,2)
            py3=round(py3,2)
            px4=round(px4,2)
            py4=round(py4,2)  
            
            #coinciden los puntos de corte, y el punto de corte está entre los máximos y minimos
            if (px01==px03 and py01==py03)and (self.Xminf<=px01 and px01<=self.Xmaxf and self.Yminf<=py01 and py01<=self.Ymaxf):
                if (px01==round(px1,2) and py01==round(py1,2)):
                    descartarEstaPareja=descartarEstaPareja*0
                if (px01==round(px2,2) and py01==round(py2,2)):
                    descartarEstaPareja=descartarEstaPareja*0
                if (px01==round(px3,2) and py01==round(py3,2)):
                    descartarEstaPareja=descartarEstaPareja*0
                if (px01==round(px4,2) and py01==round(py4,2)):
                    descartarEstaPareja=descartarEstaPareja*0
                if (descartarEstaPareja==1):
                    if self.d: print("-DescartarParejaDeRectas ...",descartarEstaPareja,"-El Punto de Corte no es un vertice = (",px01,py01,")=(",px03,py03,")----",px1,py1,"-",px2,py2,"-",px3,py3,"-",px4,py4)
                    ### seleccionar una combinación que no tenga estos dos segmentos
                    segmentosNoUtiles=[[px1,py1,px2,py2],[px3,py3,px4,py4]]
                    print("segmentosNoUtiles",segmentosNoUtiles)
                    retornar=1
                else:
                    if self.d: print("-El Punto de Corte es = (",px01,py01,")=(",px03,py03,") rectas:(",px1,py1,")-(",px2,py2,")-y-(",px3,py3,")-(",px4,py4,")")
        return retornar

    def esUnCuadrilatero(self):
        if self.d: print("\nVerificar punto de corte por parejas ... ")  
        retornar=1
    
        if self.tieneUnPuntoDeCorteInterno(self.segmentof1, self.segmentof3):
           retornar=retornar*0

        if self.tieneUnPuntoDeCorteInterno(self.segmentof2, self.segmentof4):
           retornar=retornar*0

        if self.tieneUnPuntoDeCorteInterno(self.segmentof1, self.segmentof2):
            retornar=retornar*0

        if self.tieneUnPuntoDeCorteInterno(self.segmentof1, self.segmentof4):
            retornar=retornar*0
        
        if self.tieneUnPuntoDeCorteInterno(self.segmentof2, self.segmentof3):
            retornar=retornar*0
    
        if self.tieneUnPuntoDeCorteInterno(self.segmentof3, self.segmentof4):
            retornar=retornar*0
        
        if retornar:
            if self.d: print("\Cuadrilatero seleccionado ...CAMBIANDO ... ")
            if self.d: print("recta 1",  self.segmentof1)
            if self.d: print("recta 2",  self.segmentof2)
            if self.d: print("recta 3",  self.segmentof3)
            if self.d: print("recta 4",  self.segmentof4)
            #seleccionarCuadrilatero=1

        return retornar 


    def estePuntoPerteneceAlCuadrilatero(self,x5, y5):
        resultado = "No pertenece"
        devolver = 0
        return resultado
