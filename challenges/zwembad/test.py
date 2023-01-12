inhoud1 = int(input("Hoeveel m3 is uw zwembad? "))
print(f"Uitgraven: €{25*36.0}")
afvoeren = round(32.20*inhoud1)
print(f"Afvoeren grond: €{afvoeren}")
voorrijkosten = round(60*2.05)
print(f"Voorrijkosten: €{voorrijkosten}")
inhoud2 = (inhoud1 / 10)
kleur = input("Welke kleur wilt u? ")
if inhoud2 < 20:
    geld = 250
    if kleur == 'rood':
        kleur_geld = 25
    else:
        kleur_geld = 100
elif inhoud2 >=20:
    geld = 200
    if kleur == 'rood':
        kleur_geld = 20
    else:
        kleur_geld = 125
print(f"Beton + tegel: €{geld + kleur_geld}")
print(f"Totaal: €{250 + 25*inhoud1 + 32.20*inhoud1 + voorrijkosten + geld + kleur_geld}")