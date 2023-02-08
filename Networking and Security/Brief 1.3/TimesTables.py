userTimes =  int(input("Which times table do you want? "))
userStart = int(input("Where do you want to start? "))
userEnd = int(input("Where do you want to end? "))
#userTimes = 7 #debug
#userStart = 4 #debug
#userEnd = 12 #debug
x = 0
#print(userRange) #debug
for i in range(userStart,userEnd+1):
    if i == 0:
        continue
    x = userTimes*i
    print(f"{userTimes} * {i} = {x}")