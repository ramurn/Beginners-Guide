lunFile="/github/pythonBeginner/Config/LUN"


with open(lunFile, "r") as fd:
    for line in fd:
        line = line.strip()
        print ("3"+line)


