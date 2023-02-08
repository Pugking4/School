
vowels = ['a', 'e', 'i', 'o', 'u']
vowelCheck = 0
userInput = input("Text: ")
#print(len(vowels))
for i in range(len(vowels)):
    if vowels[i] in userInput:
        print("You have entered a vowel.")
        vowelCheck = 1
        break
if vowelCheck == 0:
    print("You did not enter a vowel.")