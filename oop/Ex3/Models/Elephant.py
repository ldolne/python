from .Animal import Animal 

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
    print("Elephant takes mud bath.")

  def sucking_up_water(self):
    print("Elephant sucks up water.")

  def observe_environment(self):
    super().observe_environment()
    print("Elephant observes its environment.")