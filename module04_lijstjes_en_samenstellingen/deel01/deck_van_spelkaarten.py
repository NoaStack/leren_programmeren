import random

kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_nummer = ["2", "3", "4", "5", "6", "7", "8", "9", "10","boer","vrouw","heer","aas"]
kaarten = []

for i in range(2):
    kaarten.append("joker")

while len(kaarten) != 54:
    y = random.choice(kleuren)+ ' ' + (random.choice(kaart_nummer))
    if y not in kaarten:
        kaarten.append(y)

random.shuffle(kaarten)

for x in range(1, 8):
    print(f"kaart {x}: {kaarten[x]}")
    kaarten.pop(x)
    
print()
print(f"deck: {len(kaarten)} {kaarten}")
