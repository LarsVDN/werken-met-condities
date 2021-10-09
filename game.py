print("--------------------------------------------------")
print("                 Unnamed game                     ")
print("--------------------------------------------------")

taal = input("Welke taal? / Which Language? (NL/EN): ")
if taal == 'nl' or taal == 'NL':
    spelerNaam = input("Welkom bij de game, wat is uw spelersnaam?: ")
    print("Welkom bij de game " + spelerNaam)
elif taal == 'en' or taal == 'EN':
    print("Work in progress")
else:
    print("Deze taal is niet in het spel. / This language is not available in the game")
