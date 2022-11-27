import random
from random import shuffle

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_nummer = ["2", "3", "4", "5", "6", "7", "8", "9", "10","boer","vrouw","heer","aas"]
kaarten = []

for _ in range(2):
    kaarten.append("joker")

while len(kaarten) != 54:
    y = random.choice(kleuren)+ ' ' + (random.choice(kaart_nummer))
    if y not in kaarten:
        kaarten.append(y)

random.shuffle(kaarten)

for _ in range(1, 8):
    print(f"kaart {_}: {kaarten[_]}")
    kaarten.pop(_)
    
print()
print(f"deck: {len(kaarten)} {kaarten}")
