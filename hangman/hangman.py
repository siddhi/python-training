import random

f = open("words_alpha.txt")
words = []
for line in f:
    words.append(line.strip())
word = random.choice(words).lower()

guessed_letters = ["-"] * len(word)
has_won = False
num_guesses = 8
while not has_won and num_guesses > 0:
    print("".join(guessed_letters))
    print("You have {} guesses remaining".format(num_guesses))
    guess = input("Enter a letter to guess: ").lower()
    correct_guess = False
    for index, letter in enumerate(word):
        if letter == guess:
            guessed_letters[index] = guess
            correct_guess = True
    if "-" not in guessed_letters:
        has_won = True
    if not correct_guess:
        num_guesses -= 1

if has_won:
    print("You won! The word was {}".format(word))
else:
    print("You lost. The word was {}".format(word))

