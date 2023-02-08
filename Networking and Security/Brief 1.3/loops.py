def prac1():
    for i in range(10, 0, -1):
        print(i)

def prac2():
    even = 0
    for i in range(1, 11):
        if i%2 == 0:
            even += 1
    print(f"There are {even} even numbers.")

def prac3():
    sum = 0
    for i in range(1, 11):
        sum += i**2
    print(sum)

def prac4():
    for i in range(20, 31):
        print(i)

def prac5():
    x = 0
    for i in range(0, 101):
        x += i
    print(x)

def prac6():
    for i in range(1, 11):
        if i > 5:
            continue
        print(i)

def prac7():
    x = 0
    for i in range(1, 11):
        if i == 6:
            continue
        if i%2 != 0:
            continue
        x += i
    print(x)

def prac8():
    x = 0
    for i in range(1, 21):
        if i == 5:
            continue
        if i%2 != 1:
            continue
        x += i
    print(x)

def prac9():
    i = 1
    while i <= 10:
        print(i)
        i += 1

def prac10():
    i, x = 0, 0
    test = "False"
    while test == "False":
        i += 1
        if i == 6:
            continue
        elif i%2 != 0:
            continue
        elif i == 10:
            test = "True"
        x += i
    print(x)

def prac11():
    i = 0
    odd = 0
    userInput = str(input("Numbers: "))
    while i < len(userInput):
        userInt = userInput[i]
        print(userInt)
        if int(userInt)%2 == 1:
            odd += 1
        i += 1
    print(f"There is {odd} odd numbers.")

def prac12():
    i = 0
    sum = 0
    while i <= 5:
        i += 1
        if sum <= 25:
            sum += i**2
    print(sum)

def prac13():
    i = 1
    sum = 1
    userInput = int(input("Number: "))+1
    if userInput < 0:
        print("Do not use negative numbers.")
    numRange = range(userInput)
    while i < userInput:
        sum = sum * numRange[i]
        i += 1
    print(f"Factorial: {sum}")

#functionsStr = ["prac1","prac2"]
#functions = [prac1(),prac2()]
#for i in range(len(functions)):
#    print(f"Function: {functionsStr[i]}")
#    print(functions[i])