import math

class Vector():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def sumOfVector(vector):
    squareSum = vector.x ** 2 + vector.y ** 2 + vector.z ** 2
    vectorSum = math.sqrt(squareSum)
    return vectorSum

def add(vector_A, vector_B):
    sumx = vector_A.x + vector_B.x
    sumy = vector_A.y + vector_B.y
    sumz = vector_A.z + vector_B.z
    output = sumx, sumy, sumz
    return output

def scalarProduct(vector_A, vector_B):
    scalar = vector_A.x * vector_B.x + vector_A.y * vector_B.y + vector_A.z * vector_B.z
    return scalar

def angle(vector_A, vector_B):
    scalar = scalarProduct(vector_A, vector_B)
    sumA = sumOfVector(vector_A)
    sumB = sumOfVector(vector_B)
    cosPhi = scalar / (sumA * sumB)
    rad = math.acos(cosPhi)
    deg = rad * 180 / math.pi
    return deg

'''
Configure vectors here:
'''

vectorA = Vector(2,2,1)
vectorB = Vector(-1,-1,1)


'''
Output-area:
'''

print(angle(vectorA, vectorB))