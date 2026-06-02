class Enclosure:
  __name = None
  __max_capacity = 0
  __size = 0 # m²
  __animals_in_enclosure = []

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    self.__name = value

  @property
  def max_capacity(self):
    return self.__max_capacity

  @max_capacity.setter
  def max_capacity(self, value):
    if not isinstance(value, int):
      raise TypeError("Max capacity must be a int")
    self.__max_capacity = value

  @property
  def size(self):
    return self.__size

  @property
  def animals_in_enclosure(self):
    return self.__animals_in_enclosure

  def __init__(self, name = "", max_capacity = 0, size = 0):
    self.__name = name
    self.__max_capacity = max_capacity
    self.__size = size
    self.__animals_in_enclosure = []

  def add_animal(self, animal):
    if(len(self.__animals_in_enclosure) >= self.__max_capacity):
      raise Exception("Enclosure is full! Can't add another animal!")
    self.__animals_in_enclosure.append(animal)
    pass

  def remove_animal(self, animal):
    if(len(self.__animals_in_enclosure) <= 0):
      raise Exception("Enclosure is full! Can't remove an animal!")
    self.__animals_in_enclosure.remove(animal)

  def show_animals_in_enclosure(self):
    for each in self.__animals_in_enclosure:
      print(each)