import random
from abc import ABC, abstractmethod
class Animal(ABC):
    #region Constructeur
    def __init__(self,nom,soigneur,rassasier, bonheur, en_vie):
        self._nom = nom
        self._soigneur = soigneur
        self._rassasier = rassasier
        self._bonheur = bonheur
        self._en_vie = en_vie
    #endregion
    
    #region Prop's
    @property
    def nom(self):
        return self._nom

    @property
    def rassasier(self):
        return self._rassasier

    @property
    def bonheur(self):
        return self._bonheur

    @property
    def en_vie(self):
        return self._en_vie
    
    @property
    def soigneur(self):
        return self._soigneur
    #endregion
    
    #region Méthodes
    def manger(self, nom_soigneur):
        if nom_soigneur == self._soigneur.nom:
            self._rassasier = 100
            return True
        else:
            print(f"Le soigneur : {nom_soigneur} n'est pas autorisé a nourir {self._nom} 🚫")
    
    def entretiens(self, nom_soigneur):
        if nom_soigneur == self._soigneur.nom:
            self._bonheur = 100
            return True
        else:
            print(f"Le soigneur : {nom_soigneur} n'est pas autorisé a nourir {self._nom} 🚫")
    
    def diminuer_rassasier(self):
        self._rassasier -= random.randint(10,30)
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