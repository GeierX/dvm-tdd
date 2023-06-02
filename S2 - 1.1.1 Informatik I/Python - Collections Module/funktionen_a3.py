# A3:
# Erstellen Sie eine Funktion, die als Parameter 
# eine Liste mit Einträgen von verschiedenen Typen übernimmt. 
# Zurückgegeben soll eine Dictionary, die nur Einträge vom Typ "str" enthält, 
# wobei diese nach Anfangsbuchstabe sortiert sein soll.

def stringsPerBuchstabe(liste):

    dictionary = {}

    for eintrag in liste:
        if type(eintrag) != str:
            continue

        ersterBuchstabe = eintrag[0]
        if ersterBuchstabe not in dictionary:
            dictionary[ersterBuchstabe] = []

        dictionary[ersterBuchstabe].append(eintrag)

    return dictionary