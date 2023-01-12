a = int(input("Geef een heel getal toe "))
b = int(input("Geef een ander heel getal toe "))

if a > b: 
    Max = a
    Min = b
    print(f"A is het grootste getal: {Max}") 
elif a < b: 
    Min = a
    Max = b
    print(f"B is het kleinste getal: {Min}")
else:
    print("a en b zijn even groot")

print(f"Het minimum is : {Min}")
print(f"Het maximum is : {Max}")