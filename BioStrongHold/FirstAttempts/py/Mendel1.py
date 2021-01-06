(k,m,n)=input("please enter the populations with spaces:").split()

k=int(k)
m=int(m)
n=int(n)

def mendel(x,y,z):
    totalPop=x+y+z
    domProb=0
    homoDom=(x/(totalPop*(totalPop-1)))*(totalPop-1)
    heteroDom=(y/(totalPop*(totalPop-1)))*(x+(y-1)*0.75+z*0.5)
    homoRec=(z/(totalPop*(totalPop-1)))*(x+y*0.5)
    domProb=(homoDom+heteroDom+homoRec)
    return domProb

outVal = mendel(k,m,n)
print(outVal) 
