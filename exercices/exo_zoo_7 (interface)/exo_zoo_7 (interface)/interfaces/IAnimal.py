from abc import ABC, abstractmethod

class IAnimal(ABC):
    @abstractmethod
    def manger(self):
        pass
    
    @abstractmethod
    def observer_environnement(self):
        pass
    
    @abstractmethod
    def faire_une_sieste(self):
        pass
    
    @abstractmethod
    def probabilite_deces(self):
        pass

    @abstractmethod
    def diminuer_rassasier(self):
        pass
    
    @abstractmethod
    def diminuer_bonheur(self):
        pass