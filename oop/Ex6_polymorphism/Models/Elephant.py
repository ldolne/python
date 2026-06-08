from .Animal import Animal 
from random import choice, random

class Elephant(Animal):
  @property
  def tusk_size(self):
    return self.__tusk_size

  @tusk_size.setter
  def tusk_size(self, value):
    self.__tusk_size = value

  def __init__(self, name, care_taker, tusk_size):
    super().__init__(name, care_taker)
    self.__tusk_size = tusk_size

  def __str__(self):
    string = super().__str__()
    string += "Animal is an Elephant. "
    string += "Tusk size is %s" % (self.__tusk_size)
    return string

  def take_mud_bath(self):
    if self.satisfaction < 50:
      self.satisfaction += 5
    print("Elephant takes mud bath.")

  def sucking_up_water(self):
    if self.appetite < 95:
      self.appetite += 3
    print("Elephant sucks up water.")

  def observe_environment(self):
    print("Elephant observes its environment.")

  def random_behavior(self):
    method_choices = ["take_mud_bath", "sucking_up_water"]
    chosen_method = getattr(self, choice(method_choices))
    chosen_method()

  def pick_up_object(self):
    objects = ["ballon", "cacahuète", "branche", "banane"]
    picked_up_object = choice(objects)
    print(f"{self.name} the elephant picks up an object: {picked_up_object}")

  def death_probability(self):
    death_probability = random() # valeur aléatoire entre 0 et 1 (nombre à virgule)
    if death_probability < 0.9: # 10%
      self.alive = False
      print(f"{self.name} the elephant is dead.")