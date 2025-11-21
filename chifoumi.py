import random

# Constantes du jeu (les choix possibles)
PIERRE = "pierre"
FEUILLE = "feuille"
CISEAUX = "ciseaux"

def demander_choix_joueur(): 
    choix_valides = [PIERRE, FEUILLE, CISEAUX]
    while True:
        choix = input("Choisissez (pierre/feuille/ciseaux) : ")
        
        # Convertir en minuscules pour accepter "Pierre", "PIERRE", etc.
        choix = choix.lower()
        
        # Vérifier si le choix est valide
        if choix in choix_valides:
            return choix
        else:
            print("Choix non valide...")

def choix_ordinateur():
    # Créer une liste avec les trois choix possibles
    choix_possibles = [PIERRE, FEUILLE, CISEAUX]
    choix_ordinateur = random.choice(choix_possibles)
    
    return choix_ordinateur

def determiner_gagnant(choix_joueur, choix_ordi):
    
    # Cas 1 : Égalité (même choix)
    if choix_joueur == choix_ordi:
        return "egalite"
    
    # Cas 2 : Le joueur gagne
    # Pierre bat Ciseaux
    if choix_joueur == PIERRE and choix_ordi == CISEAUX or choix_ordi == PIERRE and choix_joueur == CISEAUX:
        if choix_joueur == PIERRE:
            return "joueur"
        else :
            return "ordinateur"
    
    # Feuille bat Pierre
    if choix_joueur == FEUILLE and choix_ordi == PIERRE or choix_ordi == FEUILLE and choix_joueur == PIERRE:
        if choix_joueur == FEUILLE:
            return "joueur"
        else :
            return "ordinateur"
    
    # Ciseaux bat Feuille
    if choix_joueur == FEUILLE and choix_ordi == CISEAUX or choix_ordi == FEUILLE and choix_joueur == CISEAUX:
        if choix_joueur == CISEAUX:
            return "joueur"
        else :
            return "ordinateur"

def afficher_resultat(resultat, choix_joueur, choix_ordi):
    
    # Afficher les choix
    print(f"\nVous avez choisi : {choix_joueur}")
    print(f"L'ordinateur a choisi : {choix_ordi}")
    print()  # Ligne vide pour la lisibilité
    
    # Afficher le résultat selon le cas
    if resultat == "egalite":
        print("Match nul !")
    
    elif resultat == "joueur":
        print(choix_joueur + " bat " + choix_ordi)
        print("Vous avez gagné ! 🎉")
    
    else:
        print(choix_ordi + " bat " + choix_joueur)
        print("L'ordinateur a gagné !")



def jouer_une_partie():
    # Afficher le titre
    print("=" * 40)
    print("    PIERRE - FEUILLE - CISEAUX")
    print("=" * 40)
    print()
    
    # 1. Demander le choix du joueur
    choix_joueur = demander_choix_joueur()
    
    # 2. Faire choisir l'ordinateur
    choix_ordi = choix_ordinateur()
    
    # 3. Déterminer le gagnant
    resultat = determiner_gagnant(choix_joueur, choix_ordi)
    
    # 4. Afficher le résultat
    afficher_resultat(resultat, choix_joueur, choix_ordi)
    print()
    print("=" * 40)
    rejouer = input("Voulez vous rejouer ? (oui/non) :  ")
    rejouer.lower()
    if rejouer == "oui":
        jouer_une_partie()


# Lancement du jeu
jouer_une_partie()
