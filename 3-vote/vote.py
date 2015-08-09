votes = {}
voters = []

for line in open("votes.txt"):
    person, vote = [item.strip() for item in line.split("-")]
    if person.lower() in voters:
        continue

    if vote in votes:
        votes[vote] += 1
    else:
        votes[vote] = 1
    voters.append(person.lower())

winner = (None, 0)
for colour, votes in votes.items():
    if votes > winner[1]:
        winner = (colour, votes)

print("Annnd, the winner is {0} with {1} votes!".format(winner[0], winner[1]))
