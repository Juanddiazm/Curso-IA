import numpy as np
import random
FACTOR_TO_CONVERT = 2 / 255
CROSS_LINKING_PARAMETER = 0.8
MUTATION_PARAMETER=0.01



def funtion(x):
    return 1 - (x * x)


def getRangeValue(x):
    return (FACTOR_TO_CONVERT * x) - 1
def stopAlgoritm(sum,theBest ):
    if (len(sum) < 3):
        return True
    #if(sum[len(sum)-1]==sum[len(sum)-2] and sum[len(sum)-3]==sum[len(sum)-2]):
     #   return False
    #if (theBest[len(theBest) - 1] == theBest[len(theBest) - 2] and theBest[len(theBest) - 3] == theBest[len(theBest) - 2]):
    #   return False
    if(sum[len(sum)-1]>3.9999):
        return False
    return True

def geneticAlgoritmEx( file):
    inicialPoblation = (["10010100", "10010001", "00101001", "01000101"])
    sum=[]
    theBest=[]
    generation = 1
    acumulateProbability, sumFuntion, best = generateTable(inicialPoblation, file,generation)
    poblation = inicialPoblation
    sum.append(sumFuntion)
    theBest.append(best)
    while(stopAlgoritm(sum, theBest)):

        file.write(";PASO 2;;;;;" + "\n")
        correctPair = False
        realPairs = []
        while (not correctPair):
            correctPair, realPairs = pairing(acumulateProbability, file)
        file.write(";;;;;;" + "\n")
        file.write(";PASO 3;Pc = 0.8;;;;" + "\n")
        nPoblation = []
        nPoblation.append(poblation[0])
        nPoblation.append(poblation[1])
        nPoblation.append(poblation[2])
        nPoblation.append(poblation[3])

        xPoblation = cross_linking(nPoblation, realPairs, file)
        file.write(";;;;;;" + "\n")
        file.write(";PASO 4;Pm = 0.3;;;;" + "\n")
        poblation=  mutation(xPoblation, file)
        generation = generation+1
        acumulateProbability, sumFuntion, best = generateTable(poblation, file , generation)
        sum.append(sumFuntion)
        theBest.append(best)


# Is necesary that file is inicitializate
def generateTable(poblation, file, gen):
    sum = 0
    media = 0
    best = 0

    binPoblation = []
    for x in range (0,4):
        binPoblation.append(int(poblation[x],2))

    # Value in decimal
    realValues = []
    for x in range(0, len(binPoblation)):
        realValues.append(int(binPoblation[x]))


    # Value real
    rangeValues = []
    for x in range(0, len(realValues)):
        rangeValues.append(getRangeValue(realValues[x]))



    # Funtion values
    funtionValues = []
    for x in range(0, len(rangeValues)):
        funtionValues.append(funtion(rangeValues[x]))

    for x in range(0, len(funtionValues)):
        sum = sum + funtionValues[x]

    media = np.average(funtionValues)
    best = np.max(funtionValues)


    # Probability
    probability = []
    for x in range(0, len(funtionValues)):
        probability.append((funtionValues[x]) / sum)



    # Acumulate probability
    acumulateProbability = []
    varAcumulate = 0
    for x in range(0, len(probability)):
        varAcumulate = varAcumulate + probability[x]
        acumulateProbability.append(varAcumulate)



    file.write(";PASO 1;;Generacion:"+str(gen)+";;;" + "\n")
    file.write("ID;Poblacion inicial;x;Valor real;f(x);Probabilidad de selección;Probabilidad acumulada"+ "\n")
    for x in range(0, len(poblation)):
        file.write(str(x+1)+";"+poblation[x]+";"+str(realValues[x])+";"+str(rangeValues[x])+";"+str(funtionValues[x])+";"+str(probability[x])+";"+str(acumulateProbability[x])+ "\n")

    sumFuntion=0
    for x in range(0, len(funtionValues)):
        sumFuntion = sumFuntion + funtionValues[x]

    maxFuntion= np.max(funtionValues)
    file.write(";;;Suma;"+format(sumFuntion)+";;"+ "\n")
    file.write(";;;Mejor;"+str(maxFuntion)+";;"+ "\n")
    file.write(";;;;;;"+ "\n")

    return acumulateProbability, sumFuntion, maxFuntion


def pairing(acumulateProbability, file):
    randomNumbers =[]
    for x in range(0, 4):
        randomNumbers.append(random.random())
    numbersSelected=[]
    for x in range(0,4):

        if(randomNumbers[x]<=acumulateProbability[3] and randomNumbers[x]>acumulateProbability[2]):
            numbersSelected.append(4)
        elif(randomNumbers[x]<=acumulateProbability[2] and randomNumbers[x]>acumulateProbability[1]):
            numbersSelected.append(3)
        elif (randomNumbers[x] <= acumulateProbability[1] and randomNumbers[x] > acumulateProbability[0]):
            numbersSelected.append(2)
        elif (randomNumbers[x] <= acumulateProbability[0]):
            numbersSelected.append(1)

    file.write(";Generar 4 numeros aleatorios entre [0,1];"+ str(randomNumbers[0]) +";"+ str(randomNumbers[1]) +";"+str(randomNumbers[2])+";"+ str(randomNumbers[3])+";"+ "\n")
    file.write(";Individuos seleccionados;"+ str(numbersSelected[0]) +";"+ str(numbersSelected[1]) +";"+str(numbersSelected[2])+";"+ str(numbersSelected[3])+";"+ "\n")

    #verify that there are no 3 equal values
    for x in range(0,4):
        count =0
        for y in range(0,4):
            if(x!=y):
                if(numbersSelected[x]==numbersSelected[y]):
                    count= count + 1
        if(count>1):
            file.write(";Se esta seleccionando 3 veces el mismo individuo, es necesario repetir;;;;;" + "\n")
            return False, None


    for x in range(0, 4):
        copyNumbersSelect = numbersSelected.copy()
        count = 0
        for y in range(0, 4):
            if (x != y):
                if (numbersSelected[x] == numbersSelected[y]):
                    count = count + 1
        if (count == 1):
            copyNumbersSelect.remove(numbersSelected[x])
            copyNumbersSelect.remove(numbersSelected[x])

            if(copyNumbersSelect[0]==copyNumbersSelect[1]):
                file.write(";Se produciran dos parejas iguales, es necesario repetir;;;;;" + "\n")
                return False, None


    diferentsElements= False
    realPairs = []
    while(not diferentsElements):
        realPairs.clear()
        realPairs = randomPair(numbersSelected)
        # Verify that there are not pairs with 2 elements equals
        diferentsElements= True
        for x in range(0, 3):
            if (realPairs[x] == realPairs[x + 1]):
                diferentsElements = False

    file.write(";Parejas seleccionadas:;"+ str(realPairs[0]) +"y"+ str(realPairs[1]) +";"+str(realPairs[2])+"y"+ str(realPairs[3])+";;;"+ "\n")

    return True, realPairs


def randomPair(numbersSelected):
    index= [0,1,2,3]
    indexPairs =[]
    pairs = []
    for x in range(0,4):
        select= random.choice(index)
        indexPairs.append(select)
        index.remove(select)
    #Form pairs
    for x in range(0, 4):
        pairs.append(numbersSelected[indexPairs[x]])

    return pairs

def cross_linking(poblation, realPairs, file):
    randomNumbers = []
    crossingValue = []
    for x in range(0, 2):
        randomNumbers.append(random.random())

    file.write(";Para la pareja "+str(realPairs[0])+"y" +str(realPairs[1])+" se genera; "+ str(randomNumbers[0])+";;;;"+ "\n")
    file.write(";Para la pareja " + str(realPairs[2]) + "y" + str(realPairs[3]) + " se genera; " + str(randomNumbers[1]) + ";;;;"+ "\n")

    if(randomNumbers[0]<CROSS_LINKING_PARAMETER):
        crossingValue.append(True)
    else:
        crossingValue.append(False)

    if(randomNumbers[1]<CROSS_LINKING_PARAMETER):
        crossingValue.append(True)
    else:
        crossingValue.append(False)

    firtsPartNextGen = []
    secondPartNextGen = []
    pair1= []
    pair2=[]
    pair1.append(byteToStringFormat(poblation[realPairs[0]-1]))
    pair1.append(byteToStringFormat(poblation[realPairs[1]-1]))
    pair2.append(byteToStringFormat(poblation[realPairs[2]-1]))
    pair2.append(byteToStringFormat(poblation[realPairs[3]-1]))
    if(crossingValue[0]):
        file.write(";Como " + str(randomNumbers[0]) + " es menor que Pc se entrecruza la pareja 1" +";;;;;"+ "\n")
        p = []
        p.append(realPairs[0])
        p.append(realPairs[1])
        firtsPartNextGen = cross(poblation, p)

    else :
        file.write(";Como " + str(randomNumbers[0]) + " es mayor que Pc NO se entrecruza la pareja 1" + ";;;;;"+ "\n")
        firtsPartNextGen = pair1

    if (crossingValue[1]):
        file.write(";Como " + str(randomNumbers[1]) + " es menor que Pc se entrecruza la pareja 2" + ";;;;;"+ "\n")
        p2 = []
        p2.append(realPairs[2])
        p2.append(realPairs[3])
        secondPartNextGen = cross(poblation, p2)
    else:
        file.write(";Como " + str(randomNumbers[1]) + " es mayor que Pc NO se entrecruza la pareja 2" + ";;;;;"+ "\n")
        secondPartNextGen = pair2

    file.write(";Nueva generacion:;"+str(firtsPartNextGen[0])+";;;;"+ "\n")
    file.write(";;" + str(firtsPartNextGen[1]) + ";;;;"+ "\n")
    file.write(";;" + str(secondPartNextGen[0]) + ";;;;"+ "\n")
    file.write(";;" + str(secondPartNextGen[1]) + ";;;;"+ "\n")

    nPoblation = []
    nPoblation.append(firtsPartNextGen[0])
    nPoblation.append(firtsPartNextGen[1])
    nPoblation.append(secondPartNextGen[0])
    nPoblation.append(secondPartNextGen[1])

    return nPoblation

#Enter the two individuals who will join
def cross(poblation, realPairs):
    pointCut= random.randint(1,7)
    file.write(";Punto de corte:;"+str(pointCut)+";;;;"+ "\n")
    individualA = byteToStringFormat(poblation[realPairs[0]-1])
    individualB = byteToStringFormat(poblation[realPairs[1]-1])

    firtsA = individualA[0:pointCut]
    firtsB = individualB[0:pointCut]
    secondA = individualA[pointCut:]
    secondB = individualB[pointCut:]

    individualA = firtsA + secondB +""
    individualB = firtsB + secondA +""
    nextGeneration = []
    nextGeneration.append(individualA)
    nextGeneration.append(individualB)
    return nextGeneration

#c = binary
def byteToStringFormat( c):
    numZeroToAdd = 8 - (len(str(c))-2)
    zeroToAdd = ""
    for x in range (0, numZeroToAdd):
        zeroToAdd = zeroToAdd + "0"

    nc= str(c).replace("0b", zeroToAdd)
    return nc

def gen20number():
    randomNumbers = []
    mutation = []
    for x in range(0, 20):
        randomNumbers.append(random.random())
        if(randomNumbers[x]<MUTATION_PARAMETER):
            mutation.append(x)
    return mutation

def mutation(poblation, file):
    array20Random = gen20number()

    mutIndividual1 = []
    mutIndividual2 = []
    mutIndividual3 = []
    mutIndividual4 = []

    for x in range(0, len(array20Random)) :
        if(array20Random[x] >= 24 and array20Random[x] < 32):
            mutIndividual4.append(array20Random[x]-24)
        elif(array20Random[x] >= 16 and array20Random[x] < 24):
            mutIndividual3.append(array20Random[x]-16)
        elif (array20Random[x]>=8 and array20Random[x]<16):
            mutIndividual2.append(array20Random[x]-8)
        elif (array20Random[x]<8):
            mutIndividual1.append(array20Random[x])

    if(len(mutIndividual1)>0):
        file.write(";Han ocurrido mutaciones en el individuo 1 en los genes:;"+ str(mutIndividual1)  +";;;;"+"\n")
    else:
        file.write(";No han ocurrido mutaciones en el individuo 1;;;;;"+"\n")

    if (len(mutIndividual2) > 0):
        file.write(";Han ocurrido mutaciones en el individuo 2 en los genes:;" + str(mutIndividual2) + ";;;;" + "\n")
    else:
        file.write(";No han ocurrido mutaciones en el individuo 2;;;;;"+"\n")

    if (len(mutIndividual3) > 0):
        file.write(";Han ocurrido mutaciones en el individuo 3 en los genes:;" + str(mutIndividual3) + ";;;;" + "\n")
    else:
        file.write(";No han ocurrido mutaciones en el individuo 3;;;;;"+"\n")

    if (len(mutIndividual4) > 0):
        file.write(";Han ocurrido mutaciones en el individuo 4 en los genes:;" + str(mutIndividual4) + ";;;;" + "\n")
    else:
        file.write(";No han ocurrido mutaciones en el individuo 4;;;;;"+"\n")


    nPoblation = []
    nPoblation.append(changeGen(poblation[0], mutIndividual1 ))
    nPoblation.append(changeGen(poblation[1], mutIndividual2))
    nPoblation.append(changeGen(poblation[2], mutIndividual3))
    nPoblation.append(changeGen(poblation[3], mutIndividual4))

    file.write(";Los nuevos individuos son:;" + str(nPoblation[0]) + ";;;;" + "\n")
    file.write(";;" + str(nPoblation[1]) + ";;;;" + "\n")
    file.write(";;" + str(nPoblation[2]) + ";;;;" + "\n")
    file.write(";;" + str(nPoblation[3]) + ";;;;" + "\n")

    return nPoblation

def changeGen( individual, mutIndividua):
    arrayIndiviual = list(str(individual))
    for x in range (0, len(mutIndividua)):
        arrayIndiviual[mutIndividua[x]] =  invert(arrayIndiviual[mutIndividua[x]])
    nIndividual =""
    for x in range (0, len(arrayIndiviual)):
        nIndividual = nIndividual+ arrayIndiviual[x];

    return nIndividual

def invert( n ):
    if(n == "0"):
        return "1"
    else:
        return "0"

file = open("entrega.txt", "w")
geneticAlgoritmEx(file)
