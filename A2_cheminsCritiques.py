"""
Contient les fonctions pour calculer le(s) chemin(s) critique(s) et les afficher.
"""

import numpy as np


def cheminsCritique(matrice):
    """
    Calculer le(s) chemin(s) critique(s) et les afficher.
    :param matrice:
    :return: chemin(s) critique(s).
    """
    nb_taches = len(matrice)
    marges = np.zeros(nb_taches)

    # On trouve les tâches qui sont sur le(s) chemin(s) critique(s)
    chemin_critique = []
    for i in range(nb_taches):
        if marges[i] == 0:
            chemin_critique.append(i)

    # On affiche le(s) chemin(s) critique(s)
    print("\nChemin(s) critique(s):")
    for tache in chemin_critique:
        chemin = [tache]
        temp = [tache]
        while temp:
            tache_precedente = temp.pop(0)
            for i in range(nb_taches):
                if matrice[i][tache_precedente] == 1:
                    chemin.insert(0, i)
                    temp.append(i)
        print(chemin)
