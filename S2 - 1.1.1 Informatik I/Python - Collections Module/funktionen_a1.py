# A1:
# Erstellen Sie eine Funktion, die eine Liste als Parameter übernimmt 
# und eine Liste mit Einträgen in umgekehrter Reihenfolge zurückgibt.

def dreheListeUm(alteListe):
    
    neueListe = []
    zähler = len(alteListe) - 1
    
    while zähler >= 0:
        neueListe.append(alteListe[zähler])
        zähler -= 1

    return neueListe