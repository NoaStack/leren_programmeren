from fruitmand import fruitmand
import random

sheesh = []
vraag = input("Hoeveel ? ")
for x in fruitmand:
    sheesh.append(x['name'])

print(f"{random.choice(sheesh)} {vraag} ")
