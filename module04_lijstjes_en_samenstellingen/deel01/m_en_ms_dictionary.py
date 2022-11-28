import random
aantalStukjes = int(input("Hoe veel m en ms? "))

kleuren = ['rood', 'geel', 'blauw', 'bruin', 'groen']
zak = {}

for i in kleuren:
    zak[i] = 0
for i in range(aantalStukjes):
    zak[random.choice(kleuren)] += 1
    
print(zak)