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
            


for x in range(len(deelnemers)):
    while deelnemers[x] == lootjes[x]:
        random.shuffle(lootjes)
    print(f"{deelnemers[x]} heeft {lootjes[x]}")
    

# for x in deelnemers:
#     print(teller)
#     while deelnemers[teller] == lootjes[teller]:
#         random.shuffle(lootjes)
#     print(f"{x} heeft {lootjes[teller]}") 
#     lootjes.pop(teller)
    



#Idee:
# Pas printen als het niet gelijk is maar ? hoe
# als lootje 2 zelfde is als naam 2, kies alweer tot het iets anders is
# gebruik shuffle methode 
# het kan nog simpeler met 1 list