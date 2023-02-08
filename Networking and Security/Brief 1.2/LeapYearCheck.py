userInput = int(input("Year: "))
year4 = userInput%4
year100 = userInput%100
year400 = userInput%400

if year4 == 0 and year100 == 0 and year400 == 0:
     print(f"{userInput} is a leap year.")
elif year4 == 0 and year100 != 0:
    print(f"{userInput} is a leap year.")
else:
    print(f"{userInput} is not a leap year.")