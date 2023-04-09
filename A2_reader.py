"""
Lis un fichier le fichier txt au numéro indiqué par l'utilisateur et retourne une liste de contraintes.
"""

def reader(txtNum):
    # Lire le tableau de contraintes sur fichier et le stocker en mémoire
    filename = "Graphes/table " + str(txtNum) + ".txt"
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
    """
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
        printTable[i + 1].append(str(listeContraintes[i][0]))
        printTable[i + 1].append(str(listeContraintes[i][1]))
        for j in range(2, len(listeContraintes[i])):
            printTable[i + 1].append(str(listeContraintes[i][j]))
    print(printTable)
    """
    return listeContraintes