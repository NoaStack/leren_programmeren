alle_dagen_van_de_week = ("maandag","dinsdag","woensdag","donderdag","vrijdag","zaterdag","zondag")
werk_dagen = alle_dagen_van_de_week[0:5]
weekend_dagen = alle_dagen_van_de_week[5:7]
omgekeerd_dagen = alle_dagen_van_de_week[::-1]
omgekeerd_werkdagen = alle_dagen_van_de_week[4::-1]
omgekeerd_weekend_dagen = alle_dagen_van_de_week[6:4:-1]

for x in alle_dagen_van_de_week:
    print(x)

print()
print("werk dagen: ")


for x in werk_dagen:
    print(x)

print()
print("weekend dagen: ")


for x in weekend_dagen:
    print(x)
    
print()
print("omgekeerd dagen: ")

for x in omgekeerd_dagen:
    print(x)

print()
print("omgekeerd werkdagen: ")


for x in range(4, -1, -1):
    print(alle_dagen_van_de_week[x])
    
print()
print("omgekeerd weekend dagen: ")

for x in omgekeerd_weekend_dagen:
    print(x)
