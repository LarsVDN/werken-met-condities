# Import system van package os en slaap module van time package
from os import system
from os import getlogin # Dit vraagt de gebruikersnaam van de gebruiker op
from sys import exit
from time import sleep

# Print naam van game
print("--------------------------------------------------")
print("                Unnamed space game                ")
print("--------------------------------------------------\n")

startBalans = 5000 # Quasi Universal Intergalactic Denomination (QUID)

# Taal selectie lets go
localization = input("Welke taal? / Which Language? (NL/EN): ")
system('cls')
if localization == 'nl' or localization == 'NL':
    # spelerNaam = input("Welkom bij de game, wat is uw spelersnaam?: ")
    system('cls')
    print("Welkom " + getlogin())
    doelSpel = input("Het doel van het spel is om de wereld te herstellen zoals het was voor dat de asteroïde insloeg.\nGa jij de mensheid redden? (J/N): ")
    system('cls')
    if doelSpel == 'j' or doelSpel == 'J':
        print("Ik wist dat ik op je kon rekenen")
        sleep(2.5)
        system('cls')
        print("Het is het jaar 2369, de aarde is verwoest door asteroïde Hygiea.\nAan jou is de taak om samen met je collegas op de maan instrumenten te maken om aarde te herstellen.\nAan boord zijn een aantal materialen beschikbaar maar je moet ook mineralen uit de grond halen.\n")
        sleep(1)
        print("Je moet nu een actie ondernemen\n")
        plaatsSelectie = input("1. Ga naar de mijn.\n2. Ga naar de hardware store om een laser te halen om mineralen op de graven.\n")
        if plaatsSelectie == "1":
            print("Mijn")
        elif plaatsSelectie == "2":
            print("----------Hardware Store----------\n")
            print("Wat heb je nodig?\n")
            koopHardware = input("1. Gigawatt Transmitter\n2. Minelaser \n3. Sorbet-ijs\n")
            if koopHardware == "1":
                print("Hier heb je niks aan.")
            elif koopHardware == "2":
                print("placeholder")
            elif koopHardware == "3":
                print("Hier heb je niks aan.")
    elif doelSpel == 'n' or doelSpel == 'N':
        print("Game stopt nu")
elif localization == 'en' or localization == 'EN':
    print("Work in progress")
else:
    print("Deze taal is niet in het spel. / This language is not available in the game")
