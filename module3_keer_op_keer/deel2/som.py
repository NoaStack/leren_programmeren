str_antwoord = "50"
getal = 50
som = 50
counter = 0
while som  + 1 <= 1000:
    getal += 1
    str_antwoord += " + " + str(getal)
    som += getal
    counter += 1
    print(f"{counter}. {str_antwoord} = {som}")
    