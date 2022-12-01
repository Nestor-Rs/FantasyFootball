import math

class perseptron():
    input=[]
    weight=[]
    points=[]
    def __init__(self,input,weight):
        self.input=input
        self.weight=weight
        self.points=[0,0,0,0]

    def jugarPartidos(self):
        for i in range(len(self.input)):
            for j in range(i+1,len(self.input)):
                playerA=abs(math.sin(self.input[i]*self.weight[i]))
                playerB=abs(math.sin(self.input[j]*self.weight[j]))
                print("%f - %f"%(playerA,playerB))

                

inp=[1440,1464,1584,1694]
pesos=[1,1,1,1]

a=perseptron(inp,pesos)
a.jugarPartidos()

#print("%i - %i"%(i,j))