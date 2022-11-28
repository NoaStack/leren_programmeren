import random

<<<<<<< HEAD

kleuren = ['orange', 'blauw', 'groen', 'bruin']
m_en_ms = int(input("Hoe veel M&M's moeten er in de zak? "))
hoeveel_m_en_ms = {}
random_kleur = random.choice(kleuren)


for x in range(m_en_ms):
    random_nummer = (random.randint(0, m_en_ms))
    totaal = m_en_ms - random_nummer
    if totaal > 0:
        hoeveel_m_en_ms.update({f"{random_kleur}": f"{totaal}"})
    
print(hoeveel_m_en_ms)

=======
aantalStukjes = int(input("Hoe veel m en ms? "))

kleuren = ['rood', 'geel', 'blauw', 'bruin', 'groen']
zak = {}

for i in kleuren:
    zak[i] = 0
for i in range(aantalStukjes):
    zak[random.choice(kleuren)] += 1

print(zak)
>>>>>>> beb39b9de3bb00f7d6da9486c98889d0ed75872c
