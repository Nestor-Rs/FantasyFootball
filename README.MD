# Fantasy Football

That's a simulation of world cup, using a neural network supervised.

You need information of group data to use that neural network:

~~~py
ranking=[[1440,1464,1584,1694],[1728,1565,1627,1570],[1774,1438,1645,1549],[1760,1489,1667,1508],[1715,1504,1650,1560],[1644,1475,1564,1646],[1841,1564,1636,1471],[1677,1393,1639,1530]]

ganadores=[[1694,1584],[1728,1627],[1774,1549],[1760,1489],[1715,1560],[1564,1646],[1841,1636],[1677,1393]]
~~~

## Perceptron

Use a sinus activation function to define winners.

In code, it's a class and has constructor receive an input list and a weight list .

Input -> weight -> Perceptron (play game and get winner) -> two winners

~~~py
import math

class perceptron():
    #All data used
    input=[]
    weight=[]
    points=[]
    winers=[]
    #Init class
    def __init__(self,input,weight):
        self.input=input
        self.weight=weight
        self.points=[0,0,0,0]
    #Evaluation for play
    def jugarPartidos(self):
        self.points=[0,0,0,0]
        for i in range(len(self.input)):
            for j in range(i+1,len(self.input)):
                playerA=abs(math.sin(self.input[i]*self.weight[i]))
                playerB=abs(math.sin(self.input[j]*self.weight[j]))
                if playerA > playerB:
                    self.points[i]+=1
                else:
                    self.points[j]+=1
    #Get the two best players
    def ganadores(self):
        primerLugar=0
        segundoLugar=0
        for i in range(len(self.points)):
            if self.points[i]>primerLugar:
                segundoLugar=primerLugar
                primerLugar=self.points[i]
            elif self.points[i]<primerLugar and self.points[i]>segundoLugar:
                segundoLugar=self.points[i]
        self.winers=[self.points.index(primerLugar),self.points.index(segundoLugar)]
        return self.winers
    #Calcula error and get new weight
    def nevoPeso(self,w,obtenido,esperado):
        error=esperado-obtenido
        newW=w+0.000004*error
        return newW
    #get a list of values, play and get new weights
    def aprender(self,esperado):
        for i in range(1000):
            self.jugarPartidos()
            w=self.ganadores()
            self.weight[w[0]]=self.nevoPeso(self.weight[w[0]],self.input[w[0]],esperado[0])
            self.weight[w[1]]=self.nevoPeso(self.weight[w[1]],self.input[w[1]],esperado[1])
            #print(self.weight)
            #print(self.points)
~~~

## Data

That's file contain all data used in program.

~~~py
#Incial data
equipoNombre=[["QATAR","ECUADOR","SENEGAL","HOLANDA"],["INGLATERRA","IRAN","ESTADOS UNIDOS","GALES"],["ARGENTINA","ARABIA SAUDITA","MEXICO","POLONIA"],["FRANCIA","AUSTRALIA","DINAMARCA","TUNEZ"],["ESPAÑA","COSTA RICA","ALEMANIA","JAPAN"],["BELGICA","CANADA","MARRUECOS","CROACIA"],["BRASIL","SERBIA","SUIZA","CAMERUN"],["PORTUGAL","GHANA","URUGUAY","COREA DEL SUR"]]
ranking=[[1440,1464,1584,1694],[1728,1565,1627,1570],[1774,1438,1645,1549],[1760,1489,1667,1508],[1715,1504,1650,1560],[1644,1475,1564,1646],[1841,1564,1636,1471],[1677,1393,1639,1530]]
ganadores=[[1694,1584],[1728,1627],[1774,1549],[1760,1489],[1715,1560],[1564,1646],[1841,1636],[1677,1393]]
#Ranking to search
rankingSearch=[1440,1464,1584,1694,1728,1565,1627,1570,1774,1438,1645,1549,1760,1489,1667,1508,1715,1504,1650,1560,1644,1475,1564,1646,1841,1564,1636,1471,1677,1393,1639,1530]
#Nombres to search
nombreSearch=["QATAR","ECUADOR","SENEGAL","HOLANDA","INGLATERRA","IRAN","ESTADOS UNIDOS","GALES","ARGENTINA","ARABIA SAUDITA","MEXICO","POLONIA","FRANCIA","AUSTRALIA","DINAMARCA","TUNEZ","ESPAÑA","COSTA RICA","ALEMANIA","JAPAN","BELGICA","CANADA","MARRUECOS","CROACIA","BRASIL","SERBIA","SUIZA","CAMERUN","PORTUGAL","GHANA","URUGUAY","COREA DEL SUR"]
~~~

## Main

Its word cup and modify the neural network.

~~~py
from data import *
from perceptron import *
#Neural Netwok List
octavos=[]
cuartos=[]
semifinal=[]
#=====================================Octavos============================================
#Data to next phase
inputCuartos=[]
pesosCuartos=[]
#Set data to Neural network
for i in range(len(ranking)):
    print("================= Octavos =================")
    octavos.append(perceptron(ranking[i],[1,1,1,1]))
    octavos[i].aprender(ganadores[i])
    print(equipoNombre[i][octavos[i].winers[0]])
    print(equipoNombre[i][octavos[i].winers[1]])
    # get data to next phase
    inputCuartos.append(octavos[i].input[octavos[i].winers[0]])
    inputCuartos.append(octavos[i].input[octavos[i].winers[1]])
    pesosCuartos.append(octavos[i].weight[octavos[i].winers[0]])
    pesosCuartos.append(octavos[i].weight[octavos[i].winers[1]])

print()
#=====================================Cuartos============================================

inputSemiFinal=[]
pesosSemiFinal=[]
#put the data in a list of list to neural netwok
for i in range(0,len(inputCuartos),4):
    newGroup=[]
    newWeight=[]
    for j in range(i,i+4):
        newGroup.append(inputCuartos[j])
        newWeight.append(pesosCuartos[j])
    cuartos.append(perceptron(newGroup,newWeight))
#Play and get winners
for i in range(len(cuartos)):
    print("================= Cuartos =================")
    cuartos[i].jugarPartidos()
    cuartos[i].ganadores()
    print(nombreSearch[rankingSearch.index(cuartos[i].input[cuartos[i].winers[0]])])
    print(nombreSearch[rankingSearch.index(cuartos[i].input[cuartos[i].winers[1]])])
    # get data to next phase
    inputSemiFinal.append(cuartos[i].input[cuartos[i].winers[0]])
    inputSemiFinal.append(cuartos[i].input[cuartos[i].winers[1]])
    pesosSemiFinal.append(cuartos[i].weight[cuartos[i].winers[0]])
    pesosSemiFinal.append(cuartos[i].weight[cuartos[i].winers[1]])
print()
#=====================================Semifinal============================================
#Data to next phase
inputFinal=[]
pesosFinal=[]
#put the data in a list of list to neural netwok
for i in range(0,len(inputSemiFinal),4):
    newGroup=[]
    newWeight=[]
    for j in range(i,i+4):
        newGroup.append(inputSemiFinal[j])
        newWeight.append(pesosSemiFinal[j])
    semifinal.append(perceptron(newGroup,newWeight))
#Play and get winners
for i in range(len(semifinal)):
    print("================= Semi Final =================")
    semifinal[i].jugarPartidos()
    semifinal[i].ganadores()
    print(nombreSearch[rankingSearch.index(semifinal[i].input[semifinal[i].winers[0]])])
    print(nombreSearch[rankingSearch.index(semifinal[i].input[semifinal[i].winers[1]])])
    # get data to next phase
    inputFinal.append(semifinal[i].input[semifinal[i].winers[0]])
    inputFinal.append(semifinal[i].input[semifinal[i].winers[1]])
    pesosFinal.append(semifinal[i].weight[semifinal[i].winers[0]])
    pesosFinal.append(semifinal[i].weight[semifinal[i].winers[1]])
print()

#=====================================Final============================================
#Put data to final perceptron
final=perceptron(inputFinal,pesosFinal)

print("================= Final =================")
#Play 
final.jugarPartidos()
#Get winners
final.ganadores()
#Print Champion
print("Campeon "+nombreSearch[rankingSearch.index(final.input[final.winers[0]])])
print(nombreSearch[rankingSearch.index(final.input[final.winers[1]])])
~~~

## Result and Winner

using the information of data file, the simulation set that's result:

~~~log
================= Octavos =================
HOLANDA
SENEGAL
================= Octavos =================
INGLATERRA
ESTADOS UNIDOS
================= Octavos =================
ARGENTINA
POLONIA
================= Octavos =================
FRANCIA
AUSTRALIA
================= Octavos =================
ESPAÑA
JAPAN
================= Octavos =================
CANADA
CROACIA
================= Octavos =================
BRASIL
SUIZA
================= Octavos =================
PORTUGAL
GHANA

================= Cuartos =================
HOLANDA
SENEGAL
================= Cuartos =================
FRANCIA
ARGENTINA
================= Cuartos =================
ESPAÑA
CANADA
================= Cuartos =================
BRASIL
PORTUGAL

================= Semi Final =================
FRANCIA
ARGENTINA
================= Semi Final =================
BRASIL
ESPAÑA

================= Final =================
Campeon BRASIL
FRANCIA
~~~
