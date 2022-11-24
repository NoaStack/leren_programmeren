import random


kleuren_tuple = ('orange', 'blauw', 'groen', 'bruin')
m_en_ms = int(input("Hoe veel M&M's moeten er in de zak? "))
hoeveel_m_en_ms = []


for x in range(1, m_en_ms + 1):
    hoeveel_m_en_ms.append(random.choice(kleuren_tuple))
print(hoeveel_m_en_ms)
orangje_aantal = hoeveel_m_en_ms.count('orange')
bluaw_aantal = hoeveel_m_en_ms.count('blauw')
groen_aantal = hoeveel_m_en_ms.count('groen')
bruin_aantal = hoeveel_m_en_ms.count('bruin')
print(f"Je hebt een M&M zak met {m_en_ms} daarvan zijn er\n{orangje_aantal} oranje\n{bluaw_aantal} blauwe\n{groen_aantal} groene\n{bruin_aantal} bruine")


