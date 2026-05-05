"""Simulation attaque par force brute manuelle"""

import string


#caractères possibles
letter = string.printable[:3]

#fonctions qui affiche les combinaisons
def etape1():
    a = 0
    for i in range (3):
        passworld = letter[a]
        a += 1
        print(passworld)


def etape2():
    a = 0
    b = 0
    for i in range (9):
        if b == len(letter):
            b = 0
            a += 1
            
        passworld = letter[a] + letter[b]
        b += 1
        print(passworld)


def etape3():
    a = 0
    b = 0
    c = 0
    for i in range (27):
        if b == len(letter):
            b = 0
            a += 1
        if c == len(letter):
            b += 1
            c = 0
            
        passworld = letter[a] + letter[b] + letter[c]
        c += 1
        print(passworld)

#Boucle principale
etape1()
etape2()
etape3()
