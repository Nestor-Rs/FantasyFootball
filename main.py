from data import *
from perseptron import *

neuralNetwork = []

for i in range(len(equipoID)):
    juegos=[]
    for j in range(len(equipoID[i])):
        for k in range(j+1,len(equipoID[i])):
            jugadores=[equipoID[i][j],equipoID[i][k]]
            pesos=[ranking[i][j],ranking[i][k]]
            juegos.append(perseptron(jugadores,pesos))
    neuralNetwork.append(juegos)
            #print("%i - %i"%(equipoID[i][j],equipoID[i][k]))
    #print("\n")

for i in range(len(neuralNetwork)):
    for j in range(len(neuralNetwork[i])):
        print(neuralNetwork[i][j].evalution())
    print()