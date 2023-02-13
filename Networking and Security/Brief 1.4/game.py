from random import randint

min_value = 1
max_value = 100
#max_guess = 10
current_guess = 0
guess = -1
answer = randint(min_value,max_value)

def get_guess(min_value,max_value):
    guess = int(input(f"Guess a number between {min_value} and {max_value}: ")) 
    return guess

def hint(guess, hint):
    if guess < answer:
        return f"{guess} is too low."
    elif guess > answer:
        return f"{guess} is too high."

while guess != answer:
    guess = get_guess(min_value,max_value)
    current_guess += 1
    print(hint(guess,answer))

print(f"{guess} was correct! You won in {current_guess} guesses.")
    

#print("Welcome to my guessing game!")
#while guess != answer:
#    if current_guess <= max_guess:
#        guess = int(input("Guess a number: ")) 
#        if guess != answer:
#            current_guess += 1
#            if guess > answer:
#                print(f"{guess} is too high.")
#            else:
#                print(f"{guess} is too low.")
#        if guess == answer:
#            current_guess += 1
#            print("You guessed right!")
#    else:
#        print("You ran out of guesses.")
#        break
#print("Game Over")
#'''test'''