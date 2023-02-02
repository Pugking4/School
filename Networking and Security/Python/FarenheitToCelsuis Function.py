def convertToFarenheit(degreesCelsius):
    celsiusConvert = degreesCelsius * (9/5) + 32
    return celsiusConvert

def convertToCelsuis(degreesFarenheit):
    farenheitConvert = (degreesFarenheit - 32) * 5/9
    return farenheitConvert

#degreesCelsius = int(input("Celsuis: "))
#print(f"Farenheit output: {convertToFarenheit(degreesCelsius)}")
#degreesFarenheit = int(input("Farenheit: "))
#print(f"Celsuis output: {convertToCelsuis(degreesFarenheit)}")

assert convertToCelsuis(0) == -17.77777777777778
assert convertToCelsuis(180) == 82.22222222222223
assert convertToFarenheit(0) == 32
assert convertToFarenheit(100) == 212
assert convertToCelsuis(convertToFarenheit(15)) == 15

print("Successful!")