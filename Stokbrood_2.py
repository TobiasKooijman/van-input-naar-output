# Inputs

Aantal_Stokbrood = input('geef het aantal stokbroden ')
Stokbrood = input('geef de prijs van de stokbroden ')
Aantal_Croissant = input('geef het aantal croissants ')
Croissant = input('geef de prijs van de croissants ')

# Value Numbers:

Totaal_Stokbrood = int(Stokbrood) * int(Aantal_Stokbrood)
Totaal_Croissant = int(Croissant) * int(Aantal_Croissant)
Totaal = (Totaal_Croissant+Totaal_Stokbrood)
factuurtext = 'De prijs van '+str(Aantal_Croissant) + ' Croisantjes van '+str(Croissant)+' euro is '+str(Totaal_Croissant)+' en de prijs van '+str(Aantal_Stokbrood)+' Stokbroden van ' + str(Stokbrood)+' is '+str(Totaal_Stokbrood)+' dus het totale bedrag word '+str(Totaal)

print(factuurtext)