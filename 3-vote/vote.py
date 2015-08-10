votes = {}
voters = []


with open("votes.txt") as file_obj:
    for line in file_obj:
        person, vote = [item.strip() for item in line.split("-")]
        if person.lower() in voters:
            continue

        if vote in votes:
            votes[vote] += 1
        else:
            votes[vote] = 1
        voters.append(person.lower())

winner = ("", 0)
for colour in votes:
    if votes[colour] > winner[1]:
        winner = (colour, votes[colour])

print("Annnd, the winner is {0[0]} with {0[1]} votes!".format(winner))
