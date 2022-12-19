namen = []
leeftijden = []
a = 0
vraag = True

def namen_leeftijden(l):
    global vraag
    naam = input("Voer een naam in:\nOf voer stop in om te stoppen:\n>>> ")
    if naam == "stop":
        vraag = False
        return False
    leeftijd = input("Voer een leeftijd in: ")
    namen.append(naam)
    leeftijden.append(leeftijd)
    return{'naam':naam, 'leeftijd':leeftijd}

while vraag:
    namen_leeftijden()
    
for i in namen:
    print(f'{i} is {leeftijden[a]} jaar')
    a +=1