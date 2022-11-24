# vraag om 10 getallen via de input
# nadat je 10 getallen het opgevraagd, doe je het volgende:
#print 
#het grootste getal is:...
#get kleinste getal is: ...                
# get aantal getallen deelbaar door 3 (zonder rest) is: ...
import math
import random
grootste = 0
kleinste = math.inf
aantal_getallen = 0
for x in range(100000000000000):
    for x in range(10):
        getal = random.randint(0, 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
        print(getal)
        if getal > grootste:
            grootste = getal
        if getal < kleinste:
            kleinste = getal
        if getal % 3 == 0:
            aantal_getallen = aantal_getallen + 1
        


print(f"Het grootste getal is: {grootste}")
print(f"het kleinste getal is: {kleinste}")
print(f"De getalen deelbaar door 3 (zonder rest) is: {aantal_getallen}")