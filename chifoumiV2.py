import random
import tkinter as tk  # on importe tkinter
from tkinter import ttk

version = "v0.0.1"

score_joueur = 0
score_ordinateur = 0

# Constantes du jeu (les choix possibles)
PIERRE = "pierre"
FEUILLE = "feuille"
CISEAUX = "ciseaux"


def demander_choix_joueur(): 
    choix_valides = [PIERRE, FEUILLE, CISEAUX]

    label_text.config(text="Choisissez une arme :")

    variable = tk.StringVar(value=choix_valides[0])

    choix_menu = tk.OptionMenu(root, variable, *choix_valides)
    choix_menu.grid(row=15, column=0, pady=0)

    root.wait_variable(variable)  # Attendre que l'utilisateur fasse un choix

    choix = variable.get()

    choix_menu.destroy()
    label_text.config(text="")

    return choix

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
    label_text.config(text="Vous avez choisi : " + choix_joueur)
    label_text2.config(text="L'ordinateur a choisi : " + choix_ordi)
    
    # Afficher le résultat selon le cas
    if resultat == "egalite":
        label_text_result.config(text="Match nul !")
    
    elif resultat == "joueur":
        global score_joueur
        score_joueur += 1
        label_text_annonce.config(text=choix_joueur + " bat " + choix_ordi)
        label_text_result.config(text="Vous avez gagné ! 🎉")
    
    else:
        global score_ordinateur
        score_ordinateur += 1
        label_text_annonce.config(text=choix_ordi + " bat " + choix_joueur)
        label_text_result.config(text="L'ordinateur a gagné !")



def jouer_une_partie():
    label_text.config(text="")
    label_text2.config(text="")
    label_text_annonce.config(text="")
    label_text_result.config(text="")

    # 1. Demander le choix du joueur
    choix_joueur = demander_choix_joueur()
    if choix_joueur == "":
        return
    
    # 2. Faire choisir l'ordinateur
    choix_ordi = choix_ordinateur()
    
    # 3. Déterminer le gagnant
    resultat = determiner_gagnant(choix_joueur, choix_ordi)
    
    # 4. Afficher le résultat
    afficher_resultat(resultat, choix_joueur, choix_ordi)

    print("joueur : " + str(score_joueur) + " - " + str(score_ordinateur)) 
    
    print()
    rejouer = input("Voulez vous rejouer ? (oui/non) :  ")
    print()
    rejouer.lower()

    if rejouer == "oui" or rejouer == "ui" or rejouer == "1":
        jouer_une_partie()
    else : 
        print("////// - Score final - \\\\\\\\\\\\")
        print("joueur : " + str(score_joueur) + " - " + str(score_ordinateur)) 
        print()


root = tk.Tk()
root.title("Chifoumi - DZ Mafia")
root.geometry("600x400")

label_text = tk.Label(root, text="")
label_text.grid(row=10, column=0, padx=0, pady=0)

label_text2 = tk.Label(root, text="")
label_text2.grid(row=11, column=0, padx=0, pady=0)

label_text_annonce = tk.Label(root, text="")
label_text_annonce.grid(row=14, column=0, padx=0, pady=0)

label_text_result = tk.Label(root, text="")
label_text_result.grid(row=15, column=0, padx=0, pady=0)

label_version = tk.Label(root, text="Chifoumi " + version)
label_version.grid(row=50, column=0, padx=0, pady=20)

button = tk.Button(root, text="Lancer", command=jouer_une_partie)
button.grid(row=1, column=0, pady=20)


root.mainloop()

# Lancement du jeu
#jouer_une_partie()
