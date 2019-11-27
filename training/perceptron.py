from random import uniform
import json
from math import e

class Perceptron:
    def __init__(self, trainSet, errb, max):
        self.trainSet = json.loads(trainSet)
        self.w = []
        self.wb = 0
        self.sp = 0
        self.errb = errb
        self.err = 0
        self.p = 0
        self.po = 0
        self.wo = []
        self.wbo = 0
        self.max = max

    def initializeW(self):
        for x in self.trainSet["table"]:
            for y in x["in"]:
              self.w.append(uniform(-1,1))
            break  
        for k in self.w:
            print(k)    
        self.wb = uniform(-1,1)
        self.p = self.errb + 1

    def training(self):
        iterations = 0
        while self.p > self.errb and iterations < self.max : 
            #self.p = 0
            for x in self.trainSet["table"]:
                acumVector = 0
                i = 0
                for j in x["in"]:
                    acumVector = acumVector + j*self.w[i]
                    i = i + 1
                self.sp = self.wb + acumVector
                #self.sp = 1/(1+e**(-1*self.sp))
                if self.sp < 0:
                    self.sp = 0
                else:
                    self.sp = 1
                self.err = x["y"] - self.sp
                if self.err != 0:
                    self.p = self.p + 1
                #Error cuadratico medio
                #self.ECM = self.ECM + self.err**2
                #self.ECM = self.ECM / len(self.trainSet["table"])
                #calcular pesos
                k=0
                for inT in x["in"]:
                    self.w[k] = self.w[k] + inT * self.err
                    k = k + 1
                self.wb = self.wb +  self.err
            #print("Iteracion" + repr(iterations))
            if self.p > self.po:
                self.wo = self.w
                self.po = self.p
                self.wbo = self.wb
            iterations = iterations + 1
        print("Iteraciones:" + repr(iterations))
        self.testPerceptron()
    
    def testPerceptron(self):
        for x in self.trainSet["table"]:
                acumVector = 0
                i = 0
                print("Con:")
                print(x["in"])
                for j in x["in"]:
                    acumVector = acumVector + j*self.wo[i]
                    i = i + 1
                self.sp = self.wbo + acumVector
                #self.sp = 1/(1+e**(-1*self.sp))
                if self.sp < 0:
                    self.sp = 0
                else:
                    self.sp = 1
                print("La salida es:" + repr(self.sp))

    def getWeight(self):
        weights = {"w":self.wo, "wb":self.wbo}
        return weights
    
    def runPerceptron(self,data):
        for x in self.trainSet["table"]:
                acumVector = 0
                i = 0
                print("Con:")
                print(x["in"])
                for j in x["in"]:
                    acumVector = acumVector + j*data["w"][i]
                    i = i + 1
                self.sp = data["wb"] + acumVector
                #self.sp = 1/(1+e**(-1*self.sp))
                if self.sp < 0:
                    self.sp = 0
                else:
                    self.sp = 1
                print("La salida es:" + repr(self.sp))