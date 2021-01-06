
a,b=input("Enter your numbers below 10000:").split()
a=int(a)
b=int(b)
oddSum=0
#check is a is even
if a%2 == 0:
    oVal = a+1
else:
    oVal = a

while oVal <= b:
    oddSum = oddSum + oVal
    oVal = oVal + 2
print(oddSum)
