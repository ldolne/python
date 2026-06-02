import datetime as dt

class CareTaker:
  _name = None
  _birthdate = None
  _experience = 0
  _number_of_animals_in_care = 0
  _animals_in_care = []

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @property
  def birthdate(self):
    return self._birthdate

  @property
  def experience(self):
    return self._experience

  @property
  def number_of_animals_in_care(self):
    return self._number_of_animals_in_care

  @property 
  def computed_age(self):
    if self._birthdate != None:
      birthdate = dt.date.fromisoformat(self._birthdate)
      age = int(dt.datetime.today().strftime("%Y")) - int(birthdate.strftime("%Y"))
      return age

  def __init__(self, name, birthdate):
    self._name = name
    self._birthdate = birthdate

  def __str__(self):
    return "Caretaker: name is %s, birthdate is %s, experience is %s, number_of_animals_in_care is %s" % (self._name, self._birthdate, self._experience, self._number_of_animals_in_care)

  def add_in_care(self, animal):
    self._animals_in_care.append(animal)
    self._number_of_animals_in_care += 1

  def feed(self, animal):
    animal.eat()
    self._experience += 5

  def take_care_of(self, animal):
    animal.been_taken_care_of()
    self._experience += 5

  def show_animals_in_care(self):
    for each in self._animals_in_care:
      print(each)