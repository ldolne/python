import random as rd

class Elephant:
  _name = None
  _appetite = 50
  _satisfaction = 50
  _alive = True
  _care_taker = None

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @property
  def appetite(self):
    return self._appetite

  @property
  def satisfaction(self):
    return self._satisfaction

  @property
  def alive(self):
    return self._alive

  @property
  def care_taker(self):
    return self._care_taker

  @care_taker.setter
  def care_taker(self, new_care_taker):
    self._care_taker = new_care_taker

  def __init__(self, name, care_taker):
    self._name = name
    self._care_taker = care_taker

  def __str__(self):
    return "Elephant: name is %s, appetite is %s, satisfaction is %s, alive is %s, caretaker is %s" % (self._name, self._appetite, self._satisfaction, self._alive, self._care_taker)

  def eat(self):
    if not(self._alive):
      raise Exception("The elephant has died of hunger!")
    self._appetite += rd.randint(10, 30)
    if self._appetite >= 100:
      self._appetite = 100
    elif self._appetite <= 100:
      self._appetite = 0

  def been_taken_care_of(self):
    if not(self._alive):
      raise Exception("The elephant is dead and can't receive love!")
    self._satisfaction += rd.randint(10, 20)
    if self._satisfaction >= 100:
      self._satisfaction = 100
    elif self._satisfaction <= 100:
      self._satisfaction = 0

  def grows_hungry(self):
    if not(self._alive):
      raise Exception("The elephant is dead and can't go hungry anymore!")
    self._appetite -= 10
    if(self._appetite <= 0):
      self._alive = False

  def grows_sad(self):
    if not(self._alive):
      raise Exception("The elephant is dead and can't reveice love!")
    self._satisfaction -= 10