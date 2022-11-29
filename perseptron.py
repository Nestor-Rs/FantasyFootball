import numpy as np
import math

class perseptron():
    input=[]
    weight=[]
    def __init__(self,input,weight):
        self.input=input
        self.weight=weight

    def activation(self,x):
        if  math.sin(x)>0.5:
            return True
        else:
            return False

    def evalution(self):
        data=0
        for i in range(np.size(self.input)):
            data+=self.input[i]*self.weight[i]
        return self.activation(data)
        
input=[3,2,3]
weight=[3,2,3]

a=perseptron(input,weight)
print(a.evalution())