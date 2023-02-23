#userInput = input("Input: ")
userInput = "aabcccaaaa"
count = 0
string = ""
for_count = -1

def cooler_len(userStr):
    counter = 0
    for i in userStr:
        counter += 1
    return counter

#print(len2(userInput))

for x in userInput:
    count = 0
    for_count += 1
    for y in userInput:
        if x == y:
            count += 1
        else:
            print("break")
            break

    #if x not in string:
    #    string += x + str(count)
    print(f"for = {for_count*2}, len = {cooler_len(string)}, x = {x}, y = {y}")
    print(string)
    if cooler_len(string) == for_count*2:
        for_count = 0

    if cooler_len(string) != 0:
        print(f"for_len = {string[for_count*2]}")


    if cooler_len(string) != 0:
        if x != string[for_count*2]:
            string += x + str(count)
    else:
        string += x + str(count)

print(string)


#if cooler_len(string) < cooler_len(userInput):
#    print(string)
#else:
#    print(userInput)


#0, 1, 2, 3
#0, 2, 4, 6,
#a, 6, b, 2, c, 5, a, 2