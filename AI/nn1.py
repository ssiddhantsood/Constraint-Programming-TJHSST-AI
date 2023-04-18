import sys;args = sys.argv[1:]
import math

def setGlobals():
    global TF, inputs
    TF = args[1]
    inputs = list(map(float, args[2:]))

def readInp():
    with open(args[0]) as r:
        lines = r.readlines()
        weights = [list(map(float, line.strip().split())) for line in lines]
    return weights

def dotProduct(w1, w2):
    return sum(val1 * val2 for val1, val2 in zip(w1, w2))

def switch(x, layer):
    if layer == "T1":
        return x
    elif layer == "T2":
        return x if x > 0 else 0
    elif layer == "T3":
        return 1.0 / (1.0 + math.exp(-x))
    elif layer == "T4":
        return (2.0 / (1.0 + math.exp(-x))) - 1.0


def calcV(inputs, weightLine, TF):
    numInputs = len(inputs)
    numCells = int(len(weightLine) / numInputs)
    indexList = [(weightLine[k * numInputs:k * numInputs + numInputs]) for k in range(numCells)]
    cellList = [switch(dotProduct(inputs, k), TF) for k in indexList]
    
    return cellList

def feedForward(data, weightList, TF):
    inputs = data
    for layer in range(len(weightList) - 1):
        inputs = calcV(inputs, weightList[layer], TF)
    finalWeights = weightList[len(weightList) - 1]
    outputs = [inputs[k] * finalWeights[k] for k in range(len(inputs))]
    return outputs

def main():
    global TF, inputs
    setGlobals()
    weights = readInp()
    output = feedForward(inputs, weights, TF)
    print(" ".join(map(str, output)))

if __name__ == "__main__":
    main()

#Siddhant Sood, 7, 2024
