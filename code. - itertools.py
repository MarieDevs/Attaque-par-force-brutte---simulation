"""Simulation d'une attaque par force brute"""

import string
import itertools

#chemin d'acces du fichier
FICHIER = "C:\\Users\\Geek\\Desktop\\Python\\Attaque force brute\\code.txt"

#caractères possibles
letter = string.printable[:5]

#Boucle principale qui calcule les combinaisons
for length in range(1,6):
    for combo in itertools.product(letter, repeat = length):
        passworld = "".join(combo)
        with open (FICHIER, "w") as f:
            f.write(passworld)
            f.write("\n")


print("Tache effectuee")
        
        
