import numpy as np
import torch as tc

def sigmoid(x):
    return 1/(1 + np.exp(-x))


def sigmoidDerivative(x):
    return x * (1 - x)


inputs = np.array([ [0,0,1],
                    [1,1,1],
                    [1,0,1],
                    [0,1,1]])
training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

print(inputs)
print(training_outputs)
weights = 2 * np.random.random((3, 1)) - 1

print("Pesos:")
print(weights)

for i in range(10000):
    inputLayer = inputs
    outputs = sigmoid(np.dot(inputLayer,weights))
    #calcular el error y re-ajustar los pesos
    error = training_outputs - outputs
    adjustments = error * sigmoidDerivative(outputs)

    weights += np.dot(inputLayer.T,adjustments)

print("Pesos despues de entrenar")
print(weights)
print("Salidas despues de entrenar")
print(outputs)