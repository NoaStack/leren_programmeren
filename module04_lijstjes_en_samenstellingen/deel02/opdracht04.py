from fruitmand import fruitmand
import random

naam = []
vraag = input("Hoeveel ? ")
for x in fruitmand:
    naam.append(x['name'])

print(f"{random.choice(naam)} {vraag} ")
