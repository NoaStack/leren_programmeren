import random


deelnemers = []
lootjes = []



while True:
    naam = input("Welke naam\n>>> ")
    if naam == "" and len(deelnemers) < 2:
        print("Er moeten minimaal 3 namen zijn ")
    elif naam == "" and len(deelnemers) > 2:
        break
    if naam != "":
        if naam not in deelnemers:
            deelnemers.append(naam)
            lootjes.append(naam)
        else:
            print("Die naam is er al")

for i in deelnemers:
    while True:
        random_lotje = random.choice(lootjes)
        if random_lotje == i:
            random_lotje = random.choice(lootjes)
        else:
            break
    print(f"{i} heeft {random_lotje}")
    lootjes.remove(random_lotje)
    if i in lootjes:
        lootjes.remove(i)
