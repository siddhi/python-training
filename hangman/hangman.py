import random

with open("words.txt") as fp:
    words = fp.read().split("\n")

num_guesses = 8
correct_letters = set()
wrong_letters = set()
choice = random.choice(words)

def user_wins():
    return set(choice) == correct_letters

def guesses_over():
    return num_guesses == len(wrong_letters)

def game_over():
    return user_wins() or guesses_over()

def get_char_to_display(char):
    if char in correct_letters:
        return char
    return "-"

while not game_over():
    print("You have {} wrong guesses remaining".format(num_guesses-len(wrong_letters)))
    print([get_char_to_display(char) for char in choice])
    user_char = input("Enter a character: ")
    if user_char in choice:
        correct_letters.add(user_char)
    else:
        wrong_letters.add(user_char)

print("The word is {}".format(choice))
