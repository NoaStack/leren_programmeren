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


getal = len(deelnemers) - 1
getal_2 = abs(getal - len(deelnemers))

for i in range(getal):
    while deelnemers[getal] == lootjes[getal]:
        random.shuffle(lootjes)
    while deelnemers[getal_2] == lootjes[getal_2]:
        random.shuffle(lootjes)
        

for x in range (len(deelnemers)):
    print(f"{deelnemers[x]} heeft {lootjes[x]}")
    
    
