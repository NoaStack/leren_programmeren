import random


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

