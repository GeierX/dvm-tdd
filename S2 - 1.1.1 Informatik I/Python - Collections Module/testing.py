from funktionen_a1 import dreheListeUm
from funktionen_a2 import erstelleDictionarySortiertNachTyp, erstelleDictionarySortiertNachTyp2
from funktionen_a3 import stringsPerBuchstabe
from funktionen_a4 import summeAllerZahlen

liste = ["Anton", "Berta", "Bea", 20, 10, 0.02, True]

a1 = dreheListeUm(liste)

a2 = erstelleDictionarySortiertNachTyp(liste)
a2b = erstelleDictionarySortiertNachTyp2(liste)

a3 = stringsPerBuchstabe(liste)

a4 = summeAllerZahlen(liste)