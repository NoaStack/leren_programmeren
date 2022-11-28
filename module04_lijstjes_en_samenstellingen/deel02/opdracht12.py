from fruitmand import fruitmand

namen = []
lengte = []

for _ in fruitmand:
    namen.append(_['name'])
    
sheesh = namen.count(1)
    
print(namen)

for x in namen:
    lengte.append(len(x))
    
lengte.sort()

print(f"naam ({lengte[0]} letters) heeft een "