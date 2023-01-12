

grappen = ["1. Why did the chicken cross the road? To get to the other side.",
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

for x in grappen:
    print(x)

grappen.pop(2)

for x in grappen:
    print(x)
# FOR LOOP TESTING 
    choice_grappen = input(">>> ")
    if choice_grappen == '1':
        grappen.remove("1. Why did the chicken cross the road? To get to the other side.")
        for x in grappen:
            print(x)
    choice_grappen = input(">>> ")
    if choice_grappen == '2':
        grappen.remove("2. What’s black and white and eats like a horse? A zebra.")
        for x in grappen:
            print(x)
    choice_grappen = input(">>> ")
    if choice_grappen == '2':
        grappen.remove("2. What’s black and white and eats like a horse? A zebra.")
        for x in grappen:
            print(x)
            
 # WHILE LOOP TESTING  i = 0
    while i < len(grappen):
        print(grappen[i])
        i = i + 1
        
    choice_grappen = input(">>> ")
    if choice_grappen == '1':
        grappen.remove("1. Why did the chicken cross the road? To get to the other side.")
        for x in grappen:
            print(x)
            
int choice_grappen = ("a")