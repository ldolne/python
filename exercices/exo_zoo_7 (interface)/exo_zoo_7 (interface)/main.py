import datetime
import time

from models.Elephant import Elephant
from models.Girafe import Girafe
from models.Enclos import Enclos
from models.Soigneur import Soigneur
from models.Outils import Outils

if __name__ == "__main__":
    #region Encodage
    Outils.clear_console()
    print("🌲 Simulation de vie au sein d'un enclos 🌲")
    time.sleep(3)
    Outils.clear_console()
    
    # infos soigneur
    print("Veuillez saisir les informations demandées pour le soigneur : \n")
    soigneur = Soigneur()
    soigneur.nom = input("Nom :")
    soigneur.date_naissance = datetime.datetime.strptime(input("Entrez la date de naissance (format YYYY-MM-DD) : "), "%Y-%m-%d")
    Outils.clear_console()
    
    # infos enclos
    print("Veuillez à présent saisir les informations liées à l'enclos : \n")
    enclos = Enclos()
    enclos.nom = input("Nom enclos:")
    enclos.capacite_max = 20
    enclos.taille = 4000
    Outils.clear_console()
    
    #infos animaux
    nombre_animaux = int(input(f"De combien d'animaux l'enclos sera-t-il constitué ? (max = {enclos.capacite_max}) : "))
    Outils.clear_console()
    
    for i in range(nombre_animaux):
        type_animal = input("Quel type d'animal voulez-vous ajouter (E pour Elephant, G pour Girafe) : ").upper()
        animal = None
        if type_animal == 'E':
            animal = Elephant()
        elif type_animal == 'G':
            animal = Girafe()
        print(f"Encodage animal nr° {i+1}")
        animal.nom = input("Nom :")
        animal.soigneur = soigneur
        enclos.ajouter_animal(animal)
        Outils.pause(1)
        Outils.clear_console()
    
    nombre_jour = int(input("Nombre de jour(s) : "))
    Outils.clear_console()
    #endregion
    
    #region logique
    input("Appuyez sur Enter pour lancer la simulation 🎮")
    
    for i in range(nombre_jour):
        for animal in enclos.liste_animaux:
            if animal.rassasier <= 50:
                soigneur.nourrir(animal)
                Outils.pause(1)
            if animal.bonheur <= 70:
                soigneur.entretenir(animal)
                Outils.pause(1)
            if isinstance(animal, Elephant) or isinstance(animal, Girafe):
                animal.comportement_hasard()
                Outils.pause(1)
                animal.probabilite_deces()
                Outils.pause(1)
        
        input("Appuyez sur Enter pour continuer ⏭")
        Outils.clear_console()
        enclos.passer_un_jour()
        Outils.clear_console()
        print(f"Jours : {i+1}")
        print("---------")
        enclos.afficher_animaux()
        input("Appuyez sur Enter pour passer au jour suivant ⏭")
        Outils.clear_console()
    
    print("La simulation est arrivée à son terme 😁")
    Outils.pause(3)
    print()
    print()
    input("--- Appuyez sur Enter pour quitter ---")
    #endregion