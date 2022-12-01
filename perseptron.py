import math

class perseptron():
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