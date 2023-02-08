#Challenge 1
i = 0
list = []
userInput = input("Input: ")
for c in userInput:
    list.append(c)
for c in userInput:
    x = list.count(c)
    if x == 1:
        i += 1
        if i == len(userInput):
            print("Output: True")
    else:
        print("Output: False")
        break