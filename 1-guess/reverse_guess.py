class InvalidStateException(Exception):
    pass

print("Think of a number between 0 and 99")
highest = 100
lowest = -1
new_guess = (highest + lowest) // 2
guessed = input("Did you think of {} [y/h/l]?".format(new_guess))
try:
    while guessed != "y":
        if guessed == "h":
            lowest = new_guess
        if guessed == "l":
            highest = new_guess
        new_guess = (highest + lowest) // 2
        if new_guess == highest or new_guess == lowest:
            raise InvalidStateException("Hey, you've entered something wrong!")
        guessed = input("Did you think of {} [y/h/l]?".format(new_guess))
except InvalidStateException as e:
    print(e)
