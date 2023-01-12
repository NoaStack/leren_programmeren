boodschappenLijst = {}

toevoeging = "ja"

while toevoeging == "ja":
    producten = input('Wat wil je toevoegen? ')
    hoeveel_producten = int(input("Hoeveel wil je toevoegen? "))
    if producten not in boodschappenLijst:
        boodschappenLijst[producten] = hoeveel_producten
    else:
        boodschappenLijst[producten] += hoeveel_producten
    toevoeging = input('Wil je nog meer toevoegen? ')



print('--------------------{''Boodschappenlijst''}--------------------')
for x in boodschappenLijst:
    print(f"{boodschappenLijst[x]}x {x}")
print('--------------------{''Boodschappenlijst''}--------------------')