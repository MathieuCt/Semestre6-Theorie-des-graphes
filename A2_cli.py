'''Contient les fonctions d'interactions avec l'utilisateur.'''


def selection():
    
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
        printTable[i + 1].append(str(listeContraintes[i][0]))
        printTable[i + 1].append(str(listeContraintes[i][1]))
        for j in range(2, len(listeContraintes[i])):
            printTable[i + 1].append(str(listeContraintes[i][j]))
    print(printTable)
    
    return listeContraintes


def continuer():
    """
    Demande à l'utilisateur s'il veut continuer ou non.
    :return: 1 si l'utilisateur veut continuer, 0 sinon.
    """
    runtimeContinue = ""
    
    # Continuer tant que la réponse n'est pas valide
    while runtimeContinue != 'y' or 'Y' or 'n' or 'N':
        # Demander à l'utilisateur s'il veut continuer
        runtimeContinue = str(input("Voulez-vous lire un autre tableau ? y/n "))
        if runtimeContinue == 'y' or runtimeContinue == 'Y':
            # L'utilisateur veut continuer
            return 1
        elif runtimeContinue == 'n' or runtimeContinue == 'N':
            # L'utilisateur ne veut pas continuer
            return 0
        # L'utilisateur n'a pas entré une réponse valide
        print("Erreur de syntaxe. Veuillez entrer Y ou N., vous avez entré: " + "\""+ runtimeContinue+ "\"")