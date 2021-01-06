s1 = input("input the first strand: ")
s2 = input("input the second strand: ")

hamDist=0

for i in range(len(s1)):
    if s1[i] != s2[i]:
        hamDist +=1

print(hamDist)
