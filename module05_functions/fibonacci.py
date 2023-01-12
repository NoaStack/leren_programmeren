def fibonacci(hoeveel:int):
    n1, n2 = 0, 1
    teller = 0
    while teller < hoeveel:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        teller +=1
    

fibonacci(hoeveel=10)