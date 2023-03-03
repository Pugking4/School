#Challenge 4
def FizzBuzz(int):
    if int%3 == 0 and int%5 == 0:
        print("Output: FizzBuzz")
    elif int%3 == 0:
        print("Output: Fizz")
    elif int%5 == 0:
        print("Output: Buzz")
    else:
        print(f"Output: {int}")

FizzBuzz(int(input("Input: ")))