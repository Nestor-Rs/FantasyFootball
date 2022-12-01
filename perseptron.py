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
        self.points=[0,0,0,0]
        for i in range(len(self.input)):
            for j in range(i+1,len(self.input)):
                playerA=abs(math.sin(self.input[i]*self.weight[i]))
                playerB=abs(math.sin(self.input[j]*self.weight[j]))
                if playerA > playerB:
                    self.points[i]+=1
                else:
                    self.points[j]+=1

    def ganadores(self):
        primerLugar=0
        segundoLugar=0
        for i in range(len(self.points)):
            if self.points[i]>primerLugar:
                segundoLugar=primerLugar
                primerLugar=self.points[i]
            elif self.points[i]<primerLugar and self.points[i]>segundoLugar:
                segundoLugar=self.points[i]
        return [self.points.index(primerLugar),self.points.index(segundoLugar)]

    def nevoPeso(self,w,obtenido,esperado):
        error=esperado-obtenido
        newW=w+0.000004*error
        return newW
    
    def aprender(self,esperado):
        for i in range(50):
            self.jugarPartidos()
            w=self.ganadores()
            self.weight[w[0]]=self.nevoPeso(self.weight[w[0]],self.input[w[0]],esperado[0])
            self.weight[w[1]]=self.nevoPeso(self.weight[w[1]],self.input[w[1]],esperado[1])
            print(self.weight)
            print(self.points)


inp=[1440,1464,1584,1694]
pesos=[1,1,1,1]

a=perseptron(inp,pesos)
print(a.weight)
a.aprender([1694,1584])