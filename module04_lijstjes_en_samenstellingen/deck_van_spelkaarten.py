import random


kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_nummer = ["2", "3", "4", "5", "6", "7", "8", "9", "10","boer","vrouw","heer","aas"]
kaarten = []


while len(kaarten) != 52:
    y = random.choice(kleuren)+ ' ' + (random.choice(kaart_nummer))
    if y not in kaarten:
        kaarten.append(y)

kaarten.append('joker2'), kaarten.append('joker1')


for _ in range(1, 8):
    random_kaart = random.choice(kaarten)
    print(f"kaart {_}: {random_kaart}")
    kaarten.remove(random_kaart)
    
print ()
print(f"deck: {len(kaarten)} {kaarten}")
