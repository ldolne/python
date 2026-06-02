from datetime import date

class CareTaker:
  __name = None
  __birthdate = None
  __experience = 0
  __number_of_animals_in_care = 0
  __animals_in_care = []

  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, value):
    if not isinstance(value, str):
      raise TypeError("Name must be a string")
    self.__name = value

  @property
  def birthdate(self):
    return self.__birthdate

  @property
  def experience(self):
    return self.__experience

  @property
  def number_of_animals_in_care(self):
    return self.__number_of_animals_in_care

  @property 
  def computed_age(self):
    if not hasattr(self, "birthdate"):
      print("No birthdate defined")
      raise ValueError("No birthdate defined")
    try:
      # My Solution
      # birthdate = date.fromisoformat(self.__birthdate)
      # age = int(date.today().strftime("%Y")) - int(birthdate.strftime("%Y"))
      # return age
      birthdate = date.strptime(self.__birthdate, "%Y-%m-%d")
      today = date.today()
      birthday_has_passed = (today.month, today.day) < (birthdate.month, birthdate.day)
      age = today.year - birthdate.year - birthday_has_passed # bool transformed as 0 or 1
      return age
    except ValueError:
      return "Birthdate not valid: YYYY-MM-DD"

  def __init__(self, name = "", birthdate = "01/01/1970", experience = 0):
    self.__name = name
    self.__birthdate = birthdate
    self.__experience = experience

  def __str__(self):
    return "Caretaker: name is %s, birthdate is %s, experience is %s, number_of_animals_in_care is %s" % (self.__name, self.__birthdate, self.__experience, self.__number_of_animals_in_care)

  def add_in_care(self, animal):
    self.__animals_in_care.append(animal)
    self.__number_of_animals_in_care += 1

  def feed(self, animal):
    animal.eat()
    self.__experience += 5

  def take_care_of(self, animal):
    animal.been_taken_care_of()
    self.__experience += 5

  def show_animals_in_care(self):
    for each in self.__animals_in_care:
      print(each)