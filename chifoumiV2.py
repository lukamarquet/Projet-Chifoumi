import random
import tkinter as tk
import winsound

font_taille = 10
font_taille_grand = 14

nbr_parties = 0
score_joueur = 0
score_ordinateur = 0

PIERRE = "pierre"
FEUILLE = "feuille"
CISEAUX = "ciseaux"

def jouer_son(chemin):
    winsound.PlaySound(chemin, winsound.SND_FILENAME | winsound.SND_ASYNC)

def demander_choix_joueur(): 
    choix_valides = [PIERRE, FEUILLE, CISEAUX]

    label_text.config(text="Choisissez une arme :", font=("Arial", font_taille_grand))

    variable = tk.StringVar(value=choix_valides[0])

    choix_menu = tk.OptionMenu(root, variable, *choix_valides)
    choix_menu.place(relx=0.5, rely=0.45, anchor="center")

    root.wait_variable(variable)

    choix = variable.get()

    choix_menu.destroy()
    label_text.config(text="", font=("Arial", font_taille, "bold"))

    return choix

def choix_ordinateur():
    return random.choice([PIERRE, FEUILLE, CISEAUX])

def determiner_gagnant(choix_joueur, choix_ordi):
    if choix_joueur == choix_ordi:
        return "egalite"

    if choix_joueur == PIERRE and choix_ordi == CISEAUX or choix_ordi == PIERRE and choix_joueur == CISEAUX:
        return "joueur" if choix_joueur == PIERRE else "ordinateur"
    
    if choix_joueur == FEUILLE and choix_ordi == PIERRE or choix_ordi == FEUILLE and choix_joueur == PIERRE:
        return "joueur" if choix_joueur == FEUILLE else "ordinateur"
    
    if choix_joueur == CISEAUX and choix_ordi == FEUILLE or choix_ordi == CISEAUX and choix_joueur == FEUILLE:
        return "joueur" if choix_joueur == CISEAUX else "ordinateur"

def afficher_resultat(resultat, choix_joueur, choix_ordi):
    label_text.config(text="Vous avez choisi : " + choix_joueur)
    label_text2.config(text="L'ordinateur a choisi : " + choix_ordi)
    
    global nbr_parties
    nbr_parties += 1

    if resultat == "egalite":
        label_text_result.config(text="Match nul !", fg="orange", font=("Arial", font_taille_grand, "bold"))
    
    elif resultat == "joueur":
        global score_joueur
        score_joueur += 1
        label_text_annonce.config(text=choix_joueur + " bat " + choix_ordi)
        label_text_result.config(text="Vous avez gagné ! 🎉", fg="green", font=("Arial", font_taille_grand, "bold"))
    
    else:
        global score_ordinateur
        score_ordinateur += 1
        label_text_annonce.config(text=choix_ordi + " bat " + choix_joueur)
        label_text_result.config(text="L'ordinateur a gagné !", fg="red", font=("Arial", font_taille_grand, "bold"))

def jouer_une_partie():
    if nbr_parties == 0:
        jouer_son("Ressources/Ressources/ambiance/theme.wav")

    button.config(state=tk.DISABLED)
    label_text.config(text="", fg="black", font=("Arial", font_taille, "bold"))
    label_text2.config(text="")
    label_text_annonce.config(text="")
    label_text_result.config(text="")
    label_text_result2.config(text="")

    choix_joueur = demander_choix_joueur()
    if choix_joueur == "":
        return
    
    choix_ordi = choix_ordinateur()
    resultat = determiner_gagnant(choix_joueur, choix_ordi)
    afficher_resultat(resultat, choix_joueur, choix_ordi)
    
    if score_joueur > score_ordinateur:
        label_text_score.config(fg="green")
    elif score_joueur < score_ordinateur:
        label_text_score.config(fg="red")
    else:
        label_text_score.config(fg="orange")
    label_text_score.config(text=str(score_joueur) + " - " + str(score_ordinateur))

    choix_valides = ["oui", "non"]
    label_text_colum2.config(text="Voulez vous rejouer ? (oui/non) :")

    variable = tk.StringVar(value=choix_valides[0])

    choix_menu_colum2 = tk.OptionMenu(root, variable, *choix_valides)
    choix_menu_colum2.place(relx=0.5, rely=0.65, anchor="center")

    root.wait_variable(variable)

    rejouer = variable.get()

    choix_menu_colum2.destroy()
    label_text_colum2.config(text="")
    label_text.config(text="")

    if rejouer == "oui":
        jouer_une_partie()
    else:
        label_text2.config(text="")
        label_text_score.config(text="0 - 0")
        label_text_annonce.config(text="")

        if score_joueur > score_ordinateur:
            color = "green"
            label_text_result.config(text="Vous avez gagné la partie finale ! 🎉", fg="green", font=("Arial", font_taille_grand, "bold"))
        elif score_joueur < score_ordinateur:
            color = "red"
            label_text_result.config(text="L'ordinateur a gagné la partie finale !", fg="red", font=("Arial", font_taille_grand, "bold"))
        else:
            color = "orange"
            label_text_result.config(text="Match nul pour la partie finale !", fg="orange", font=("Arial", font_taille_grand, "bold"))
        
        label_text.config(text="////// - Score final - \\\\\\\\\\\\", fg=color, font=("Arial", font_taille_grand, "bold"))
        label_text_result2.config(text=str(score_joueur) + " - " + str(score_ordinateur), fg=color, font=("Arial", font_taille_grand, "bold"))

        button.config(state=tk.NORMAL, text="Rejouer")
        score_zero()

def score_zero():
    global score_joueur, score_ordinateur, nbr_parties
    nbr_parties = 0
    score_joueur = 0
    score_ordinateur = 0

root = tk.Tk()
root.title("Chifoumi - DZ Mafia")
root.geometry("600x400")

# --- PLACEMENTS ELEMENTS ---

# Score en haut à droite
label_text_score = tk.Label(root, text="0 - 0", font=("Arial", font_taille_grand, "bold"))
label_text_score.place(relx=1, rely=0, x=-10, y=10, anchor="ne")

# Bouton en haut à gauche
button = tk.Button(root, text="Lancer", command=jouer_une_partie, font=("Arial", font_taille-2, "bold"))
button.place(relx=0, rely=0, x=10, y=10, anchor="nw")

# Éléments centraux
label_text = tk.Label(root, text="Lancer d'abord la partie afin de jouer.", font=("Arial", font_taille_grand, "bold"))
label_text.place(relx=0.5, rely=0.30, anchor="center")

label_text2 = tk.Label(root, text="", font=("Arial", font_taille, "bold"))
label_text2.place(relx=0.5, rely=0.35, anchor="center")

label_text_annonce = tk.Label(root, text="", font=("Arial", font_taille, "bold"))
label_text_annonce.place(relx=0.5, rely=0.40, anchor="center")

label_text_result = tk.Label(root, text="", font=("Arial", font_taille, "bold"))
label_text_result.place(relx=0.5, rely=0.50, anchor="center")

label_text_result2 = tk.Label(root, text="", font=("Arial", font_taille, "bold"))
label_text_result2.place(relx=0.5, rely=0.55, anchor="center")

label_text_colum2 = tk.Label(root, text="", font=("Arial", font_taille, "bold"))
label_text_colum2.place(relx=0.5, rely=0.60, anchor="center")

jouer_son("Ressources/Ressources/ambiance/cool-sound.wav")
root.mainloop()

# Lancement du jeu
#jouer_une_partie()
