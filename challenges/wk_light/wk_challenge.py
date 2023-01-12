groepA = []
score = []
land1_punten = 0
land2_punten = 0
land3_punten = 0

for _ in range(3):
    landen = input("Welk land wil je toevoegen aan groep A: ")
    groepA.append(landen)
    
for x in range(2):
    wed1_score = int(input(f"Wat is de score van {groepA[x]}? "))
    score.append(wed1_score)

doelsaldo1 = score[0] - score[1]
print(doelsaldo1)

doelsaldo2 = score[1] - score[0]
print(doelsaldo2)

if doelsaldo1 > doelsaldo2:
    land1_punten += 3
else:
    land2_punten += 3
    
    
print(f"""
Wedstrijd {groepA[0]} - {groepA[1]} eindigde in: {score[0]} - {score[1]}
Overzicht groep A
{groepA[0]}: punten {land1_punten};  doelsaldo: {doelsaldo1}
{groepA[1]}: punten {land2_punten};  doelsaldo: {doelsaldo2}
{groepA[2]}: punten {land3_punten};  doelsaldo: 0 """)