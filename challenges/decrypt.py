text = """HVqxBjoZ!?GkqdeOEezAE!?ohNjqRuxojy!?esAX!?dLsZc!? VcpGtt!?gOxjFQkzTDy!?etEyySXt!?dMVfSG!?akOgOdFpje!?aZpjG!?nydTfnQ!q!? nmanp!?aCa!?lIYeTdIl!?l!yYZyVI!?eOm!?mfcBM!?aNteYpX!?aGFlGtW!?lSy!XYh!?,TfgEb!? uD K!?oqpjKodZrz!?mEm r!?ddo!?aFUpe!qwj!?tvZo!? qKBspNfS!?iQXfEoo!?kGSdJlWh!? VTKzOZq!?jdSLdJdKAv!?aVTKun!?rQEvJ!?ictXgAKZY!?gbIdxqGSp!? aEfGvYgv!?bWgDdYZ!?eB !?ngAt!!? D qLljmm!?vhtTdpIqoJZ!?oQyJXBHX!?lupz!?gYAVXXNg!?taWDDVBQDSO!? BQO HIOZLY!?eoTXtn!?eyR!?nYZkIf!?  OrFk!?kJenGc!?lElWj!?e hOwVlpWz!?iVF!?nu odOVXvSP!?ebinLp!? fRwfXGQs!?tWdfhPh!?ruTvo!!?aHBj!PZaHtQ!?kYYk!?tWeNjDqV!?aFMctpAli!?tnIz!?ivq!?eGRNQq!?!KbotZVm
"""
next = False
uitroep_gevonde = False
vraagteken_gevonden = False
decrypted_zin = ""

for c in text:
    print(c)
    print(next)
    print(uitroep_gevonde)
    print(vraagteken_gevonden)
    
    if next:
        decrypted_zin += c
        next = False

    vraagteken_gevonden = c == "?"
    next = vraagteken_gevonden and uitroep_gevonde
    uitroep_gevonde = c == "!"
    
    print (next)
    
print(decrypted_zin)
    