import random


kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
kaart_nummer = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
kaartenType = ['boer', 'vrouw', 'heer', 'aas']
kaarten = []


while len(kaarten) != 52:
    y = random.choice(kleuren)+ ' ' + (random.choice(kaart_nummer))
    if y not in kaarten:
        kaarten.append(y)
    z = random.choice(kleuren)+ ' ' + (random.choice(kaartenType))
    if z not in kaarten:
        kaarten.append(z)

kaarten.append('joker2'), kaarten.append('joker1')

a = 1
for _ in range(7):
    random_kaart = random.choice(kaarten)
    print(f"kaart {a}: {random_kaart}")
    kaarten.remove(random_kaart)
    a += 1
print ()
print(f"deck: {len(kaarten)} {kaarten}")