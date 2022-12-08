from fruitmand import fruitmand

gewicht = []

for x in fruitmand:
    gewicht.append(x["weight"])
gewicht.sort(reverse=True)
for y in gewicht:
    for z in fruitmand:
        if z['weight'] == y:
            print(f"{z['name']} weegt {z['weight']} gram.")
             