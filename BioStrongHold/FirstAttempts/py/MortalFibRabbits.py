
(a,b)=input("input your number of months and the rabbits lifespan:").split()

numMonths=int(a)
numLifeSpan=int(b)

def fibPairs(mon,lSpan):
    # Need to keep track of the ages more closely this time
    # Make a list to track of the numbers
    ageList = [0] * lSpan
    ageList[-1] = 1
    for i in range(1,mon):
        new_fibs = sum(ageList[:-1])
        ageList[:-1] = ageList[1:] # To age up the rabbits
        ageList[-1] = new_fibs
    return(sum(ageList))

totalPairsAlive=fibPairs(numMonths,numLifeSpan)
print(totalPairsAlive)


