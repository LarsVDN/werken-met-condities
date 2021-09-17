# kaasGeel = "Is de kaas geel? (ja/nee): "
# kaasGaten = "Zitten er gaten in? (ja/nee): "
# kaasDuur = "Is de kaas belachelijk duur? (ja/nee): "
# kaasSchimmels = "Heeft de kaas blauwe schimmels? (ja/nee): "
# kaasHard = "Is de kaas hard als steen? (ja/nee): "
# kaasKorst = "Heeft de kaas een korst? (ja/nee): "

# bovenstaande regels waren er om te onthouden welke vragen er gesteld worden


kaasGeel = input("Is de kaas geel? (ja/nee): ")
if kaasGeel == 'ja':
    kaasGaten = input("Zitten er gaten in? (ja/nee): ")
    if kaasGaten == 'ja':
        kaasDuur = input("Is de kaas belachelijk duur? (ja/nee): ")
        if kaasDuur == 'ja':
            print("De kaas is Emmenthaler")
        if kaasDuur == 'nee':
            print("De kaas is Leerdammer")
    else:
        kaasHard = input("Is de kaas hard als steen? (ja/nee): ")
        if kaasHard == 'ja':
            print("De kaas is Parmigiano Reggiano")
        if kaasHard == 'nee':
            print("De kaas is Goudse Kaas")
else:
    kaasSchimmels = input("Heeft de kaas blauwe schimmels? (ja/nee): ")
    if kaasSchimmels == 'ja':
        kaasKorst = input("Heeft de kaas een korst? (ja/nee): ")
        if kaasKorst == 'ja':
            print("De kaas is Bleu de Rochbaron")
        if kaasKorst == 'nee':
            print("De kaas is fourme d'ambert")
    if kaasSchimmels == 'nee':
        kaasKorst = input("Heeft de kaas een korst? (ja/nee): ")
        if kaasKorst == 'ja':
            print("De kaas is camembert")
        if kaasKorst == 'nee':
            print("De kaas is Mozzarella")
