from fruitmand import fruitmand

fruitmand.append({'name': 'watermeloen','weight': 14000, 'color': 'green','round': True})

totaal_gewicht = 0
for x in fruitmand:
    gewicht = x['weight']
    totaal_gewicht += gewicht

print(totaal_gewicht)