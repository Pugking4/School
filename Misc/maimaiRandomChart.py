import random

def addVertBar(filename):
    filepath = f"Misc\\maimaiRandomChartData\\{filename}"
    with open(filepath,encoding="utf8") as f:
        lines = f.read().splitlines()

    with open(filepath, "w",encoding="utf8") as f:
        for line in lines:
            f.write(line + "|")

level13 = 0
level13_list = []
level13plus = 0
level13plus_list = []
level14 = 0
level14_list = []
level14plus = 0
level14plus_list = []
allmas = 0
allmas_list = []
allremas = 0
allremas_list = []
allremaslevel = 0
allremaslevel_list = []
allmaslevel = 0
allmaslevel_list = []

userInputFormat = input("Do you need to format the data? ")
if userInputFormat == "Yes" or userInputFormat == "Y" or userInputFormat == "1":
    userInputFormatFN = input("What's the filename? ")
    addVertBar(userInputFormatFN)

with open("Misc\\maimaiRandomChartData\\13+List.txt",encoding="utf8") as f:
    level13plus = f.read()
with open("Misc\\maimaiRandomChartData\\14List.txt",encoding="utf8") as f:
    level14 = f.read()
with open("Misc\\maimaiRandomChartData\\14+List.txt",encoding="utf8") as f:
    level14plus = f.read()
with open("Misc\\maimaiRandomChartData\\AllMasList.txt",encoding="utf8") as f:
    allmas = f.read()
with open("Misc\\maimaiRandomChartData\\AllReMasList.txt",encoding="utf8") as f:
    allremas = f.read()
with open("Misc\\maimaiRandomChartData\\AllReMasLevelList.txt",encoding="utf8") as f:
    allremaslevel = f.read()
with open("Misc\\maimaiRandomChartData\\AllMasLevelList.txt",encoding="utf8") as f:
    allmaslevel = f.read()

level13plus_list = level13plus.strip("|").split("|")
level14list = level14.strip("|").split("|")
level14plus_list = level14plus.strip("|").split("|")
allmas_list = allmas.strip("|").split("|")
allremas_list = allremas.strip("|").split("|")
allremaslevel_list = allremaslevel.split("|")
allmaslevel_list = allmaslevel.split("|")

userInputLevel = input("What level do you want to play? ")
if userInputLevel == "13+":
    rand = random.randint(0, len(level13plus_list))
    print(f"You should play '{level13plus_list[rand]}'")
elif userInputLevel == "14":
    rand = random.randint(0, len(level14_list))
    print(f"You should play '{level14_list[rand]}'")
elif userInputLevel == "14+":
    rand = random.randint(0, len(level14plus_list))
    #print(rand) debug
    #print(len(level14plus_list)) debug
    print(f"You should play '{level14plus_list[rand]}'")
elif userInputLevel == "All ReMas":
    rand = random.randint(0, len(allremas_list))
    print(f"You should play '{allremas_list[rand]}' which is level {allremaslevel_list[rand]}")
elif userInputLevel == "All Mas":
    rand = random.randint(0, len(allmas_list))
    print(f"You should play '{allmas_list[rand]}' which is level {allmaslevel_list[rand]}")