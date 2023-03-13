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
    matriceValeurs = np.full([len(contraintes), len(contraintes)],-1)
    # Parcourir chaque ligne de la matrice de contraintes
    for i in range(0, len(contraintes)):
        for j in range(0, len(contraintes)):
            for k in contraintes[i][2:]:
                    if k == j:
                        matriceValeurs[i][j] = contraintes[i][1]
    print(matriceValeurs)
    return matriceValeurs