"""
Contient les fonctions pour calculer le calendrier au plus tôt, au plus tard et les marges.
"""


import numpy as np

def calendrierPlusTotPlusTardMarge(matrice):
    """
    Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges.
    :param matrice:
    :return: calendrier au plus tôt, calendrier au plus tard et marges.
    """
    nb_activites = len(matrice)
    plus_tot = [0] * nb_activites  # Initialisation du calendrier au plus tôt
    plus_tard = [0] * nb_activites  # Initialisation du calendrier au plus tard
    marges = [0] * nb_activites  # Initialisation des marges

    # Calcul du calendrier au plus tôt
    for i in range(nb_activites):
        max_date = 0
        # Parcours des activités précédentes
        for j in range(i):
            # Calcul de la date la plus élevée possible à laquelle l'activité actuelle peut être terminée
            date = plus_tot[j] + matrice[j][i]
            if date > max_date:
                max_date = date
        plus_tot[i] = max_date  # Mise à jour de la date au plus tôt de l'activité actuelle

    # Calcul du calendrier au plus tard
    plus_tard[-1] = plus_tot[-1]  # La date au plus tard de la dernière activité est égale à sa date au plus tôt
    # Parcours des activités en ordre inverse
    for i in range(nb_activites - 2, -1, -1):
        min_date = plus_tard[-1]
        # Parcours des activités suivantes
        for j in range(nb_activites - 1, i, -1):
            # Calcul de la date la plus basse possible à laquelle l'activité actuelle doit être terminée sans retarder la date de fin du projet
            date = plus_tard[j] - matrice[i][j]
            if date < min_date:
                min_date = date
        plus_tard[i] = min_date  # Mise à jour de la date au plus tard de l'activité actuelle

    # Calcul des marges
    for i in range(nb_activites):
        marges[i] = plus_tard[i] - plus_tot[i]

    print("\nCalendrier au plus tôt:", plus_tot)
    print("Calendrier au plus tard:", plus_tard)
    print("Marges:", marges)
