groep_a = []
scores = []

while len(groep_a) < 3:
    land_vraag = input("Welk land wil je toevoegen? ")
    groep_a.append(land_vraag)
    
print(f"Wat is de score van {groep_a[0]} tussen {groep_a[1]}")
score_1 = int(input(f"Score van {groep_a[0]} "))
score_2 = int(input(f"Score van {groep_a[1]} "))


scores.append(score_1)
scores.append(score_2)

total_scorses = scores[0] - scores[1]

if scores[0] > scores[1]:
    score_3 = scores[0]
    score_4 = total_scorses
    punten_1 = scores[1]
    punten_2 = scores[0]
else:
    score_3 = total_scorses
    score_4 = scores[1]
    punten_2 = scores[0]
    punten_2 = scores[1]
    
print(f"""
Wedstrijd {groep_a[0]} - {groep_a[1]} eindigde in: {scores[0]} - {scores[1]}
Overzicht groep A
{groep_a[0]}: punten {punten_1};  doelsaldo: {score_3}
{groep_a[1]}: punten {punten_2};  doelsaldo: {score_4}
{groep_a[2]}: punten;  doelsaldo: 0
""")

