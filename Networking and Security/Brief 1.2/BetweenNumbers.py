userInput = int(input("Number: "))
if userInput >= 0 and userInput <= 10:
    print(userInput)
    print("Your number is between 0 and 10.")
elif userInput >= 20 and userInput <= 30:
    print("Your number is between 20 and 30.")
else:
    print("Your number is not in any range specified.")