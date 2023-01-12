# while deelnemers[0] == lootjes[0]:
#     random.shuffle(lootjes)

# while deelnemers[1] == lootjes[1]:
#     random.shuffle(lootjes)

# while deelnemers[2] == lootjes[2]:
#     random.shuffle(lootjes)

import random
import string

abc = list(string.printable)
deelnemers = list(string.printable)
lootjes = list(string.printable)

# while True:
#     naam = input("Welke naam\n>>> ")
#     if naam == "" and len(deelnemers) < 2:
#         print("Er moeten minimaal 3 namen zijn ")
#     elif naam == "" and len(deelnemers) > 2:
#         break
#     if naam != "":
#         if naam not in deelnemers:
#             deelnemers.append(naam)
#             lootjes.append(naam)
#         else:
#             print("Die naam is er al")


# for x in range(random.randint(3, 26)):
#     deelnemers.append(random.choice(abc))
    
lootjes = deelnemers.copy()

def test():
    getal = len(deelnemers) - 1
    for i in range(getal):
        for index, item in (enumerate(deelnemers)):
            while item == lootjes[index]:
                random.shuffle(lootjes)                      
    for x in range (len(deelnemers)):
        if deelnemers[x] == lootjes[x]:
            print(f"{deelnemers[x]} heeft {lootjes[x]}")
    
        
        
for x in range(1000):
    print("---------")
    test()