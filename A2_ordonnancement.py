"""
Permet de dire si un graphe peut servir de graphe d'ordonnancement.
"""

import numpy as np

def ordonnancement(matriceValeurs):
    """
    Vérifie si un graphe est un graphe d'ordonnancemeant.
    :param matriceValeurs: Matrice de valeurs.
    :return: True si le graphe est ordonnanble, False sinon.
    """
    # Un graphe est un graphe d'ordonnancement si il ne contient pas de circuit et si il ne contient pas d'arc à valeurs négatives.
    print( "circuit(matriceValeurs) = " + str(circuit(matriceValeurs)))
    print( "arcNegatif(matriceValeurs) = " + str(arcNegatif(matriceValeurs)))
    if circuit(matriceValeurs) and arcNegatif(matriceValeurs):
        return True
    return False

def circuit(matriceValeurs):
    """
    Vérifie si un graphe contient un circuit.
    :param matriceValeurs: Matrice de valeurs.
    :return: True si le graphe contient un circuit, False sinon.
    """
    # Calcul de la matrice de la fermeture transitive du graphe par la méthode de Roy-Warshall
    # Taille de la matrice (carrée)
    n = len(matriceValeurs)
    # Construction de la matrice binaire à partir de la matrice de valeurs
    C = np.zeros((n,n))
    for i in range(0, n):
        for j in range(0, n):
            if matriceValeurs[i][j] == -1:
                C[i][j] = 0
            else:
                C[i][j] = 1
    # Parcours des sommets
    for k in range (0, n-1):            
        for i in range(0, n-1):            
            for j in range(0, n-1):
                C[i][j] = C[i][j] or (C[i][k] and C[k][j])
    # Vérification qu'il n'y a pas de circuit
    # Il y a un circuit s'il existe un sommet i tel que C[i,i] = 1
    for i in range(0, n-1):
        if C[i][i] == 1:
            print( "Il y a un circuit" )
            return False

    return True



def arcNegatif(matriceValeurs):
    """
    Vérifie si un graphe contient un arc négatif.
    :param matriceValeurs: Matrice de valeurs.
    :return: True si le graphe contient un arc négatif, False sinon.
    """
    # Parcours de la matrice de valeurs
    for i in range(0, len(matriceValeurs)):
        for j in range(0, len(matriceValeurs)):
            if matriceValeurs[i][j] < -1:
                print("Il y a un arc négatif")
                return False
    return True