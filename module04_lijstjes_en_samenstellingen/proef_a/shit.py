import random

namen = []
loten = {}
keys = []
values = []

while True:
    naamVraag = input('naam: ').lower()
    if naamVraag not in namen:
        namen.append(naamVraag)

    if len(namen) >= 3:
        ask = input('Wil je nog namen toevoegen? ja / nee ')
        if (ask.lower()).startswith('n'):
            break
        else:
            continue
        

while len(loten) != len (namen):
    for naam in namen:
        randomNaam = random.choice(namen)
        if naam != randomNaam and naam not in keys and randomNaam not in values:
           loten[naam] = randomNaam
           keys.append(naam)
           values.append(randomNaam)
            

print(loten)

for i, j in loten.items():
    print(i.capitalize() , 'heeft', j.capitalize(), 'getrokken!')