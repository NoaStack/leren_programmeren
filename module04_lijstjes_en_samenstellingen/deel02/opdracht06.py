from fruitmand import fruitmand


for x in fruitmand:
    gewicht = (x['name'])
    if gewicht == 'appel':
        print(x['weight'])
