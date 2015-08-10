excerpt = """
The Babel fish, said The Hitchhikers Guide to the Galaxy quietly,
is small, yellow, and leech-like, and probably the oddest thing in
the Universe. It feeds on brainwave energy received not from its own
carrier but from those around it. It absorbs all unconscious mental
frequencies from this brainwave energy to nourish itself with. It then
excretes into the mind of its carrier a telepathic matrix formed by
combining the conscious thought frequencies with nerve signals picked
up from the speech centres of the brain which has supplied them. The
practical upshot of all this is that if you stick a Babel fish in your
ear you can instantly understand anything said to you in any form of
language. The speech patterns you actually hear decode the brainwave
matrix which has been fed into your mind by your Babel fish.
"""

def word_count(word_count_pair):
    return word_count_pair[1]

frequency = {}
for word in excerpt.split():
    try:
        frequency[word] += 1
    except KeyError:
        frequency[word] = 1

items = list(frequency.items())
items.sort(key=word_count, reverse=True)
print(items[:3])
