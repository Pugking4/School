#Calendar wonder land

#You are to create a program that can accept user input and display it. The program that you ask to write asks a user for the following input:

#    Their given name
#    The day of their birth
#    The month of their birth
#    The year of their birth

#Your program must calculate an approximation* of how many days that person has been alive and then output it in the following format:

#"Hi {given_name}, you have been alive for approximately {n_days}"

#NOTE: calculating the exact number of days isn't trivial. An approximation is fine. Don't over think it.

m31 = ["jan","mar","may","jul","aug","oct","dec"]
m30 = ["apr","jun","sep","nov"]
m28 = "feb"
mDay = 0
curYear = 2023
curMonth = "Feb"
curMonthD = 28
curDay = 2
yDay = 0
curMonthPass = 33
jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
name = input("What's your given name? ")
day = int(input("What day were you born on? "))
year = int(input("What year were you born in? "))
month = input("What month were you born in? ")

yDay = (curYear-year-1)*365 #Calculates how many days have passed in whole years
#print(f"{yDay} days from years")

if month in m31:
    mDay = 31
elif month in m30:
    mDay = 30
elif month in m28:
    mDay = 28
else:
    mDay = 0

if month == "jan":
    mmDay = 0 + day - 1
elif month == "feb":
    mmDay = jan + day - 1
elif month == "mar":
    mmDay = jan + feb + day - 1
elif month == "apr":
    mmDay = jan + feb + mar + day - 1
elif month == "may":
    mmDay = jan + feb + mar + apr + day - 1
elif month == "jun":
    mmDay = jan + feb + mar + apr + may + day - 1
elif month == "jul":
    mmDay = jan + feb + mar + apr + may + jun + day - 1
elif month == "aug":
    mmDay = jan + feb + mar + apr + may + jun + jul + day - 1
elif month == "sep":
    mmDay = jan + feb + mar + apr + may + jun + jul + aug + day - 1
elif month == "oct":
    mmDay = jan + feb + mar + apr + may + jun + jul + aug + sep + day - 1
elif month == "nov":
    mmDay = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + day - 1
elif month == "dec":
    mmDay = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + day - 1

mmmDay = 365 - mmDay
nDays = mmmDay + yDay

print(f"Hi {name}, you have been alive for approximately {nDays} days.")