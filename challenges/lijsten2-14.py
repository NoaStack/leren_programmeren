# oefening 2:
print("oefening 2: ")
getallen = [5,12,19,27,3]

print(getallen)
print(" ")
#oefening 3:
print("oefening 3: ")
getallen.append(25)

print(getallen)
print(" ")

#oefening 4:
print("oefening 4: ")
print((len(getallen)))
print(" ")

#oefening 5:
print("oefening 5: ")
getallen.remove(12)
print(getallen)
print(" ")

#oefening 6:
print("oefening 6: ")
print(getallen)
getallen.pop(0)
print(getallen)
print("")

#oefening 7:
print("oefening 7:")
getallen.insert(0, 36)
print(getallen)

#oefening 8:
print("oefening 8: ")
samen = sum(getallen)
print(samen)

#oefening 9:
print("oefening 9: ")
getallen.clear()
print(getallen)

#oefening 10:
print("oefening 10: ")
for x in range(1, 4):
    getallen.append(x)
print(getallen)
print()

#oefening 11:
print("oefening 11: ")
for x in range(4, 51):
    getallen.append(x)
print(getallen)
print()

#oefening 12:
print("oefening 12: ")
print(getallen.index(25))
print()

#oefening 13:
print("oefening 13: ")
print(getallen)
getallen.reverse()
print(getallen)
print()

#oefening 14:
print("oefening 14: ")
lijst_14 = [1, "aap", 2, "apen", 3, "watermeloen", 15, 27, 15, "lekker bezig", "6"]
print(lijst_14)
resultaat = [value for value in lijst_14 if isinstance(value, (int))]
print(resultaat)