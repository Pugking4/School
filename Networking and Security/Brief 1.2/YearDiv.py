userInput = int(input("Year: "))
year4 = userInput%4
year100 = userInput%100
year400 = userInput%400

if year4 == 0 and year100 == 0 and year400 == 0:
     print("True")
elif year4 == 0 and year100 != 0:
    print("True")
else:
    print("False")
