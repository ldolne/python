import datetime
import os
from random import choice
import time

from models.Elephant import Elephant
from models.Girafe import Girafe
from models.Enclos import Enclos
from models.Soigneur import Soigneur

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear') 

if __name__ == "__main__":
    #region Encodage
    clear_console()
    print("🌲 Simulation de vie au sein d'un enclos 🌲")
    time.sleep(3)
    clear_console()
    
    # infos soigneur
    print("Veuillez saisir les informations demandées pour le soigneur : \n")
    soigneur = Soigneur()
    soigneur.nom = input("Nom :")
    soigneur.date_naissance = datetime.datetime.strptime(input("Entrez la date de naissance (format YYYY-MM-DD) : "), "%Y-%m-%d")
    clear_console()
    
    # infos enclos
    print("Veuillez à présent saisir les informations liées à l'enclos : \n")
    enclos = Enclos()
    enclos.nom = input("Nom enclos:")
    enclos.capacite_max = 20
    enclos.taille = 4000
    clear_console()
    
    #infos animaux
    nombre_animaux = int(input(f"De combien d'animaux l'enclos sera-t-il constitué ? (max = {enclos.capacite_max}) : "))
    clear_console()
    
    for i in range(nombre_animaux):
        type_animal = input("Quel type d'animal voulez-vous ajouter (E pour Elephant, G pour Girafe) : ").upper()
        animal = None
        print(f"Encodage animal nr° {i+1}")
        if type_animal == 'E':
            animal = Elephant()
            animal.nom = input("Nom :")
            animal.longueur_defense = input("insérer la longueur des défenses (cm) : ")
        elif type_animal == 'G':
            animal = Girafe()
            animal.nom = input("Nom :")
            animal.longueur_cou = input("insérer la longueur du cou (cm) : ")
        animal.soigneur = soigneur
        enclos.ajouter_animal(animal)
        time.sleep(1)
        clear_console()
    
    nombre_jour = int(input("Nombre de jour(s) : "))
    clear_console()
    #endregion
    
    #region logique
    input("Appuyez sur Enter pour lancer la simulation 🎮")
    
    comportements_elephant = ["prendre_bain_de_boue", "aspirer_eau", "observer_environnement"]
    comportements_girafe = ["manger_feuilles", "boire_eau", "observer_environnement"]
    
    for i in range(nombre_jour):
        for animal in enclos.liste_animaux:
            if animal.rassasier <= 50:
                soigneur.nourrir(animal)
                time.sleep(2)
            if animal.bonheur <= 70:
                soigneur.entretenir(animal)
                time.sleep(2)
            if isinstance(animal, Elephant):
                comportement = choice(comportements_elephant)
            elif isinstance(animal, Girafe):
                comportement = choice(comportements_girafe)
            # Exécutez le comportement choisi
            getattr(animal, comportement)()
            time.sleep(2)
        
        clear_console()
        enclos.passer_un_jour()
        clear_console()
        print(f"Jours : {i+1}")
        print("---------")
        enclos.afficher_animaux()
        input("Appuyez sur Enter pour passer au jour suivant ⏭")
        clear_console()
    
    print("La simulation est arrivée à son terme 😁")
    time.sleep(3)
    print()
    print()
    input("--- Appuyez sur Enter pour quitter ---")
    #endregion