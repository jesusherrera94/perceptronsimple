from training.perceptron import Perceptron
from connection.connection import connection

inputs = '{"table":[{"in":[0,0]},{"in":[0,1]},{"in":[1,0]},{"in":[1,1]}]}'

dbExtracted = connection()
result = dbExtracted.getDB("-Luh2RGCkrEBcoTABzea")
print(result["OR"])

perceptron = Perceptron(inputs, None, None)
perceptron.runPerceptron(result["OR"])