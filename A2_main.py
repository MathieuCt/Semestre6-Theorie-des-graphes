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
import A2_display

# Tant que l’utilisateur décide de tester un tableau de contraintes faire
runtimeKey = 1
while runtimeKey:
    # Choisir le tableau de contraintes à traiter
    selectTable = int(input("Choisir le tableau à faire (1-12): "))
    while (selectTable < 1) or (selectTable > 12):
        print("Entrée invalide. Veuillez réessayer.\n")
        selectTable = int(input("Choisir le tableau à faire (1-12): "))
    # Lire le tableau de contraintes sur fichier et le stocker en mémoire
    filename = "Graphes/table " + str(selectTable) + ".txt"
    # Ouvrir le fichier et lire son contenu
    with open(filename, "r") as f:
        lignes = f.readlines()
    # Créer la matrice correspondant au graphe représentant ce tableau de contraintes et l’afficher
    listeContraintes = []
    # Parcourir chaque ligne du fichier
    for ligne in lignes:
        # Diviser la ligne en une liste de nombres
        nombres = ligne.strip().split()
        # Convertir chaque nombre en entier
        nombres = [int(n) for n in nombres]
        # Ajouter la liste de nombres à la matarice de contraintes
        listeContraintes.append(nombres)
    # Afficher la matrice de contraintes en liste
    print(listeContraintes)
    nTasks = listeContraintes[-1][0]
    taskAlpha = []
    taskOmega = []
    spacer = ", "
    printTable = [["Num taches", "Durée", "Prédécesseurs"]]
    print()
    for i in range(0, len(listeContraintes)):
        printTable.append([])
        printTable[i+1].append(str(listeContraintes[i][0]))
        printTable[i+1].append(str(listeContraintes[i][1]))
        for j in range(2, len(listeContraintes[i])):
            printTable[i+1].append(str(listeContraintes[i][j]))
    print(printTable)

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




    # Test utilisateur
    runtimeContinue = str(input("Voulez-vous lire un autre tableau ? y/n "))
    if runtimeContinue == 'y' or runtimeContinue == 'Y':
        runtimeKey = 1
    elif runtimeContinue == 'n' or runtimeContinue == 'N':
        runtimeKey = 0
    else:
        while runtimeContinue != 'y' or 'Y' or 'n' or 'N':
            print("Erreur de syntaxe. Veuillez entrer Y ou N.")
            runtimeContinue = str(input("Voulez-vous lire un autre tableau ? y/n "))
