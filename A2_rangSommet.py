import numpy as np

def rangSommet(S):
    r = 0
    s = np.array(S)
    rang = np.array(S)

    for m in range(0, len(s)):
        nb_sommets = nb_sommets + 1
    # je parcours toute la première colonne du tableau
    # pour savoir combien possède le tableau de sommets
    # je mets le nombre de sommets dans nb_sommets

    for i in range(0, len(s)):
        for j in range(0, len(s)):
            for k in s[i][2:]:
                if s[i][2] is None:
                    rang[i] = r
                if s[i][k] == s[i][0]:
                    np.delete(s, k)

    for m in range(rang):
        print(rang[m])

