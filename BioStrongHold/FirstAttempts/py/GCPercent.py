inpPath=input("Input path to FASTA formatted file: ")

f=open(inpPath,"r")
ftext= f.readlines()
f.close()

GCDict={}
theGC = 0
maxGC=0
totalNT=0

for l in ftext:
    if '>Rosalind' in l:
        RosFasta = l
        RosFasta = l.replace('>','')
        GCcount=0
        totalNT=0
    else :
        for char in list(l):
            if char == 'G' or char == 'C':
                GCcount += 1
                totalNT+=1
            if char == 'A' or char == 'T':
                totalNT+=1
            #totalNT+=1
        theGC = (GCcount/totalNT)*100
        GCDict[RosFasta] = theGC
    #print(GCcount)
    #print(totalNT)
v = list(GCDict.values())
k = list(GCDict.keys())
print(k[v.index(max(v))])

for key,value in GCDict.items():
    print(key,value)
