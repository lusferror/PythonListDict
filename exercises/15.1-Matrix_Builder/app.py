#Import random

#Create the function below:
def matrixBuilder(num):
    array1=[]
    for i in range(num):
        arra2=[]
        for j in range(num):
            arra2.append(1)
        array1.append(arra2)
    return array1

print(matrixBuilder(3))