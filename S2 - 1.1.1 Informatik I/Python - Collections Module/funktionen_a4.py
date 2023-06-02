# A4:
# Erstellen Sie eine Funktion, die als Parameter 
# eine Liste mit Einträgen von verschiedenen Typen übernimmt. 
# Zurückgegeben soll die Summe aller Einträge, die eine Zahl sind.

def summeAllerZahlen(liste):

    summe = 0.0

    for eintrag in liste:
        if type(eintrag) in (int, float):
            summe += eintrag

    return summe