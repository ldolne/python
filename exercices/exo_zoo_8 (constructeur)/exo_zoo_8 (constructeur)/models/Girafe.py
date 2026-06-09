import random
from models.Animal import Animal
from random import choice
from interfaces.IAnimal import IAnimal


class Girafe(Animal, IAnimal):
    #region Attributs
    _apparence = "🦒"
    #endregion
    
    #region Constructeurs
    def __init__(self ,nom ,soigneur, longueur_cou ,rassasier = 100, bonheur = 100, en_vie = True):
        super().__init__(nom ,soigneur ,rassasier ,bonheur ,en_vie)
        self._longueur_cou = longueur_cou
    #endregion
    
    #region Prop's
    @property
    def apparence(self):
        return self._apparence
    
    @property
    def longueur_cou(self):
        return self._longueur_cou
    #endregion
    
    #region Méthodes
    def manger_feuilles(self):
        if self.rassasier < 95:
            self.rassasier += 3
            print(f"{self._nom} mange des feuilles avec son long cou 🌿🦒")

    def boire_eau(self):
        if self.rassasier < 95:
            self.rassasier += 3
            print(f"{self._nom} boit de l'eau avec sa langue 👅🦒")

    def ramasser_objet(self):
        objets = ["feuille", "brindille", "fleur", "pomme de pin"]
        objet_ramasse = choice(objets)
        print(f"{self._nom} a ramassé une {objet_ramasse} avec son long cou 🤲🦒")
    
    def observer_environnement(self):
        print(f"La girafe {self.nom} lève la tête pour observer les environs avec son long cou 👀🦒")
    
    def faire_une_sieste(self):
        print(f"{self._nom} se couche et fait la sieste avec son long cou 🦒💤")
    
    def comportement_hasard(self):
        comportements = ["manger_feuilles", "boire_eau", "ramasser_objet", "observer_environnement","faire_une_sieste"]
        comportement = choice(comportements)
        if comportement == "manger_feuilles":
            self.manger_feuilles()
        elif comportement == "boire_eau":
            self.boire_eau()
        elif comportement == "ramasser_objet":
            self.ramasser_objet()
        elif comportement == "observer_environnement":
            self.observer_environnement()
        elif comportement == "faire_une_sieste":
            self.faire_une_sieste()
    
    def probabilite_deces(self):
        prob_deces = random.random()  # Générez une probabilité de décès aléatoire entre 0 et 1
        if prob_deces < 0.03:  # Par exemple, une probabilité de décès de 3%
            self._en_vie = False
            print(f"{self._nom} est malheureusement décédée 😢")
    #endregion
