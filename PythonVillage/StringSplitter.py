

theMessage = input("please enter the string:")
a,b,c,d = input("enter indices, space delimited:").split()

a=int(a)
b=int(b)
c=int(c)
d=int(d)
found1=""
found2=""

for i in range(a,b+1):
    found1 = found1 + theMessage[i]
for j in range(c,d+1):
    found2 = found2 + theMessage[j]

print(found1)
print(found2)
