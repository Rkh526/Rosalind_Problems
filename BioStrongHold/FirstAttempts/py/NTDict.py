inputStr=input("Enter the DNA string to start:")

myDict={}

for nt in list(inputStr):
    if nt in myDict:
        myDict[nt] += 1
    else:
        myDict[nt] = 1
for key, value in myDict.items():
    print (key,value)


