from models.Animal import Animal
from random import choice

class Girafe(Animal):
    #region Attributs
    _apparence = "🦒"
    _longueur_cou = float()
    #endregion
    
    #region Prop's
    @property
    def apparence(self):
        return self._apparence
    
    @property
    def longueur_cou(self):
        return self._longueur_cou

    @longueur_cou.setter
    def longueur_cou(self, new_longueur_cou):
        self._longueur_cou = new_longueur_cou
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
    
    def observer_environnement(self):
        print(f"La girafe {self.nom} lève la tête pour observer les environs avec son long cou 👀🦒")
    
    def comportement_hasard(self):
        comportements = ["manger_feuilles", "boire_eau", "observer_environnement"]
        comportement = choice(comportements)
        if comportement == "manger_feuilles":
            self.manger_feuilles()
        elif comportement == "boire_eau":
            self.boire_eau()
        elif comportement == "observer_environnement":
            self.observer_environnement()
    #endregion
