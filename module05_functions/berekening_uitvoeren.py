def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

eerste_ronde = True
n1 = False
n2 = False
keuze = False

b = ("""
A) iets optellen
B) iets aftrekken
C) iets vermenigvuldigen
D) iets delen
E) getallen ophogen
F) getallen verlagen
G) getallen verdubbelen
H) getallen halveren
I) niets""")

a = ("""       
Wat wilt u doen?
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getallen ophogen
F) getallen verlagen
G) getallen verdubbelen
H) getallen halveren
I) niets""")

while eerste_ronde:
    if n1 == False:
        print(a)
    else:
        print(b)
    keuze = input("""Kies:
""")
    if keuze == "i":
        break
    elif keuze == "a":
        som = addition
        reken = "+"
        print("Getallen optellen")
        while n1 == False:
            try:
                n1 = float(input("Welk getal? "))
            except:
                print("Typ een nummer")
        while n2 == False:
            try:
                n2 = float(input(f"Welk getal optellen bij {n1}? "))
            except:
                print("typ een nummer in")
    elif keuze == "b":
        som = subtraction
        reken = "-"
        print("Getallen aftellen")
        while n1 == False:
            try:
                n1 = float(input("Welk getal? "))
            except:
                print("Typ een nummer in")
        while n2 == False:
            try:
                n2 = float(input(f"Welk getal aftrekken bij {n1}? "))
            except:
                print("typ een nummer in")
    elif keuze == "c":
        som = multiplication
        reken = "x"
        print("Getallen vermenigvuldigen")
        while n1 == False:
            try:
                n1 = float(input("Welk getal? "))
            except:
                print("Typ een nummer in")
        while n2 == False:
            try:
                n2 = float(input(f"Welk getal vermenigculdigen bij {n1}? "))
            except:
                print("typ een nummer in")            
    elif keuze == "d":
        som = division
        reken = ":"
        print("Getallen delen")
        while n1 == False:
            try:
                n1 = float(input("Welk getal? "))
            except:
                print("Typ een nummer in")
        while n2 == False:
            try:
                n2 = float(input(f"Welk getal delen bij {n1}? "))
            except:
                print("typ een nummer in")
    elif keuze == "e":
        som = addition
        reken = "+"
        n2 = 1
        print("Getallen ophogen")
    elif keuze == "f":
        som = subtraction
        reken = "-"
        n2 = 1
        print("Getallen verlagen")
    elif keuze == "g":
        som = multiplication
        reken = "x"
        n2 = 2
        print("Getallen verdubbelen")
    elif keuze == "h":
        som = division
        reken = ":"
        n2 = 2
        print("Getallen halveren")
    else:
        continue
    print(f"{n1} {reken} {n2} = {som(number1=n1, number2=n2)}")
    print("--------------------------------------------------")
    print(f"Wat wilt u doen met de uitkomst ({som(number1=n1, number2=n2)})")
    n1 = som(number1=n1, number2=n2)
    n2 = False