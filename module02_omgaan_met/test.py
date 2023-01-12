def kings_rooms():
    print("You entered the king's room you have 15 jokes to make him laugh")
    print("Choose")
    jokes = [
    "1. Why did the chicken cross the road? To get to the other side.\n",
    "2. What’s black and white and eats like a horse? A zebra.\n",
    "3. On a farm there is a cow and a sheep. The cow asked the sheep 'How long have you been in this farm?'. The sheep responded with 'MMEEEHH'\n",
    "4. Where does a farmer get his medicine from? The farm-acist\n",
    "5. What kind of pigs know karate? Pork chops\n",
    "6. What do you call a Mexican who lost his car? Carlost\n",
    "7. What do you call someone who can’t aim? Blind\n",
    "8. What type of horses only go out at night? Nightmares!\n",
    "9. What do you call a horse that lives next door? A neigh-bor\n",
    "10. What do you call brown and sticky? A stick\n",
    "11. I tried to navigate the farmer’s field… But it was a maize\n",
    "12. Two crows go on a date, and they go to a bar which bar do they go to? A crowbar…\n",
    "13. Why did the cabbage win the race? Because it was ahead\n",
    "14. How do farmers party? They turnip\n",
    "15. Who tell chicken jokes? Comedihens\n"]
    print(jokes)
    choice = input(">>> ")
    if choice == "1":
        print("You went left, this isn't the king's room this is the squeezer")
        print("The gaurds mistake you for someone to be squeezed")
        print("the guards force you to be squeezed and you die")
        print("GAME OVER")
    else:
        print("You've spelt somethign wrong")
    kings_rooms()       
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
        quit()
    elif choice == "2":
        print("You went in front, there's a big dragon")
        print("He eats you like you are nothing")
        print("GAME OVER")
    elif choice == "3":
        kings_rooms()
    else:
        print("You've spelt something wrong")
        intro()
intro()