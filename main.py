from data import *
from perseptron import *

octavos=[]
cuartos=[]
semifinal=[]
final=[]
#=====================================Octavos============================================
inputCuartos=[]
pesosCuartos=[]
for i in range(len(ranking)):
    print("================= Octavos =================")
    octavos.append(perseptron(ranking[i],[1,1,1,1]))
    octavos[i].aprender(ganadores[i])
    print(equipoNombre[i][octavos[i].winers[0]])
    print(equipoNombre[i][octavos[i].winers[1]])

    inputCuartos.append(octavos[i].input[octavos[i].winers[0]])
    inputCuartos.append(octavos[i].input[octavos[i].winers[1]])
    pesosCuartos.append(octavos[i].weight[octavos[i].winers[0]])
    pesosCuartos.append(octavos[i].weight[octavos[i].winers[1]])

print()
#=====================================Cuartos============================================
for i in range(0,len(inputCuartos),4):
    newGroup=[]
    newWeight=[]
    for j in range(i,i+4):
        newGroup.append(inputCuartos[j])
        newWeight.append(pesosCuartos[j])
    
