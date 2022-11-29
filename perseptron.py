import numpy as np

class perseptron():
    input=[]
    weight=[]
    def __init__(self,input,weight):
        self.input=input
        self.weight=weight

    def evalution(self):
        data=0
        for i in range(np.size(self.input)):
            data+=self.input[i]*self.weight[i]
        return data
        
input=[1,2,3]
weight=[1,2,3]

a=perseptron(input,weight)
print(a.evalution())