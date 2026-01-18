import random

correct_num = random.randint(1,20)
guesses = 0
guess = 0

while guess != correct_num:

    guess = int(input("Guess a number between 1 and 20: "))
    guesses += 1

    if guess == correct_num:
        print("Correct! It took ",guesses," guesses.")
        break
    elif guess < correct_num:
        print(guess,"-> Too low")
    elif guess > correct_num:
        print(guess,"-> Too high")

