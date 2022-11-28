from fruitmand import fruitmand

namen = []
lengte = []

for i in fruitmand:
    namen.append(i['name'])
    
sheesh = namen.count(1)
    

for x in namen:
    lengte.append(len(x))

lengte.sort(reverse=True)


for x in fruitmand:
    if len(x['name']) == (lengte[0]):
        print(f"De {x['name']} ({(lengte[0])} leters) heeft een {x['color']} kleur en een gewicht van {x['weight'] / 1000} kg")