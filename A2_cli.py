'''Contient les fonctions d'interactions avec l'utilisateur.'''


def selection():
    """
    Demande à l'utilisateur de choisir un fichier txt.
    :return: Le numéro du fichier txt choisi.
    """
    # Choisir le tableau de contraintes à traiter
    while True:
        # Demander à l'utilisateur de choisir un fichier txt
        reponse = input("Choisir le tableau à faire (1-12): ")
        # Si la fonction est un numéro entre 1 et 12, retourner ce numéro
        if reponse.isdigit():
            if int(reponse) in range(1, 13):
                return int(reponse)
        print("Entrée invalide. Veuillez réessayer.\n")




def continuer():
    """
    Demande à l'utilisateur s'il veut continuer ou non.
    :return: 1 si l'utilisateur veut continuer, 0 sinon.
    """
    # Continuer tant que la réponse n'est pas valide
    while True:
        # Demander à l'utilisateur s'il veut continuer
        runtimeContinue = str(input("Voulez-vous lire un autre tableau ? y/n "))
        if runtimeContinue == 'y' or runtimeContinue == 'Y':
            # L'utilisateur veut continuer
            return 1
        elif runtimeContinue == 'n' or runtimeContinue == 'N':
            # L'utilisateur ne veut pas continuer
            return 0
        # L'utilisateur n'a pas entré une réponse valide
        print("Erreur de syntaxe. Veuillez entrer Y ou N.")