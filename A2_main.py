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
from A2_reader import reader
from A2_display import printContraintes, printVal
from A2_dataConverter import *
from A2_calendrierMarges import *
from A2_cheminsCritiques import *
from A2_cli import *

# Tant que l’utilisateur décide de tester un tableau de contraintes faire
runtimeKey = 1
while runtimeKey:
    # Choix de l'utilisateur et construction du tableau de contrainte
    txtnum = selection()
    # Créer la matrice de containtes
    listeContraintes = reader(txtnum)
    printContraintes(listeContraintes)
    # Créer la matrice de valeurs
    matriceValeurs = contraintesVersMatriceValeurs(listeContraintes)
    printVal(matriceValeurs)
    # Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges
    calendrierPlusTotPlusTardMarge(matriceValeurs)
    # Calculer le calendrier au plus tôt, le calendrier au plus tard et les marges
    cheminsCritique(matriceValeurs)
    # Test utilisateur
    runtimeKey = continuer()

