with open("multiply.txt") as f:
    for line in f:
        line=line.strip("\n")
        line=line.split("|")
        x,y=[x.split() for x in line]
        someAr=[]
        for num in range(len(x)):
            someAr.append(str(int(x[num])*int(y[num])))
        print " ".join(someAr)
        someAr=[]
