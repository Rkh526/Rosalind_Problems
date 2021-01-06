s = list(input("input main string: "))
t = list(input("input sub string: "))

subLocs=[]
fullSub=1
for i in range(0,len(s)):
    left=len(s)-i
    if s[i] == t[0] and len(t)<left:
        for j in range(0,len(t)):
            if s[i+j] != t[j]:
                fullSub=0
        if fullSub:
            subLocs.append(i+1)
        fullSub = 1
for x in subLocs:
    print(x)

