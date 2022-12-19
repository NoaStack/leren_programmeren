def vraag_getal_float(vraag: str) -> float:
    while True:
        try:
            getal = float(input(vraag))
            break
        except ValueError:
            print("Typ een getal in ")
            continue   
        
    return getal