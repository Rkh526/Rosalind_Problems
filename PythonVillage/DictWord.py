inputStr=input("Enter the string to start:")

myDict={}

for word in inputStr.split(' '):
    if word in myDict:
        myDict[word] += 1
    else:
        myDict[word] = 1
for key, value in myDict.items():
    print (key,value)


