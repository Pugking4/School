#Challenge 2
userInput = input("Input: ")
newList = []
userList = list(userInput)
for i in userList:
    if i == " ":
        newList.append("%20")
        continue
    newList.append(i)
newList = "".join(newList)
print(f"Output: {newList}")