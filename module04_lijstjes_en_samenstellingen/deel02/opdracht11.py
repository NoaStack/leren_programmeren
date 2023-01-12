from fruitmand import fruitmand
kleuren = []
rond_kleuren = []
niet_rondkleuren = []
for x in fruitmand:
    kleuren.append(x['color'])
    if x['round'] == True:
        rond_kleuren.append(x['color'])
    elif x['round'] == False:
        niet_rondkleuren.append(x['color'])

    

while True:
    for i in fruitmand:
        print(i['color'])
    keuze_kleur = input(f"Which color do you want? ")
    if keuze_kleur not in kleuren:
        print("Deze kleur zit er niet in")
    else:
        break
    
print(keuze_kleur)

rond_teller = rond_kleuren.count(keuze_kleur)
niet_rond_teller = niet_rondkleuren.count(keuze_kleur)


if niet_rond_teller > rond_teller:
    print(f" Er zijn {abs(rond_teller - niet_rond_teller)} meer ronde vruchten dan niet ronde vruchten in de kleur {keuze_kleur}")
    
if niet_rond_teller < rond_teller:
    print(f" Er zijn {abs(niet_rond_teller - rond_teller)} minder ronde vruchten dan niet ronde vruchten in de kleur {keuze_kleur}")

if rond_teller == niet_rond_teller:
    print(f" Er zijn {rond_teller} rond en {niet_rond_teller} niet ronde vruchten in de kleur{keuze_kleur}")
    
    