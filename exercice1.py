# -*-coding:Utf-8 -*
import os

# Acquisition des donnees
phrase = input("Veuillez saisir une phrase!")

# Restitution des donnees
print(""+phrase+" est une chaîne de caractère de type string")

#triage de la châine de caractère
chain=phrase.split()
print(chain)

# Preparation de l’arret
os.system("pause")