import random


def get_random_woord() -> str:
    try:
        with open('woorden.txt') as file:
            content = file.read()
            woorden_lijst = content.split('\n')
            te_raden_woord = random.choice(woorden_lijst)
    except:
        te_raden_woord = 'appel'
    return te_raden_woord

def vraag_om_een_letter() -> str:
    while True:
        letter = input("Voer een letter in: ")
        if len(letter) != 1:
            print("Je moet max 1 letter invoeren!!!")
        elif not letter.isalpha():
            print("jet moet wel een letter invoeren!!!")
        elif letter.isupper():
            print("Geen hoofdletters a.u.b")
        else:
            return letter

