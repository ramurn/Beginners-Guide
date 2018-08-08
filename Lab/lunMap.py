lunFile="/github/pythonBeginner/Config/LUN"

#out=f.readlines()
#myout=[x.strip() for x in out]

def mpth(a,w):
    print ("multipath {\n\talias ",a,"\n\twwid ",w,"\n\t}")

with open(lunFile, "r") as fd:
    for line in fd:
        line = line.strip()
        out=line.split()
        a=out[1]
        w=out[0]
        mpth(a,w)



