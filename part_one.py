import numpy as np

def module(c1):

    number1 = c1[0]**2
    number2 = c1[1]**2
    operation = (number1 + number2)** 1/2
    return operation

def norm_of_Vector(array):
    row = len(array)
    column = len(array[0])
    result = 0

    for i in range(row):
        for j in range(column):
            result += array[i][j][0]**2+array[i][j][1]**2
    return (result**1/2)

def problability (array, number):
    p = (module(array[number])**2)/(norm_of_Vector(array))**2
    print (p)
    return(p)

def posibily_probabilty(posicion, index):
    estados = [[(0,1),(1,0)],[(0,-1),(1,0)],[(1,0),(1,0)],[(-1,0),(1,0)],[(0,0),(1,0)],[(1,0),(0,0)]]
    result = []
    for i in range((index*2)-2,index*2):
        if problability(posicion,estados[i])!= 0.0:
            result = result + estados[i]
    return result

def probabilidadValoresPropios(posicion, index):
    matrices = [[[(1,0),(0,0)],[(0,0),(-1,0)]],[[(0,0),(0,-1)],[(0,1),(0,0)]],[[(0,0),(1,0)],[(1,0),(0,0)]]]
    values_propies = []
    aux = posibily_probabilty(posicion, index)
    pro= []
    answer = 0
    for i in range(3):
        values,no = np.linalg.eig(matrices[i])
        values_propies+=values
    for i in range(len(aux)):
        pro+=problability(posicion, aux[i])
    for i in range(2):
        answer+=(problability[i]*values_propies[index][i])
    return answer


if __name__=="__main__":
    problability(,)