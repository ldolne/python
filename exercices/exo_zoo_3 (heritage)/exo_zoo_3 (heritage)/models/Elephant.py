from models.Animal import Animal

class Elephant(Animal):
    #region Attributs
    _apparence = "🐘"
    _longueur_defense = float()
    #endregion

    #region Prop's
    @property
    def apparence(self):
        return self._apparence
    
    @property
    def longueur_defense(self):
        return self._longueur_defense

    @longueur_defense.setter
    def longueur_defense(self, new_longueur_defense):
        self._longueur_defense = new_longueur_defense
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
    
    def observer_environnement(self):
        print(f"L'éléphant {self.nom} regarde autour de lui avec ses grands yeux 👀🐘")
    #endregion