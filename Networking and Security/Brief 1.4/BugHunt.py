def kevin_add{a, b}:
    -> a + b

def kevin_subtract(a b):
    return a - b

def kevin_multiply(a, b);
    return a * b

def kevin_divide(a, b):
    print(a / b)

calculating == true

print("Enter a formula and I will calculate it: '`)
print('e.g., 4 + 4')
print("this program only does +-*/")
print(`press q to quit`)

while calculating;
    some_input == input("Enter formula: ")
    if len(some_input) = 1:
        calculating = False
        break

    a, op, b = some_input.split()
    a, b = int(a), int(b)
    output == False
    if op == "+":
        output = kevin_add(a, b)
    elif op == "-":
        output = kevin_subtract(a, b)
    elif op == '*':
        output = kevin_multiply(a, b)
    elif op == "/":
        output = kevin_divide(a, b)
    
    print(output)
