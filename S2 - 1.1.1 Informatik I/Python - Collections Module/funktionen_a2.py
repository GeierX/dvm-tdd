# A2:
# Erstellen Sie eine Funktion, die als Parameter eine Liste mit 
# Einträgen von Typen "str", "int", "float", und "bool" übernimmt.
# Diese Einträge sollen, nach Typ sortiert, als Dictionary zurückgegeben werden.

def erstelleDictionarySortiertNachTyp(liste):

    dictionary = {}

    for eintrag in liste:

        typ = type(eintrag)
        if typ == str:
            typ = "str"
        elif typ == int:
            typ = "int"
        elif typ == float:
            typ = "float"
        elif typ == bool:
            typ = "bool"

        if typ not in dictionary:
            dictionary[typ] = []

        dictionary[typ].append(eintrag)

    return dictionary

def erstelleDictionarySortiertNachTyp2(liste):

    dictionary = {}
    zuordnungen = {
        str: "str",
        int: "int",
        float: "float",
        bool: "bool"
    }

    for eintrag in liste:

        typ = type(eintrag)
        if typ not in zuordnungen:
            continue

        typAlsString = zuordnungen[typ]

        if typAlsString not in dictionary:
            dictionary[typAlsString] = []

        dictionary[typAlsString].append(eintrag)

    return dictionary