inpPath = input("please input your input file path:")

f=open(inpPath,"r")
outFile=open("evenOut.txt", "w+")

f1 = f.readlines()
f.close()
i=1
for x in f1:
    if i%2 == 0:
        outFile.write(x)
    i=i+1
outFile.close()
