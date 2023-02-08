from random import randint
guess = 0
answer = randint(1,10)
print("Welcome to my guessing game!")
while guess != answer:
    guess = int(input("Guess a number: ")) 
    if guess != answer:
        print("You guessed wrong.")
print("You guessed right!")
print("Game Over")