import sys

print("De kosten per pizza maten, is small 5 euro, medium 7 euro en large 9 euro") # print de prijzen van de pizza

try:
 small = int(input("Hoeveel small pizza's wilt u? "))
except: exit(print("Alleen gehele nummers invullen"))

try:
 medium = int(input("Hoeveel medium pziza's wilt u? "))
except: exit(print("Alleen gehele nummers invullen"))

try:
    large = int(input("Hoeveel large pizzas's wilt u? "))
except: exit(print("Alleen gehele nummers invullen"))

smallPrijs = int(small * 5)# rekensommen voor de pizza's 
mediumPrijs = int(medium * 7)# ^
largePrijs = int(large * 9)# ^
prijs = smallPrijs + mediumPrijs + largePrijs# ^

print(f"""
Restaurant Niks
Gewoon Niks

Onbestaand 31
1234 No Caps
+31 00 0000000
wwww.niet.com
small x {small}     €{smallPrijs}
medium x {medium}   €{mediumPrijs}
large x {large}     €{largePrijs}

Totaal €{prijs}""")