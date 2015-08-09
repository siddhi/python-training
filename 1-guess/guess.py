import random


def get_guess():
    guess = None
    while guess is None:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Enter an integer please")
    return guess

number = random.randint(0, 99)
print("I've thought of a number between 0 and 99. Try to guess it")

guess = get_guess()
while guess != number:
    if number < guess:
        print("Nope! It's lower")
    elif number > guess:
        print("Nope! It's higher")
    guess = get_guess()

print("You got it, it was {}".format(guess))
