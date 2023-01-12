personen = int(input("Met hoeveel personen ben jij? "))
toegangsticket = int(7.45)
minuten = int(input("Hoeveel minuten wil jij in de VIP-VR GameSeat? "))
minutenKosten = int(7.4 * minuten)
totaleKosten = int(personen + minutenKosten)

print (f"Dit geweldige dagje-uit met {personen} mensen in de Speelhal met {minuten} minuten VR kost je maar {totaleKosten} euro")
