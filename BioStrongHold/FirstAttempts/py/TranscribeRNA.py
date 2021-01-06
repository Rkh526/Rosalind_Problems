
inputString=input("please enter the dna string to transcribe:")

outList=""

for char in list(inputString):
    if char == 'T':
        char = 'U'
    outList = outList + str(char)

print(outList)
