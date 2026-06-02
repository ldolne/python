class Enclosure:
  _name = None
  _max_capacity = 0
  _size = 0 # m²
  _animals_in_enclosure = []

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @property
  def max_capacity(self):
    return self._max_capacity

  @max_capacity.setter
  def max_capacity(self, new_max_capacity):
    self._max_capacity = new_max_capacity

  @property
  def size(self):
    return self._size

  @property
  def animals_in_enclosure(self):
    return self._animals_in_enclosure

  def __init__(self, name, max_capacity, size):
    self._name = name
    self._max_capacity = max_capacity
    self._size = size

  def add_animal(self, animal):
    if(len(self._animals_in_enclosure) >= self._max_capacity):
      raise Exception("Enclosure is full! Can't add another animal!")
    self._animals_in_enclosure.append(animal)
    pass

  def remove_animal(self, animal):
    if(len(self._animals_in_enclosure) <= 0):
      raise Exception("Enclosure is full! Can't remove an animal!")
    self._animals_in_enclosure.remove(animal)

  def show_animals_in_enclosure(self):
    for each in self._animals_in_enclosure:
      print(each)