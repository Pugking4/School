#NOTES 
#This is accurate up to the 2nd of February, 2023.

#Declaring variables
mDay = 0 
mmDay = 0
curYear = 2023
curDayPassed = 33 #how many days have passed in the current year
yDay = 0
jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

#Getting user input
name = input("What's your given name? ")
day = int(input("What day were you born on? "))
year = int(input("What year were you born in? "))
month = input("What month were you born in? ")

#Calculating whole years
yDay = (curYear-year-1)*365 #Calculates how many days have passed in whole years
#print(f"{yDay} days from years") #debugging

#Calculating birth year
if month == "jan":
    mDay = 0 + day - 1
elif month == "feb":
    mDay = jan + day - 1
elif month == "mar":
    mDay = jan + feb + day - 1
elif month == "apr":
    mDay = jan + feb + mar + day - 1
elif month == "may":
    mDay = jan + feb + mar + apr + day - 1
elif month == "jun":
    mDay = jan + feb + mar + apr + may + day - 1
elif month == "jul":
    mDay = jan + feb + mar + apr + may + jun + day - 1
elif month == "aug":
    mDay = jan + feb + mar + apr + may + jun + jul + day - 1
elif month == "sep":
    mDay = jan + feb + mar + apr + may + jun + jul + aug + day - 1
elif month == "oct":
    mDay = jan + feb + mar + apr + may + jun + jul + aug + sep + day - 1
elif month == "nov":
    mDay = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + day - 1
elif month == "dec":
    mDay = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + day - 1

mmDay = 365 - mDay #how many days the user was alive in their birth year

#Adding it all together
nDays = mmDay + yDay + curDayPassed #adds how many days the user was alive in their birth year, whole years and current year.

#Printing the final answer
print(f"Hi {name}, you have been alive for approximately {nDays} days.")