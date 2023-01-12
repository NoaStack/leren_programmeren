import random
getal_1 = random.randint(1,100)
Vraag_1 = input("Wilt u beginnen, ")
while Vraag_1 == "ja":
    for x in range(20):
        for x in range(10):
            Vraag_2 = int(input("raad het getal, "))
            
        Vraag_4 = input("wil je nog een ronde? ")
        if Vraag_4 == "nee":
            quit()
        else:
            continue
    if Vraag_2 >= getal_1:
        print("lager")
    else:
        print("hoger")


else:
    quit