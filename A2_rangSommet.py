"""
Contient le calcul des rangs de chaque sommet.
"""
import copy
from A2_main import *

def rangSommet(S):
    r = 1
    s = copy.deepcopy(S)  # copie de la liste de contraintes prise en paramètre
    sommet = 0
    rang = np.zeros(shape=len(S))  # nouveau tableau qui prend la taille de la liste de contraintes prise en paramètres
                                   # ce tableau va contenir le rang de chaque sommet

    for i in range(0, len(s)):  # je calcule les sommets qui ont un rang 0
        if len(s[i]) == 2:
            rang[i] = 0
            sommet = s[i][0]
            for n in range(len(s)):
                for j in range(len(s[n])):
                    if s[n][j] == sommet:
                        s[n][j] = 0

    for k in range(0, len(s)):
        if len(s[k]) == 2:
            for a in range(len(s)):
                for b in range(2, len(s[a])):
                    if s[a][b] != 0:
                        break

    #for m in range(rang):
        #print("Le sommet ", m , "a pour rang ", rang[m], \n)


print(rangSommet(listeContraintes))
