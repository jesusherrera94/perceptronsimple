from training.perceptron import Perceptron
from connection.connection import connection

trainOR = '{"table":[{"in":[0,0],"y":0},{"in":[0,1],"y":1},{"in":[1,0],"y":1},{"in":[1,1],"y":1}]}'
trainAND = '{"table":[{"in":[0,0],"y":0},{"in":[0,1],"y":0},{"in":[1,0],"y":0},{"in":[1,1],"y":1}]}'
trainXOR = '{"table":[{"in":[0,0],"y":0},{"in":[0,1],"y":1},{"in":[1,0],"y":1},{"in":[1,1],"y":0}]}'
print("OR")
perceptronOR = Perceptron(trainOR, 10, 1000)
perceptronOR.initializeW()
perceptronOR.training()
print("AND")
perceptronAND = Perceptron(trainAND, 45, 1000)
perceptronAND.initializeW()
perceptronAND.training()
print("XOR")
perceptronXOR = Perceptron(trainXOR, 100, 1000)
perceptronXOR.initializeW()
perceptronXOR.training()

insert = connection()
insert.pushDB({"AND":perceptronAND.getWeight(),"OR":perceptronOR.getWeight(),"XOR":perceptronXOR.getWeight()})
