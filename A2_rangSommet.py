"""
Contient le calcul des rangs de chaque sommet.
"""
import copy
import numpy as np


# 1. Créer un tableau avec tous les rangs initialisés à -1, r = 0
# 2. tant qu'il y a un rang qui contient -1, boucle
# 3. copie de S dans une nouvelle variable
# 4. Si notre taille, c'est 2 -> on met le rang, et pour tous les vertices qui le continennent on met 0
# 5. faire une autre boucle après les modifications et del tous les nombres qui ont 0
# 6. r = r+1

def rangSommet(S):
    r = 0
    s = copy.deepcopy(S)  # copie de la liste de contraintes prise en paramètre
    rang = np.full(len(S), -1)  # nouveau tableau qui prend la taille de la liste de contraintes prise en paramètres
                                # ce tableau va contenir le rang de chaque sommet

    while -1 in rang:
        for i in range(len(s)):  # calcul des rangs de chaque sommets
            if len(s[i]) == 2 and rang[i] == -1:
                rang[i] = r
                for n in range(len(s)):
                    for j in range(2, len(s[n])):
                        if s[n][j] == s[i][0]:
                            s[n][j] = 0

        for k in range(len(s)):
            b = 2
            while b < len(s[k]):
                if s[k][b] == 0:
                    del s[k][b]
                else:
                    b = b + 1
        r = r + 1

    for m in range(len(rang)):
        print("Le sommet", m + 1, "a pour rang", rang[m])
