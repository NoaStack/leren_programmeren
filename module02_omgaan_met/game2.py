print("Suddenly you spawn in a house\nYou have two options:\n1. You can quit. \n2. You can look around")
a = input("Which option do you choose? ")
if a == '1':
    print("You've decided to quit")
if a == '2':
    print("You've decided look around and you see:\nThe door infront of you\nThe window besides you\nThe basement behind you")
    b = input("Choose in which direction you want to go\n1. The door \n2. The window\n3. The basement ")
    if b == '1':
        print("You decided to went through the window but there was a spike pit under you, you died")
    elif b == '2':
        print("You go through the door and you see: \nA spike pit under the window, good that u didn't choose the window\nand you also see a huge desert outside with a house north ")
        c = input("You have two options\n 1. go into the house that is north from you \n2. go south from the desert ")
        if c =='1':
            print("You picked to go for the house before you get there, there was a giant sand shark in your path you try to flee but you fail and you die.")
        elif c =='2':
            print("You went south of the desert and you eventually run out of water and die")
            g = input("You have two options\n 1. go into the house that is north from you \n2. go south from the desert ")
            if g =='1':
                print("You picked to go for the house before you get there, there was a giant sand shark in your path you try to flee but you fail and you die.")
            elif g =='2':
                print("You went south of the desert and you eventually run out of water and die")
            d = input("Choose what u want to do \n1. fight \n go down the ladder ")
            if d =='1':
                print("You grab your wits and you try to fight the monster, the monster easily snaps you in half and you die")
            elif d =='2':
                print("Instead of fighting the monster you run to the ladder and go down. There u find a gun\nYou have two choices\n1. go back to the up and shoot the monster\n 2. you shoot yourself")
                e = input("1")
                if e =='shoot': 
                    print("You shoot yourself and you die and lose")
                elif e == 'monster':
                    print("You go back with the gun to kill the monster.\n YOU WIN!, you win the game and the curse of the witches that placed you in this world is gone\n you go back to the real world and enjoy living once again") q    