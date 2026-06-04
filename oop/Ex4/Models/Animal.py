import random as rd
from abc import ABC, abstractmethod

class Animal(ABC):
  @property
  def name(self):
    return self.__name

  @name.setter
  def name(self, new_name):
    self.__name = new_name

  @property
  def appetite(self):
    return self.__appetite
  
  @appetite.setter
  def appetite(self, value):
    self.__appetite = value

  @property
  def satisfaction(self):
    return self.__satisfaction

  @property
  def alive(self):
    return self.__alive
  
  @alive.setter
  def alive(self, value):
    self.__alive = value

  @property
  def care_taker(self):
    return self.__care_taker

  @care_taker.setter
  def care_taker(self, value):
    self.__care_taker = value

  def __init__(self, name=None, care_taker=None, appetite=50, satisfaction=50, alive=True):
    self.__name = name
    self.__appetite = appetite
    self.__satisfaction = satisfaction
    self.__alive = alive
    self.__care_taker = care_taker

  def __str__(self):
    return "Animal: name is %s, appetite is %s, satisfaction is %s, alive is %s, caretaker is %s" % (self.__name, self.__appetite, self.__satisfaction, self.__alive, self.__care_taker)
  
  def eat(self):
    if not(self.__alive):
      raise Exception("The elephant has died of hunger!")
    self.__appetite += rd.randint(10, 30)
    if self.__appetite >= 100:
      self.__appetite = 100
    elif self.__appetite <= 100:
      self.__appetite = 0

  def been_taken_care_of(self):
    if not(self.__alive):
      raise Exception("The elephant is dead and can't receive love!")
    self.__satisfaction += rd.randint(10, 20)
    if self.__satisfaction >= 100:
      self.__satisfaction = 100
    elif self.__satisfaction <= 100:
      self.__satisfaction = 0

  def grows_hungry(self):
    if not(self.__alive):
      raise Exception("The elephant is dead and can't go hungry anymore!")
    self.__appetite -= 10
    print("The animal grows hungry.")
    if(self.__appetite <= 0):
      self.__alive = False

  def grows_sad(self):
    if not(self.__alive):
      raise Exception("The elephant is dead and can't receive love!")
    self.__satisfaction -= 10
  
  @abstractmethod
  def observe_environment(self):
    pass

  @abstractmethod
  def pick_up_object(self):
    pass

  @abstractmethod
  def death_probability(self):
    pass