from .Animal import Animal 
from random import choice, random

class Giraffe(Animal):
  @property
  def neck_size(self):
    return self.__neck_size

  @neck_size.setter
  def neck_size(self, value):
    self.__neck_size = value

  def __init__(self, name, care_taker, neck_size):
    super().__init__(name, care_taker)
    self.__neck_size = neck_size

  def __str__(self):
    string = super().__str__()
    string += "Animal is a Giraffe. "
    string += "Neck size is %s" % (self.__neck_size)
    return string

  def eat_leaves(self):
    if self.appetite < 95:
      self.appetite += 5
      print("Giraffe eats leaves with long neck.")

  def drink_water(self):
    if self.appetite < 95:
      self.appetite += 3
      print("Giraffe drinks water.")

  def observe_environment(self):
    print("Giraffe observes its environment.")

  def random_behavior(self):
    method_choices = ["eat_leaves", "drink_water"]
    chosen_method = getattr(self, choice(method_choices))
    chosen_method()

  def pick_up_object(self):
    objects = ["feuille", "pomme de pin", "brindille", "banane"]
    picked_up_object = choice(objects)
    print(f"{self.name} the giraffe picks up an object: {picked_up_object}")

  def death_probability(self):
    death_probability = random() # valeur aléatoire entre 0 et 1 (nombre à virgule)
    if death_probability < 0.9: # 10%
      self.alive = False
      print(f"{self.name} the giraffe is dead.")