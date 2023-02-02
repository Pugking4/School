def convertToFarenheit(degreesCelcius):
    celciusConvert = degreesCelcius * (9/5) + 32
    return celciusConvert

def convertToCelcuis(degreesFarenheit):
    farenheitConvert = (degreesFarenheit - 32) * 5/9
    return farenheitConvert

#degreesCelcius = int(input("Celcuis: "))
#print(f"Farenheit output: {convertToFarenheit(degreesCelcius)}")
#degreesFarenheit = int(input("Farenheit: "))
#print(f"Celcuis output: {convertToCelcuis(degreesFarenheit)}")

assert convertToCelcuis(0) == -17.77777777777778
assert convertToCelcuis(180) == 82.22222222222223
assert convertToFarenheit(0) == 32
assert convertToFarenheit(100) == 212
assert convertToCelcuis(convertToFarenheit(15)) == 15

print("Successful!")