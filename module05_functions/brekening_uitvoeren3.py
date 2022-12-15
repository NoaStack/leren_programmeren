def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def begin():
    return"""Wat wilt u doen?
A) getallen optellen
B) getallen aftrekken
C) getallen vermenigvuldigen
D) getallen delen
E) getallen ophogen
F) getallen verlagen
G) getallen verdubbelen
H) getallen halveren
I) niets
Kies: """

def invoer():
    test2 = input()
    return test2
    

def a(nm1, nm2):
    return nm1 and nm2
    

test = begin()

while True:
    print(test)
    invoer()
    if "a" in invoer():
        test = a(nm1=invoer, nm2=invoer)