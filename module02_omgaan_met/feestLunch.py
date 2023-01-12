croissantjes = int(input("Hoeveel croissantjes wilt jij? "))
stokBroden = int(input("Hoeveel stokbroden wilt jij? " ))
kortingsBonnen = int(input("Hoeveel kortingsbonnen heb jij? " ))
totaal = croissantjes + stokBroden * kortingsBonnen

print (f"De feestlunch kost je bij de bakker {totaal} euro voor de {croissantjes} croissantjes en de {stokBroden} stokbroden als de {kortingsBonnen} kortingsbonnen nog geldig zijn!")