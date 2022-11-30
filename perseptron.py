import math

class perseptron():
    input=[]
    weight=[]
    def __init__(self,input,weight):
        self.input=input
        self.weight=weight

    def activation(self,x):
        if  math.sin(x)>0.5:
            return 1
        elif math.sin(x)<-0.5:
            return -1
        else:
            return 0

    def evalution(self):
        data=0
        for i in range(len(self.input)):
            data+=self.input[i]*self.weight[i]
        return self.activation(data)