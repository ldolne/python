import random
from models.Soigneur import Soigneur
class Elephant:
    #region Attributs
    nom = ""
    rassasier = 100
    bonheur = 100
    en_vie = True
    soigneur = Soigneur()
    #endregion
    
    #region Méthodes
    def manger(self, nom_soigneur):
        if nom_soigneur == self.soigneur.nom:
            self.rassasier = 100
            return True
        else:
            print(f"Le soigneur : {nom_soigneur} n'est pas autorisé a nourir {self.nom}")
    
    def diminuer_rassasier(self):
        self.rassasier -= random.randint(10,30)
        if self.rassasier <= 0:
            self.en_vie = False
            self.rassasier = 0
            self.bonheur = 0
            print(f"{self.nom} est mort de faim ☠️")
    
    def diminuer_bonheur(self):
        self.bonheur -= random.randint(10,20)
        if self.bonheur <= 0:
            self.bonheur = 0
    #endregion