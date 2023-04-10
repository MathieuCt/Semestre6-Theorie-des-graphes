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
            for j in range(2, len(listeContraintes[i])-1):
                txtfile.write(str(listeContraintes[i][j])+";")
                print(str(listeContraintes[i][j]), end=";")
            # Imprimer la dernière contrainte
            txtfile.write(str(listeContraintes[i][len(listeContraintes[i])-1]))
            print(str(listeContraintes[i][len(listeContraintes[i])-1]))
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


def printOrdonnancemant(circuit, neg):
    """
    Affichee le raisonnemant pour conclure si le graphe est un graphe d'ordonnancement
    """
    # Ouvrir le fichier
    with open(filename, "a",encoding='utf-8') as txtfile:
        # Afficher le raisonnement
        print(" \n # Ordonnancement : \n")
        txtfile.write(" \n # Ordonnancement : \n\n")
        # Afficher si il y a un circuit et si il y a un arc à valeur négative
        if(circuit == True):
            txtfile.write(" - il n'y a pas de citcuit\n")
            print(" - Il n'y a pas de circuit")
        else:
            txtfile.write(" - il y a un circuit\n")
            print(" - Il y a un circuit")
        if(neg == True):
            txtfile.write(" - Il n'y a pas d'arc à valeur négative\n")
            print(" - Il n'y a pas d'arc à valeur négative")
        else:
            txtfile.write(" - Il y a un arc à valeur négative\n")
            print(" - Il y a un arc à valeur négative")
        # Afficher la conclusion
        if(circuit == True and neg == True):
            txtfile.write("Donc le graphe est un graphe d'ordonnancement\n")
            print("Donc le graphe est un graphe d'ordonnancement")
        else:
            txtfile.write("Donc le graphe n'est pas un graphe d'ordonnancement\n")
            print("Donc le graphe n'est pas un graphe d'ordonnancement")
    txtfile.close()


def printRang(rang):
    """
    Affiche le rang de chaque sommet
    """
    with open(filename, "a",encoding='utf-8') as txtfile:
        print(" \n # Rangs : \n")
        txtfile.write(" \n # Rangs : \n\n")
        for m in range(0, len(rang)):
            txtfile.write("Le sommet "+ str(m + 1)+ " a pour rang "+ str(rang[m]) + "\n")
            print("Le sommet", m + 1, "a pour rang", rang[m])
    txtfile.close()


def printCalendrier(plus_tot, plus_tard, marges):
    """
    Afficher les calendriers au plus tôt, au plus tard et les marges
    """
    with open(filename, "a", encoding="utf-8") as txtfile:
        print("\n # Calendrier et marges : \n")
        txtfile.write("\n # Calendrier et marges : \n")
        # Calendrier au plus tôt
        print("Calendrier au plus tôt : ",end="")
        txtfile.write("\nCalendrier au plus tôt : ")
        for i in range(len(plus_tot)-1):
            print(str(plus_tot[i])+", ",end="")
            txtfile.write(str(plus_tot[i])+", ")
        print(str(plus_tot[len(plus_tot)-1]))
        txtfile.write(str(plus_tot[len(plus_tot)-1]))
        # Calendrier au plus tard
        print("Calendrier au plus tôt : ",end="")
        txtfile.write("\nCalendrier au plus tôt : ")
        for i in range(len(plus_tard)-1):
            print(str(plus_tard[i])+", ", end="")
            txtfile.write(str(plus_tard[i])+", ")
        print(str(plus_tard[len(plus_tard)-1]))
        txtfile.write(str(plus_tard[len(plus_tard)-1]))
        # Marges
        txtfile.write("\nMarges : ")
        print("Marges : ", end="")
        for i in range(len(marges)-1):
            print(str(marges[i])+", ", end="")
            txtfile.write(str(marges[i])+", ")
        print(str(marges[len(marges)-1]))
        txtfile.write(str(marges[len(marges)-1]))


def printCheminsCritiques():
    """
    Affiche le chemin critique
    """
    with open(filename, "a",encoding='utf-8') as txtfile:
        txtfile.write("\n\n # Chemin critique : \n\n")
        print("\n # Chemin critique : \n")
    txtfile.close()

def printChemin(chemin):
    """
    Affiche un chemin
    """
    with open(filename, "a",encoding='utf-8') as txtfile:
        for i in range(0, len(chemin)):
            txtfile.write(str(chemin[i]) + " ")
            print(str(chemin[i]), end=" ")
        txtfile.write("\n")
        print()
    txtfile.close()


def printSeparateur():
    with open(filename, "a",encoding='utf-8') as txtfile:
        print("\n=======================================\n")
        txtfile.write("\n=======================================\n")
    txtfile.close()