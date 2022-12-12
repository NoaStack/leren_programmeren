def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

eerste_ronde = " "

while eerste_ronde:
    print("""
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
    keuze = input("""Kies:
""")
    if keuze == "A".lower() or keuze == "B".lower() or keuze == "C".lower() or keuze == "D".lower():
        if keuze == "A".lower():
            print("Getallen optellen")
            n1 = float(input("Welk getal? "))
            n2 = float(input(f"""Welk getal optellen bij {n1}
"""))        
            som = addition
            reken = "+"
    
        elif keuze == "B".lower():
            print("Getallen aftrekken")
            n1 = float(input("Welk getal? "))
            n2 = float(input(f"""Welk getal aftrekken bij {n1}
"""))               
            som = subtraction
            reken = "-"
        elif keuze == "C".lower():
            print("Getallen vermeniguldigen")
            n1 = float(input("Welk getal? "))
            n2 = float(input(f"""Welk getal vermniguldigen bij {n1}
"""))                
            som = multiplication
            reken = "*"
        elif keuze == "D".lower():
            print("Getallen delen")
            n1 = float(input("Welk getal? "))
            n2 = float(input(f"""Welk getal delen bij {n1}
"""))                
            som = division
            reken = ":"

        print(f"{n1} {reken} {n2} = {som(number1=n1, number2=n2)}")
        
        
#Maak een functie voor de input 
#Maak een functie voor de strings met return

            
        