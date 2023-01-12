#Swimming garden
zwembad_lengte = float(input("Zwembad breedte in meter? "))
zwembad_breedte = float(input("Zwembad lengte in meter ?"))
zwembad_lengte_keer_breedte = zwembad_breedte * zwembad_lengte
zwembad_diepte = float(input("Zwembad diepte in meter? "))
zwembad_totaal = zwembad_diepte * zwembad_lengte_keer_breedte
kosten_uitgraven = round(25 * zwembad_totaal,2)
kosten_afvoeren = round(32.50 * zwembad_totaal, 2)
voorrij_afstand = 60 * 2.05
voorrijkosten = round(voorrij_afstand + 250, 2)
totale_kosten = round(kosten_afvoeren + kosten_uitgraven + voorrijkosten,2)


if zwembad_totaal < 20:
    beton_tegels_rood = 25 * zwembad_totaal
elif zwembad_totaal > 20:
    beton_tegels_rood = 20* zwembad_totaal 
if zwembad_totaal < 20:
    beton_tegels = 250 * zwembad_totaal
elif zwembad_totaal > 20:
    beton_tegels = 200 * zwembad_totaal


print(
f""" Zwembad Kosten
Uitgraven:                    ${kosten_uitgraven}
Afvoeren grond:               ${kosten_afvoeren}
Voorrijkosten                 ${voorrijkosten}
Totaal:                       ${totale_kosten}""")