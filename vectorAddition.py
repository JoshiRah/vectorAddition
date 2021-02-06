def pickUpVectorA():
    print('| Vektor A |')
    while True:
        try:
            x = (int(input("Ax: ")))
            break
        except:
            print('\nBitte eine ganze Zahl verwenden!\n')
    while True:
        try:
            y = (int(input("Ay: ")))
            break
        except:
            print('\nBitte eine ganze Zahl verwenden!\n')
    while True:
        try:
            z = (int(input("Az: ")))
            break
        except:
            print('\nBitte eine ganze Zahl verwenden!\n')

    vectorA = []

    vectorA.append(x)
    vectorA.append(y)
    vectorA.append(z)
    print('\nVektor A: ', vectorA)
    return vectorA

def pickUpVectorB():
    print('\n| Vektor B |')
    while True:
        try:
            x = (int(input("Bx: ")))
            break
        except:
            print('\nBitte eine ganze Zahl verwenden!\n')
    while True:
        try:
            y = (int(input("By: ")))
            break
        except:
            print('\nBitte eine ganze Zahl verwenden!\n')
    while True:
        try:
            z = (int(input("Bz: ")))
            break
        except:
            print('\nBitte eine ganze Zahl verwenden!\n')

    vectorB = []

    vectorB.append(x)
    vectorB.append(y)
    vectorB.append(z)
    print('\nVektor B: ', vectorB)
    return vectorB

print('Vektor-Addition via Python: \n')

vectorA = pickUpVectorA()
vectorB = pickUpVectorB()

AxBx = vectorA[0] + vectorB[0]
AyBy = vectorA[1] + vectorB[1]
AzBz = vectorA[2] + vectorB[2]

newVector = []

newVector.append(AxBx)
newVector.append(AyBy)
newVector.append(AzBz)

if vectorA[0] == 0 and vectorA[1] == 0 and vectorA[2] == 0 or vectorB[0] == 0 and vectorB[1] == 0 and vectorB[2] == 0:
    print('\n-| Einer der Beiden vektoren, oder beide sind ein Punkt! Die Addition funktioniert nur zwischen zwei Vektoren! |-')
else:
    print('\n-| Das Ergebnis lautet: ', newVector, '|-')