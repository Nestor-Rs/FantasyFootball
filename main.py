from data import *
from perseptron import *

octavos=[]
cuartos=[]
semifinal=[]
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
inputSemiFinal=[]
pesosSemiFinal=[]
for i in range(0,len(inputCuartos),4):
    newGroup=[]
    newWeight=[]
    for j in range(i,i+4):
        newGroup.append(inputCuartos[j])
        newWeight.append(pesosCuartos[j])
    cuartos.append(perseptron(newGroup,newWeight))

for i in range(len(cuartos)):
    print("================= Cuartos =================")
    cuartos[i].jugarPartidos()
    cuartos[i].ganadores()
    print(nombreSearch[rankingSearch.index(cuartos[i].input[cuartos[i].winers[0]])])
    print(nombreSearch[rankingSearch.index(cuartos[i].input[cuartos[i].winers[1]])])

    inputSemiFinal.append(cuartos[i].input[cuartos[i].winers[0]])
    inputSemiFinal.append(cuartos[i].input[cuartos[i].winers[1]])
    pesosSemiFinal.append(cuartos[i].weight[cuartos[i].winers[0]])
    pesosSemiFinal.append(cuartos[i].weight[cuartos[i].winers[1]])
print()
#=====================================Semifinal============================================
inputFinal=[]
pesosFinal=[]
for i in range(0,len(inputSemiFinal),4):
    newGroup=[]
    newWeight=[]
    for j in range(i,i+4):
        newGroup.append(inputSemiFinal[j])
        newWeight.append(pesosSemiFinal[j])
    semifinal.append(perseptron(newGroup,newWeight))

for i in range(len(semifinal)):
    print("================= Semi Final =================")
    semifinal[i].jugarPartidos()
    semifinal[i].ganadores()
    print(nombreSearch[rankingSearch.index(semifinal[i].input[semifinal[i].winers[0]])])
    print(nombreSearch[rankingSearch.index(semifinal[i].input[semifinal[i].winers[1]])])

    inputFinal.append(semifinal[i].input[semifinal[i].winers[0]])
    inputFinal.append(semifinal[i].input[semifinal[i].winers[1]])
    pesosFinal.append(semifinal[i].weight[semifinal[i].winers[0]])
    pesosFinal.append(semifinal[i].weight[semifinal[i].winers[1]])
print()

#=====================================Final============================================

final=perseptron(inputFinal,pesosFinal)

print("================= Final =================")
final.jugarPartidos()
final.ganadores()
print("Campeon "+nombreSearch[rankingSearch.index(final.input[final.winers[0]])])
print(nombreSearch[rankingSearch.index(final.input[final.winers[1]])])