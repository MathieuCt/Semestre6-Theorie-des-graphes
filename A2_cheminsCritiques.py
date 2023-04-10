"""
Contient les fonctions pour calculer le(s) chemin(s) critique(s).
"""

import numpy as np
from A2_display import printChemin, printCheminsCritiques


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
        # Si la marge de l'activité est nulle, elle appartient au chemin critique
        if marges[i] == 0:
            chemin_critique.append(i)

    # On affiche le(s) chemin(s) critique(s)
    printCheminsCritiques()
    for tache in chemin_critique:
        chemin = [tache]
        temp = [tache]
        while temp:
            # On récupère la première tâche précédente de la liste temporaire
            tache_precedente = temp.pop(0)
            for i in range(nb_taches):
                # Si la tâche actuelle est précédente de la tâche précédente, elle appartient aussi au chemin critique
                if matrice[i][tache_precedente] == 1:
                    # On insère la tâche actuelle au début de la liste du chemin
                    chemin.insert(0, i)
                    # On ajoute la tâche actuelle à la liste temporaire pour chercher ses tâches précédentes
                    temp.append(i)
        printChemin(chemin)