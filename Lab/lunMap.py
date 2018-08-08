lunFile="/github/pythonBeginner/Config/LUN"

#out=f.readlines()
#myout=[x.strip() for x in out]

with open(lunFile, "r") as fd:
    for line in fd:
        line = line.strip()
        print ("3"+line)


