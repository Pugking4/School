#Challenge 1
i = 0
list = []
fail = 0
userInput = input("Input: ")
for c in userInput:
    list.append(c)
for c in userInput:
    x = c
    i = 0
    for c in userInput:
        #print(x + c) #debug
        if x == c:
            fail += 1
            #print("fail") #debug
        else:
            i += 1
            #print(i) #debug
    if i == 0:
        print("True")
#print(f"fail is at {fail}") #debug
#print(f"fail thresh is {len(list)+1}") #debug
if fail >= len(list)+1:
    print("False")
else:
    print("True")