# This script will return the a consenus string and profile matrix
# for a given data set in FASTA format. 

import numpy as np
import pandas as pd

# Read in dataset from file
inpPath=input("Input path to FASTA formatted file: ")

f=open(inpPath,"r")
ftext=f.readlines()
f.close()

# Get the length of only the DNA string
dna1 = []
for line in ftext[1:]:
    if not line.lstrip().startswith('>'):
        dna1.append(line)
    else:
        break
dnaHold = "".join(x for x in dna1)
dna1 = dnaHold
dnaLen = len(dna1)
#print(dna1)
#print(dnaLen)
# We know the DNA strings are all of equal length so grab len at pos 1.
#dnaLen = len(list(ftext[1]))

pMat = np.zeros((4,dnaLen-1),dtype=int)

for l in ftext:
    if '>Rosalind' in l:
        pos = 0
    else:
        for char in list(l):
            if char =='A':
                pMat[0,pos] += 1
            elif char =='C':
                pMat[1,pos] += 1
            elif char =='G':
                pMat[2,pos] += 1
            elif char =='T':
                pMat[3,pos] += 1
            pos+=1



conStr = []
# Create a pandas dataframe with this info
profMat = pd.DataFrame(pMat, index=list('ACGT'))
maxValsIdx = profMat.idxmax()
print(pMat)
print(profMat)
conStr = ''.join([x for x in maxValsIdx.values])


f=open('conProfOut.txt',"w")
f.write(conStr)
f.write('\n')
f.close()
#f=open('conProfOut.txt',"ab")
#np.savetxt(f,profMat.values, fmt='%d', delimiter='\t',index='A:\tC:\tG:\tT:\t')
#f.close()
profMat.to_csv('conProfOut.txt', mode='a',sep='\t', header=False, index=True)
