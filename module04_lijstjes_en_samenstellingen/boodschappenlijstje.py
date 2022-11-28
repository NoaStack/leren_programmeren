boodschappenLijst = {}

keuze = 'neutraal'

while keuze == 'neutraal' or 'Ja':
    producten = (input('Wat wil je toevoegen? ')).capitalize()
    if producten not in boodschappenLijst:
        boodschappenLijst[producten] = 1
    else:
        boodschappenLijst[producten] += 1
    toevoeging = (input('Wil je nog meer toevoegen? ')).capitalize()
    if toevoeging == 'Nee':
        break
    
print('--------------------{''Boodschappenlijst''}--------------------')
for i in boodschappenLijst:
    print(boodschappenLijst[i], 'x', i)
print('--------------------{''Boodschappenlijst''}--------------------')