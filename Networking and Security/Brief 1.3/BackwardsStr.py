x = 0 #declaring x as a variable with the value of 0
backwardsStr = "" #declaring backwardsStr as a variable with the string ""
userInput = input("Line: ") #collecting user input and assigning it userInput
for i in range(len(userInput)): #loops for however long userInput is #range creates a range where it starts at 0 and goes to whatever value len(userInput) is
  x += -1 #adds -1 to x everytime the loop runs
  backwardsStr = backwardsStr + userInput[x] #adds each character backwards using x in the square bracket which is always a negative so its counting backwards through the string
print(backwardsStr) #prints the finished string after the loop has completed