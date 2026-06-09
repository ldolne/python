from random import choice
import random
from models.Animal import Animal
from interfaces.IAnimal import IAnimal

class Elephant(Animal, IAnimal):
    #region Attributs
    _apparence = "🐘"
    #endregion
    
    #region Constructeurs
    def __init__(self ,nom ,soigneur, longueur_defense ,rassasier = 100, bonheur = 100, en_vie = True):
        super().__init__(nom ,soigneur ,rassasier ,bonheur ,en_vie)
        self._longueur_defense = longueur_defense
    #endregion

    #region Prop's
    @property
    def apparence(self):
        return self._apparence
    
    @property
    def longueur_defense(self):
        return self._longueur_defense
    #endregion
    
    #region Méthodes
    def prendre_bain_de_boue(self):
        if self._bonheur <= 95:
            self._bonheur += 3
            print(f"{self._nom} prend un bain de boue 💦🐘")
    
    def aspirer_eau(self):
        if self._rassasier <= 95:
            self._rassasier += 3
            print(f"{self._nom} aspire de l'eau avec sa trompe 💧🐘")
    
    def ramasser_objet(self):
        objets = ["brindille", "feuille", "pierre", "fruit", "bâton"]
        objet_ramasse = choice(objets)
        print(f"{self._nom} a ramassé un(e) {objet_ramasse} 🤲🐘")
    
    def observer_environnement(self):
        print(f"L'éléphant {self.nom} regarde autour de lui avec ses grands yeux 👀🐘")
    
    def faire_une_sieste(self):
        print(f"{self._nom} ferme les yeux et fait la sieste 🐘💤")
    
    def comportement_hasard(self):
        comportements = ["prendre_bain_de_boue","aspirer_eau","ramasser_objet","observer_environnement","faire_une_sieste"]
        comportement = choice(comportements)
        if comportement == "prendre_bain_de_boue":
            self.prendre_bain_de_boue()
        elif comportement == "aspirer_eau":
            self.aspirer_eau()
        elif comportement == "ramasser_objet":
            self.ramasser_objet()
        elif comportement == "observer_environnement":
            self.observer_environnement()
        elif comportement == "faire_une_sieste":
            self.faire_une_sieste()
    
    def probabilite_deces(self):
        prob_deces = random.random()  # Générez une probabilité de décès aléatoire entre 0 et 1
        if prob_deces < 0.05:  # Par exemple, une probabilité de décès de 5%
            self._en_vie = False
            print(f"{self._nom} est malheureusement décédé 😢")
    #endregion