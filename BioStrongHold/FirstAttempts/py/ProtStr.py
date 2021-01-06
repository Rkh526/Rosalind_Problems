# Start by setting up RNA codon table
RNACodon = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L","UCU":"S","UCC":"S","UCA":"S","UCG":"S","UAU":"Y","UAC":"Y","UAA":"Stop","UAG":"Stop","UGU":"C","UGC":"C","UGA":"Stop","UGG":"W","CUU":"L","CUC":"L","CUA":"L","CUG":"L","CCU":"P","CCC":"P","CCA":"P","CCG":"P","CAU":"H","CAC":"H","CAA":"Q","CAG":"Q","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AUU":"I","AUC":"I","AUA":"I","AUG":"M","ACU":"T","ACC":"T","ACA":"T","ACG":"T","AAU":"N","AAC":"N","AAA":"K","AAG":"K","AGU":"S","AGC":"S","AGA":"R","AGG":"R","GUU":"V","GUC":"V","GUA":"V","GUG":"V","GCU":"A","GCC":"A","GCA":"A","GCG":"A","GAU":"D","GAC":"D","GAA":"E","GAG":"E","GGU":"G","GGC":"G","GGA":"G","GGG":"G"}


mRnaPath=input("please input path to the mRNA string to translate into a protein string: ")

f=open(mRnaPath,"r")
mRna=f.read()
f.close()

protStr = ''

for j in range(int(len(mRna)/3)):
    i=j*3
    codon=mRna[i]+mRna[i+1]+mRna[i+2]
    if codon in RNACodon:
        newAA = RNACodon[codon]
        if newAA != 'Stop':
            protStr+=RNACodon[codon]

fOut=open('protOut.txt',"w+")
fOut.write(protStr)
fOut.close

