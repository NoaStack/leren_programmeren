from fruitmand import fruitmand

list = []

for x in fruitmand:
    list.append(x['name'])
    
print max(list)