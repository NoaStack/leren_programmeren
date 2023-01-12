kaas = input("Is de kaas geel? ")
if kaas == "ja":
    gatenkaas = input("Zitten er gaten in? ja of nee ")
    if gatenkaas == "ja":
        duurkaas = input("Is de kaas belagelijk duur? ")
        if duurkaas == "ja":print("Emmenthaler")
        elif duurkaas == "nee":print("Leerdammer")
    elif gatenkaas == "nee":
        hardkaas = input("Is de kaas hard als steen? ")
        if hardkaas == "ja": print("Parmigiano")
        elif hardkaas == "nee": print("Goudse Kaas")
if kaas == "nee":
    schimmelkaas = input("Heeft de kaas blauwe schimmel? ")
    if schimmelkaas == "ja":
        korstkaasmetschimmel = input("Heeft de kaas een korst?")
        if korstkaasmetschimmel == "ja": print("Blue de Rochbaron")
        if korstkaasmetschimmel == "nee": print("Foume d'Ambert")
    elif schimmelkaas == "nee":
        kortszonderschimmel = input("Heeft de kaas een korst? ")
        if kortszonderschimmel == "ja": print("Camemebert")
        if kortszonderschimmel == "nee": print("Mozzarella")