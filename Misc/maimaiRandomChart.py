import random

def addVertBar(filename):
    filepath = f"Misc\\maimaiRandomChartData\\{filename}"
    with open(filepath,encoding="utf8") as f:
        lines = f.read().splitlines()

    with open(filepath, "w",encoding="utf8") as f:
        for line in lines:
            f.write(line + "|")
i = 0
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
#lists = ["level13plus_list","level14_list","level14plus_list","allmas_list","allmaslevel_list","allremas_list","allremaslevel_list"]
#file_lists = ["13+List.txt","14List.txt","14+List.txt","AllMasList.txt","AllMasLevelList.txt","AllReMasList.txt","AllReMasLevelList.txt"]

userInputFormat = input("Do you need to format the data? ")
if userInputFormat == "Yes" or userInputFormat == "Y" or userInputFormat == "1":
    userInputFormatFN = input("What's the filename? ")
    addVertBar(userInputFormatFN)

#while i < len(file_lists):
#    with open(f"Misc\\maimaiRandomChartData\\{file_lists[i]}",encoding="utf8") as f:
#        lists[i] = f.read()
#    #print(lists[i])
#    #print(file_lists[i])
#    print(i)
#    i += 1

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
level14_list = level14.strip("|").split("|")
level14plus_list = level14plus.strip("|").split("|")
allmas_list = allmas.strip("|").split("|")
allremas_list = allremas.strip("|").split("|")
allremaslevel_list = allremaslevel.split("|")
allmaslevel_list = allmaslevel.split("|")

#listlength = len(lists)
#i = 0
#print(f"{lists[2]} has {len(lists[2])} items")
#for listlength in lists:
#    print(f"{lists[i]} has {len(lists[i])} items")
#    print(i)
#    i += 1
#print(len(lists))
#print(len(level14plus_list))
#print(lists(0))

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
elif userInputLevel == "remas":
    rand = random.randint(0, len(allremas_list))
    print(f"You should play '{allremas_list[rand]}' which is level {allremaslevel_list[rand]}")
elif userInputLevel == "mas":
    rand = random.randint(0, len(allmas_list))
    print(f"You should play '{allmas_list[rand]}' which is level {allmaslevel_list[rand]}")
else:
    print("That is not a valid argument, please use 13+, 14, 14+, mas or remas.")