from .Animal import Animal 

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
    print("Giraffe eats leaves.")

  def drink_water(self):
    print("Giraffe drinks water.")

  def observe_environment(self):
    super().observe_environment()
    print("Giraffe observes its environment.")