import random
from models.Soigneur import Soigneur
from abc import ABC, abstractmethod
class Animal(ABC):
    #region Attributs
    _nom = str()
    _rassasier = 100
    _bonheur = 100
    _en_vie = True
    _soigneur = Soigneur()
    #endregion
    
    #region Prop's
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, new_nom):
        self._nom = new_nom

    @property
    def rassasier(self):
        return self._rassasier

    @rassasier.setter
    def rassasier(self, new_rassasier):
        self._rassasier = new_rassasier

    @property
    def bonheur(self):
        return self._bonheur

    @bonheur.setter
    def bonheur(self, new_bonheur):
        self._bonheur = new_bonheur

    @nom.setter
    def nom(self, new_nom):
        self._nom = new_nom

    @property
    def en_vie(self):
        return self._en_vie
    
    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, new_soigneur):
        self._soigneur = new_soigneur

    #endregion
    
    #region Méthodes
    def manger(self, nom_soigneur):
        if nom_soigneur == self.soigneur.nom:
            self._rassasier = 100
            return True
        else:
            print(f"Le soigneur : {nom_soigneur} n'est pas autorisé a nourir {self._nom} 🚫")
    
    def diminuer_rassasier(self):
        self.rassasier -= random.randint(10,30)
        if self._rassasier <= 0:
            self._en_vie = False
            self._rassasier = 0
            self._bonheur = 0
            print(f"{self._nom} est mort de faim ☠️")
    
    def diminuer_bonheur(self):
        self._bonheur -= random.randint(10,20)
        if self._bonheur <= 0:
            self._bonheur = 0
    
    @abstractmethod
    def observer_environnement(self):
        pass
    
    @abstractmethod
    def ramasser_objet(self):
        pass
    
    @abstractmethod
    def probabilite_deces(self):
        pass
    #endregion