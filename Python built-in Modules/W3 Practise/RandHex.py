import random

letters = ["a","b","c","d","e","f"]
digits = random.randint(1, 6)
hex_code = ""

for i in range(int(digits)):
    hex_num = str(random.randint(0, 9))
    hex_code += hex_num

hex_code = list(hex_code)

for i in range(6-digits):
    temp = random.randint(0, len(letters)-1)
    temp2 = random.randint(0, digits)
    hex_code.insert(temp2,letters[temp])
hex_code.insert(0,"#")
hex_code = "".join(hex_code)

print(hex_code)
