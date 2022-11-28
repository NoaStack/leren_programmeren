from fruitmand import fruitmand

kleuren = []
for x in fruitmand:
    druif = (x['name'])
    if druif == 'druif':
        fruitmand.remove(x)
    kleur = (x['color'])
    if kleur not in kleuren:
        kleuren.append(kleur)

print(kleuren)