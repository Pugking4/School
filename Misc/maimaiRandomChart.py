import random

def addVertBar(filename):
    filepath = f"Misc\\maimaiRandomChartData\\{filename}"
    with open(filepath,encoding="utf8") as f:
        lines = f.read().splitlines()

    with open(filepath, "w",encoding="utf8") as f:
        for line in lines:
            f.write(line + "|")

level13plus = 0
level13plus_list = []
#print(level13plus_list)

userInputFormat = input("Do you need to format the data? ")
if userInputFormat == "Yes" or userInputFormat == "Y" or userInputFormat == "1":
    userInputFormatFN = input("What's the filename? ")
    addVertBar(userInputFormatFN)

with open("Misc\\maimaiRandomChartData\\13+List.txt",encoding="utf8") as f:
    level13plus = f.read()
level13plus_list = level13plus.split("|")

userInputLevel = input("What level do you want to play? ")
if userInputLevel == "13+":
    rand = random.randint(0, len(level13plus_list))
    print(f"You should play '{level13plus_list[rand]}'")