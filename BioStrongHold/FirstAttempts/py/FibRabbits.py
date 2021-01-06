
(a,b)=input("input your number of months and offspring per pair:").split()

numMonths=int(a)
numOspring=int(b)

def fibPairs(mon,ospring):
    fibCur=1
    fibPrev=1
    for i in range(2,mon):
        fibNext = fibCur + ospring*fibPrev
        fibPrev = fibCur
        fibCur = fibNext
    return fibNext

totalPairs=fibPairs(numMonths,numOspring)
print(totalPairs)


