"""
Contient les fonctions pour convertir la représentation d'un graphe vers une autre.
"""


import numpy as np
def contraintesVersMatriceValeurs(contraintes):
    """
    Convertit une matrice de contraintes en une matrice de valeurs.
    :param contraintes: Matrice de contraintes.
    :return: Matrice de valeurs.
    """
    # Créer une matrice de valeurs vide
    matriceValeurs = np.full([len(contraintes) + 2, len(contraintes)+ 2],-1)
    # Parcourir chaque ligne de la matrice de contraintes
    for i in range(0, len(contraintes)):
        for j in range(2, len(contraintes[i])):
            matriceValeurs[contraintes[i][j]][i+1] = contraintes[i][1]
    return matriceValeurs