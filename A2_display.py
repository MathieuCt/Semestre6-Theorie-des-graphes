"""
Ces fonctions sont utilisées pour afficher les sorties du projet.
"""


def printContraintes(listeContraintes):
    """
    Affiche la liste des contraintes
    :param listeContraintes: Liste des contraintes
    :return:
    """
    print(" \n # Liste des contriantes : \n")
    # Afficher l'en-tête
    print("Numéro ", "|Durée ", "|Contraintes")
    # Parcourir la liste de contrainte
    for i in range(0, len(listeContraintes)):
        # Imprimer le numéro et la durée en ajustant les espaces
        print(str(listeContraintes[i][0]) + " "*(7-len(str(listeContraintes[i][0]))), "|" + str(listeContraintes[i][1])+ " "*(7-len(str(listeContraintes[i][1]))) + "|", end="")
        # Imprimer les contraintes
        for j in range(2, len(listeContraintes[i])):
            print(str(listeContraintes[i][j]), end=";")
        # Retour à la ligne
        print()



def printVal(matrice):
    """
    Affiche une matrice de valeur.
    :param matrice:
    :return:
    """
    print("\n # Matrice de valeurs :\n")
    # Pour laisser les bons espaces entre les colonnes on cherche la valeur avec le plus de chiffres
    maxVal = 0
    for i in range(0, len(matrice)):
        for j in range(0, len(matrice[i])):
            if len(str(matrice[i][j])) > maxVal:
                maxVal = len(str(matrice[i][j]))
    # Afficher la matrice
    # Afficher l'entête
    print("".rjust(maxVal), end=" ")
    for i in range(0, len(matrice)):
        print(str(i).rjust(maxVal), end=" ")
    # Afficher les valeurs
    print()
    for i in range(0, len(matrice)):
        # Afficher le numéro de la tâche
        print(str(i).rjust(maxVal), end=" ")
        # Afficher les valeurs
        for j in range(0, len(matrice[i])):
            if matrice[i][j] == -1:
                print("*".rjust(maxVal), end=" ")
            else :
                print(str(matrice[i][j]).rjust(maxVal), end=" ")
        print()

