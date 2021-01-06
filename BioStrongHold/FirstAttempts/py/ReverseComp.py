inputDNA = input("please input the strand to get the reverse comp:")

compOut=[]

def ntComp(argument):
    switcher = {
            'A':'T',
            'T':'A',
            'C':'G',
            'G':'C'
    }
    
    return switcher.get(argument,"nothing")

for nt in reversed(list(inputDNA)):
    compOut.append(ntComp(nt))

fullComp=''.join(compOut)
print(fullComp)
