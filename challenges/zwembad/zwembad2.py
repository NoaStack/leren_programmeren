zwembad_lengte = float(input("Wat is de lengte van het zwembad in meter? "))
zwembad_breedte = float(input("Wat is de breedte van het zwembad in meter? "))
zwembad_diepte = float(input("wat is diepte van het zwembad in meter? "))
voorrij_afstand = int(input("Wat is de afstand van het zwembad in km? "))
kleur = input("Welke kleur moet de tegels van het zwembad worden? ")
zwembad_totale_afstand = zwembad_lengte * zwembad_breedte *zwembad_diepte
kosten_uitgraven = round(zwembad_totale_afstand * 25.00, 2)
kosten_afvoeren = round(zwembad_totale_afstand * 32.50, 2)
beton_tegels = zwembad_totale_afstand * 10
if voorrij_afstand < 50 and zwembad_totale_afstand < 20:
    voorijkosten = 1.25 * zwembad_totale_afstand + 100
elif voorrij_afstand > 50 and zwembad_totale_afstand < 20:
    voorijkosten = 1.15 * zwembad_totale_afstand + 100
elif voorrij_afstand < 50 and zwembad_totale_afstand > 20:
    voorijkosten = 2.15 * zwembad_totale_afstand + 250
elif voorrij_afstand > 50 and zwembad_totale_afstand > 20:
    voorijkosten = 2.05 * zwembad_totale_afstand + 250
if zwembad_totale_afstand < 20:
    beton_tegels_kosten = 25 * zwembad_totale_afstand
elif zwembad_totale_afstand > 20:
    beton_tegels_kosten = 20 * zwembad_totale_afstand
if kleur != "rood" and zwembad_totale_afstand < 20:
    kleur_prijs = 100
elif kleur != "rood" and zwembad_totale_afstand > 20:
    kleur_prijs = 125
if kleur == "rood" and zwembad_totale_afstand < 20:
    kleur_prijs = 25 * zwembad_totale_afstand
elif kleur == "rood" and zwembad_totale_afstand < 20:
    kleur_prijs = 20 * zwembad_totale_afstand
totale_prijs = round(kosten_afvoeren + kosten_uitgraven + voorijkosten + beton_tegels_kosten, 2)
    
print(f"""Offerte voor een zwembad van {zwembad_lengte} bij {zwembad_breedte} bij {zwembad_diepte} meter(inhoud: {round(zwembad_totale_afstand, 2)} m3
      Uitgraven:                        ${kosten_uitgraven}
      Afvoeren grond:                   ${kosten_afvoeren}
      Voorrijkosten                     ${round(voorijkosten, 2)}
      Beton + tegel({round(beton_tegels,2)} m2)  ${round(beton_tegels_kosten)}
      Totaal:                           ${totale_prijs}""")

