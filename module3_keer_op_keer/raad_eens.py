import random


rondes_spel = 1
rondes_raden = 10
willekeurig_getal = random.randint(0, 1000)
score = 0
einde = (f"Je hebt {rondes_spel} van de 20 punten")


while rondes_spel < 21:
    start = input("Wil jij een ronde starten? J/N ")
    print(f"Ronde {rondes_spel} van de 20")
    if start == "N":
        print(einde)
        break
    while rondes_raden > 0:
        try:
            keuze = int(input(">>> "))
        except:
            print("Je moet een nummer typen")
        verschil = abs(keuze - willekeurig_getal)
        if keuze == willekeurig_getal:
            print("Geraden!!\nVolgende ronde")
            score += 1
            break
        if keuze < willekeurig_getal:
            print("hoger")
        else: 
            print("lager")

        if verschil < 50 and verschil > 20:
            print("Je bent warm")

        if verschil < 20:
            print("Je bent heel warm")
        if rondes_raden == 1:
            print("Het is niet gelukt in 10 keer raden\nVolgende ronde")
        rondes_raden -= 1
    rondes_raden += 10
    rondes_spel += 1

print(f"Jou score is {score}")