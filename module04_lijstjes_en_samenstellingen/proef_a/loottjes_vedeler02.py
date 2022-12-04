import random
namen_1 = []
namen_2 = []


while True:
    vraag = input("Wil jij een naam invullen? ")
    if vraag == "ja":
        naam = input("Welke naam? ")
        if naam not in namen_1:
            namen_1.append(naam)
            namen_2.append(naam)
        else:
            print("Die naam is er al")
    if vraag == "nee":
        if len(namen_1) < 3:
            print("Je moet 3 namen hebben")
        else:
            break
            
for x in namen_2:
    random_naam = random.choice(namen_1)
    while random_naam == x:
        random_naam = random.choice(namen_1)
    print(f"{x} heeft {random_naam}")
    namen_1.remove(random_naam)
    