jokes = ["",
    "1. Why did the chicken cross the road? To get to the other side.",
    "2. What’s black and white and eats like a horse? A zebra.",
    "3. On a farm there is a cow and a sheep. The cow asked the sheep 'How long have you been in this farm?'. The sheep responded with 'MMEEEHH'",
    "4. Where does a farmer get his medicine from? The farm-acist",
    "5. What kind of pigs know karate? Pork chops",
    "6. What do you call a Mexican who lost his car? Carlost",
    "7. What do you call someone who can’t aim? Blind",
    "8. What type of horses only go out at night? Nightmares",
    "9. What do you call a horse that lives next door? A neigh-bor",
    "10. What do you call brown and sticky? A stick",
    "11. I tried to navigate the farmer’s field… But it was a maize",
    "12. Two crows go on a date, and they go to a bar which bar do they go to? A crowbar…",
    "13. Why did the cabbage win the race? Because it was ahead",
    "14. How do farmers party? They turnip",
    "15. Who tell chicken jokes? Comedihens"]

tempjokes = []

jokes2 = ["",
    "1. Why did the chicken cross the road? To get to the other side.",
    "2. What’s black and white and eats like a horse? A zebra.",
    "3. On a farm there is a cow and a sheep. The cow asked the sheep 'How long have you been in this farm?'. The sheep responded with 'MMEEEHH'",
    "4. Where does a farmer get his medicine from? The farm-acist",
    "5. What kind of pigs know karate? Pork chops",
    "6. What do you call a Mexican who lost his car? Carlost",
    "7. What do you call someone who can’t aim? Blind",
    "8. What type of horses only go out at night? Nightmares",
    "9. What do you call a horse that lives next door? A neigh-bor",
    "10. What do you call brown and sticky? A stick",
    "11. I tried to navigate the farmer’s field… But it was a maize",
    "12. Two crows go on a date, and they go to a bar which bar do they go to? A crowbar…",
    "13. Why did the cabbage win the race? Because it was ahead",
    "14. How do farmers party? They turnip",
    "15. Who tell chicken jokes? Comedihens"]

lijst_fout = (1, 3, 6, 15)
lijst_goed = (2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 14)


# def maak_keuze() -> bool:
#     death = False
    
#     return death

# while True:
#     if maak_keuze():
#         print("Je bent dood") 
#         break 
    
    
def kings_room():
    print("You've entered the king's room at last")
    print("You see the king not amused one bit, It's time for you to bring the jokes")
    print("You have 15 jokes prepared, if he doesn't laugh at 3 of the jokes he will send you to die")
    print("You must choose which joke will make the king laugh")
    print("Choose wisely")
    
    points = 0
    lives = 3 
    
    while points < 9:
        for x in jokes:
            print(x)
        choice_jokes = int(input(">>> "))
        jokes.pop(choice_jokes)
        points += 1
        if choice_jokes in lijst_goed:
            lives -= 1
 
        if choice_jokes in lijst_fout:
            if  lives == 0:
                print("The king's has had enough of your silly bad jokes")
                print("The king sends you to squeezer")
                print("You get squeezed and you died")
                print("GAME OVER")
                exit()

print("You made the king laugh, you enjoy your riches and luxuries")
    
def intro():
 print("##### Funny farmer ####")
 print()
 print()
 print("You're a funny farmer you live a quite life in the downhills of a great kingdom")
 print("One day, there was a challenge make the king laugh and if you did you would get all the luxury and all the riches that u could ever need")
 print("You muster up your courage as a farmer to face the challenge, there's a catch though fail to make the king laugh and you will die")
 print("You enter the kingdom there's 3 paths in your way to the king's room")
 print("1. You can go left")
 print("2. You can in front")
 print("3. You can right")
 choice = input(">>> ")
 if choice == "1":
    print("You went left, this isn't the king's room this is the squeezer")
    print("The gaurds mistake you for someone to be squeezed")
    print("the guards force you to be squeezed and you die")
    print("GAME OVER")
 elif choice == "2":
    print("You went in front, there's a big dragon")
    print("He eats you like you are nothing")
    print("GAME OVER")
 elif choice == "3":
    kings_room()
 else:
    print("You've spelt something wrong")
    intro()
    
intro()