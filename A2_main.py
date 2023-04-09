"""
Début
    Tant que l’utilisateur décide de tester un tableau de contraintes faire
        Choisir le tableau de contraintes à traiter
        Lire le tableau de contraintes sur fichier et le stocker en mémoire
        Créer la matrice correspondant au graphe représentant ce tableau de contraintes et l’afficher
        Vérifier que les propriétés nécessaires pour que ce graphe soit un graphe d’ordonnancement sont vérifiées
        SI oui alors
            Calculer les rangs des sommets et les afficher
            Calculer les calendriers au plus tôt et au plus tard et les afficher
            Calculer les marges et les afficher
            Calculer le(s) chemin(s) critique(s) et les afficher
        Sinon
            Proposer à l’utilisateur de changer de tableau de contraintes
    fin Tant que
Fin
"""
import numpy as np
from A2_display import *
from A2_dataConverter import *
from A2_calendrierMarges import *
from A2_cheminsCritiques import *
from A2_cli import *

# Tant que l’utilisateur décide de tester un tableau de contraintes faire
runtimeKey = 1
while runtimeKey:
    # Choix de l'utilisateur et construction du tableau de contrainte
    listeContraintes = selection()
    # Créer la matrice de valeurs
    matriceValeurs = contraintesVersMatriceValeurs(listeContraintes)
    # Afficher la matrice de valeurs
    printMat(matriceValeurs)

    """"
    printableTable = [["Num taches"], ["Durée"], ["Prédécesseurs"]]
    for i in range(1, nTasks-1):
        printableTable[0].append(str(listeContraintes[i-1][0]))
        printableTable[1].append(str(listeContraintes[i-1][1]))
        taskLength = len(listeContraintes[i-1])
        if taskLength == 3:
            printableTable[2].append(str(listeContraintes[i - 1][0]))
        elif taskLength > 3:
            printableTable[2].append(str(listeContraintes[i - 1][0]) + ", ")
            for u in range(2, taskLength):
                printableTable[2][i].join([str(listeContraintes[i-1][u]), spacer])
            printableTable[2][i].rstrip(", ")
    print(printableTable)
    """
    # Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges
    calendrierPlusTotPlusTardMarge(matriceValeurs)

    # Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges
    cheminsCritique(matriceValeurs)

    # Test utilisateur
    runtimeKey = continuer()

