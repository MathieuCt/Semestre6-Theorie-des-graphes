"""
Ces fonctions sont utilisées pour afficher les sorties du projet.
"""
# Constante de temps pour nommer les fichiers
from datetime import datetime
txtName = datetime.now().strftime("%Y%m%d-%H%M%S")
filename = "Execution/" + str(txtName) + ".txt"

def printContraintes(listeContraintes):
    """
    Affiche la liste des contraintes, et les ecris dans le fichier
    Toutes les instructions sont écrites en parallèle dans le fichier et dans le terminal
    :param listeContraintes: Liste des contraintes
    :return:
    """
    # ouvrire le fichier
    with open(filename, "a", encoding='utf-8') as txtfile:
        print(" \n # Liste des contraintes : \n")
        txtfile.write(" \n # Liste des contraintes : \n\n")
        # Afficher l'en-tête
        print("Numéro ", "|Durée ", "|Contraintes")
        txtfile.write("Numéro "+ "|Durée "+ "|Contraintes" + "\n")
        # Parcourir la liste de contrainte
        for i in range(0, len(listeContraintes)):
            # Imprimer le numéro et la durée en ajustant les espaces
            print(str(listeContraintes[i][0]) + " "*(7-len(str(listeContraintes[i][0]))), "|" + str(listeContraintes[i][1])+ " "*(7-len(str(listeContraintes[i][1]))) + "|", end="")
            txtfile.write(str(listeContraintes[i][0]) + " "*(7-len(str(listeContraintes[i][0])))+ "|" + str(listeContraintes[i][1])+ " "*(6-len(str(listeContraintes[i][1]))) + "|" )
            # Imprimer les contraintes
            for j in range(2, len(listeContraintes[i])):
                txtfile.write(str(listeContraintes[i][j])+";")
                print(str(listeContraintes[i][j]), end=";")
            # Retour à la ligne
            print()
            txtfile.write("\n")
    txtfile.close()



def printVal(matrice):
    """
    Affiche une matrice de valeur.
    :param matrice:
    :return:
    """
    with open(filename, "a",encoding='utf-8') as txtfile:
        txtfile.write("\n # Matrice de valeurs :\n")
        print("\n # Matrice de valeurs :\n")
        # Pour laisser les bons espaces entre les colonnes on cherche la valeur avec le plus de chiffres
        maxVal = 0
        for i in range(0, len(matrice)):
            for j in range(0, len(matrice[i])):
                if len(str(matrice[i][j])) > maxVal:
                    maxVal = len(str(matrice[i][j]))
        # Afficher la matrice
        # Afficher l'entête
        txtfile.write("\n"+"".rjust(maxVal)+ "")
        print("".rjust(maxVal), end=" ")
        for i in range(0, len(matrice)):
            txtfile.write(str(i).rjust(maxVal)+ " ")
            print(str(i).rjust(maxVal), end=" ")
        # Afficher les valeurs
        txtfile.write("\n")
        print()
        for i in range(0, len(matrice)):
            # Afficher le numéro de la tâche
            txtfile.write(str(i).rjust(maxVal))
            print(str(i).rjust(maxVal), end=" ")
            # Afficher les valeurs
            for j in range(0, len(matrice[i])):
                if matrice[i][j] == -1:
                    txtfile.write("*".rjust(maxVal)+ " ")
                    print("*".rjust(maxVal), end=" ")
                else :
                    txtfile.write(str(matrice[i][j]).rjust(maxVal)+ " ")
                    print(str(matrice[i][j]).rjust(maxVal), end=" ")
            txtfile.write("\n")
            print()
    txtfile.close()


def printNum(txtNum):
    """
    Afficher le numéro de la matrice choisie par l'utilisateur
    """
    # Ouvrir le fichier
    with open(filename, "a",encoding='utf-8') as txtfile:
        # Afficher le numéro de la matrice
        print(" \n # Numéro de la matrice : " + str(txtNum) + "\n")
        txtfile.write(" \n # Numéro de la matrice : " + str(txtNum) + "\n")
    txtfile.close()