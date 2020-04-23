__author__ = 'Florian Cassayre'

from copy import copy, deepcopy


def inverse(toInverse):
    size = len(toInverse)

    matrix = [[0 for j in range(size * 2)] for i in range(size)] # Matrice n x 2n

    for i in range(size): # On copie la matrice à inverser
        for j in range(size):
            matrix[i][j] = toInverse[i][j]

    for i in range(size): # On ajoute la matrice identité
        matrix[i][i + size] = 1

    matrix = gaussJordanElimination(matrix) # On échelonne

    if isZero(matrix[size - 1][size - 1]):
        return None

    inverted = [[0 for j in range(size)] for i in range(size)]
    for i in range(size): # On récupère notre inverse
        for j in range(size):
            inverted[i][j] = matrix[i][j + size]

    return inverted

def gaussJordanElimination(matrix):
    lines = len(matrix)
    columns = len(matrix[0])

    copy = deepcopy(matrix) # Copie la matrice pour éviter de modifier l'original

    r = -1

    for j in range(columns):

        k = r + 1

        for i in range(r + 1, lines): # Trouver la valeur maximale de la colonne
            if(not isZero(copy[i][j])):
                k = i
        if(k >= lines): # On sort dès qu'on a fait toutes les lignes
            break

        if(not isZero(copy[k][j])):
            r += 1
            pivotDivider = copy[k][j]
            for j1 in range(columns): # Division de la ligne
                copy[k][j1] = copy[k][j1] / pivotDivider

            tempLine = copy[k] # Echange de deux lignes en trois étapes
            copy[k] = copy[r]
            copy[r] = tempLine

            for i in range(lines): # Réduction des autres lignes
                lineDivider = copy[i][j]
                if(i != r):
                    for j1 in range(columns):
                        copy[i][j1] -= copy[r][j1] * lineDivider

    return copy

def isZero(number):
    return abs(number) < 1E-10

# Tests

size = 3

# On souhaite inverser la matrice suivante :

toInverse = [[0 for j in range(size)] for i in range(size)]
toInverse[0] = [1, 2, 3]
toInverse[1] = [4, 5, 6]
toInverse[2] = [7, 8, 9]

print(inverse(toInverse)) # "None" car la matrice n'est pas inversible !