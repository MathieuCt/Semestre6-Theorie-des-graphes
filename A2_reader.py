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
    return listeContraintes