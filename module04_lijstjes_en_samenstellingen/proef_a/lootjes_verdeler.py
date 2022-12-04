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

for x in deelnemers:
    random_naam = random.choice(lootjes)
    while random_naam == x:
        random_naam = random.choice(lootjes)
    
    print(f"{x} heeft {random_naam}")
    lootjes.remove(random_naam)
#Idee:
# Pas printen als het niet gelijk is maar ? hoe
# als lootje 2 zelfde is als naam 2, kies alweer tot het iets anders is
# gebruik shuffle methode 
# het kan nog simpeler met 1 list