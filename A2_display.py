"""
Ces fonctions sont utilisées pour afficher les sorties du projet.
"""


def printMat(matrice):
    """
    Affiche une matrice de valeur.
    :param matrice:
    :return:
    """
    # Pour laisser les bons espaces entre les colonnes on cherche la valeur avec le plus de chiffres
    maxVal = 0
    for i in range(0, len(matrice)):
        for j in range(0, len(matrice[i])):
            if len(str(matrice[i][j])) > maxVal:
                maxVal = len(str(matrice[i][j]))
    # Afficher la matrice
    for i in range(0, len(matrice)):
        for j in range(0, len(matrice[i])):
            print(str(matrice[i][j]).rjust(maxVal), end=" ")

