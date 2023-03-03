temp = []
master = []
count = 0
dict = {}
ele_count = 1
key = ()
test = "False"

#master = [('the', 'big', 'red', 'ball'), ('the', 'big', 'red', 'ball', 'is', 'near', 'the', 'big', 'red', 'box'), ('i', 'am', 'near', 'the', 'box')]

userInput = input("Line: ").lower()
while userInput:
    temp = tuple(userInput.split())
    master.append(temp)
    userInput = input("Line: ").lower()

#print(master)



for mas_element in master:
    #print(mas_element)
    #print(mas_element[0:2])
    for i in range(len(mas_element)-1):
        #if test == "False":
        #    y = i + 1
        ele_count = 1
        y = i + 1
        #x = i
        #if x == i:
        #    x = i + 1
        #key = (count, mas_element[i:i+2])
        #print("key",key)
        #print(mas_element[i:y+1])
        if mas_element[i:y+1] in dict:
            ele_count = dict[mas_element[i:y+1]] + 1
            #print(mas_element[i:y+1],"raised to", ele_count)
        dict[mas_element[i:y+1]] = ele_count

#print(dict)

for x in dict:
    if dict[x] > 1:
        print(f"{' '.join(x)}: {dict[x]}")
