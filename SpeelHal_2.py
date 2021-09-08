# inputs

Ticket_PP = input('geef het aantal tickets ')
Aantal_Mensen = input('geef het aantal mensen ')
VIP_Gameseat_Pr5 = input('geef de prijs van  de VIP VR Gameseat ')
Tijd_Gameseat = input('geef de tijd dat uw de Vr Gameseat gebruikt ')

# variables
Ticket_totaal = int(Ticket_PP) * int(Aantal_Mensen)
Gameseat_Totaal = int(VIP_Gameseat_Pr5) * int(Tijd_Gameseat)
Totaal = (Gameseat_Totaal+Ticket_totaal)

# Sommen en Prints en shit

factuurtext = 'De prijs voor '+str(Aantal_Mensen) + ' mensen is per persoon '+str(Ticket_PP)+' is dus '+str(Ticket_totaal)+' totaal en de prijs van een VIP Gameseat is '+str(VIP_Gameseat_Pr5)+' per 5 minuten en de tijd dat we willen is ' + str(Tijd_Gameseat)+' is '+str(Gameseat_Totaal)+' dus het totale bedrag word '+str(Totaal)

print(factuurtext)