# Permet de centraliser les imports des classes du dossier Models
from .Animal import Animal
from .Elephant import Elephant
from .Giraffe import Giraffe
from .CareTaker import CareTaker
from .Enclosure import Enclosure
from .Tools import Tools

__all__ = ["Elephant", "CareTaker", "Enclosure", "Giraffe", "Animal", "Tools"]