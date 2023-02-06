#Challenge 1
i = 0
list = []
list_add = []
userInput = input("Input: ")
for c in userInput:
    list.append(c)
    c = 0
for c in userInput:
    print(c)
#    c += 1
    if list == 1:
        i += 1
        if i == len(userInput):
            print("Output: True")
    else:
        print("Output: False")
        #break