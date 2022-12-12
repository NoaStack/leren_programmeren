def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2




while True:
    choice = (input("""
    Wat wilt u doen?
    A) getallen optellen
    B) getallen aftrekken
    C) getallen vermenigvuldigen
    D) getallen delen
    E) getallen ophogen
    F) getallen verlagen
    G) getallen verdubbelen
    H) getallen halveren
    I) niets
    Kies: 
    """)).lower()
    if choice == "i":
        break
    if choice == "a" or choice == "b" or choice == "c" or choice == "d":
        n1 = float(input("Welk getal? "))
        if choice == "a":
            n2 = float(input(f"Welk getal optellen bij {n1}? "))
            som = addition
            reken = "+"
            
        elif choice == "b":
            n2 = float(input(f"Welk getal aftrekken bij {n1}? "))
            som = subtraction
            reken = "-"
            
        elif choice == "c":
            n2 = float(input(f"Welk getal vermenigvuldigen bij {n1}? "))
            som = multiplication
            reken = "x"
            
        elif choice == "d":
            n2 = float(input(f"Welk getal delen bij {n1}? "))
            som = division
            reken = ":"
        test = (f"{n1} {reken} {n2} = {som(number1=n1, number2=n2)}")
        elkaar = (som(number1=n1, number2=n2))
        print(test)
        print("--------------------------------------------------")
        print(f"Wat wilt u doen met de uitkomst van ({elkaar})")
    else:
        if choice == "d":
            try:
                n2 = float(input(f"Welk getal ophogen bij {elkaar}? "))
                som = addition
                reken = "+"
            except:
                print("Je hebt nummer 1 niet")
        elif choice == "e":
            try:
                n2 = float(input(f"Welk getal ophogen bij {n1}? "))
            except:
                print("Je hebt nummer 1 niet")
        elif choice == "f":
            try:
                n2 = float(input(f"Welk getal ophogen bij {n1}? "))
            except:
                print("Je hebt nummer 1 niet")
        elif choice == "g":
            try:
                n2 = float(input(f"Welk getal ophogen bij {n1}? "))
            except:
                print("Je hebt nummer 1 niet")
        elif choice == "g":
            try:
                n2 = float(input(f"Welk getal ophogen bij {n1}? "))
            except:
                print("Je hebt nummer 1 niet")
        
        test = (f"{n1} {reken} {n2} = {som(number1=elkaar, number2=n2)}")
        elkaar = (som(number1=n1, number2=n2))
        print(test)
        print("--------------------------------------------------")
        print(f"Wat wilt u doen met de uitkomst van ({elkaar})")
    
