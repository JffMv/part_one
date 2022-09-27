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


if __name__=="__main__":
    problability(,)