from Models import Elephant, CareTaker, Enclosure

# MAIN

# Setup
enclosure1 = Enclosure("Pretty gardens", 3, 500)
enclosure2 = Enclosure("Lovely gardens", 5, 250)
caretaker1 = CareTaker("Johnny", "2002-08-20")
caretaker2 = CareTaker("Luna", "1992-08-20")
print("Age of caretaker:", caretaker1.computed_age)
print("Age of caretaker:", caretaker2.computed_age)

print("Add elephants:")
elephant1 = Elephant("Micha", caretaker1)
caretaker1.add_in_care(elephant1)
enclosure1.add_animal(elephant1)
elephant2 = Elephant("Ingrid", caretaker1)
caretaker1.add_in_care(elephant2)
enclosure1.add_animal(elephant2)
elephant3 = Elephant("Georg", caretaker2)
caretaker2.add_in_care(elephant3)
enclosure2.add_animal(elephant3)
print("Show animals of caretaker:", caretaker1.name)
caretaker1.show_animals_in_care()
print("Show animals of caretaker:", caretaker2.name)
caretaker2.show_animals_in_care()
print("Show animals in enclosure:", enclosure1.name)
enclosure1.show_animals_in_enclosure()
print("Show animals in enclosure:", enclosure2.name)
enclosure2.show_animals_in_enclosure()

try:
  # Day at the Zoo
  elephant1.grows_hungry()
  elephant1.grows_sad()
  print(elephant1)
  caretaker1.feed(elephant1)
  caretaker1.feed(elephant1)
  caretaker1.take_care_of(elephant1)
  caretaker1.take_care_of(elephant1)
  print(elephant1)
  elephant2.grows_hungry()
  elephant2.grows_hungry()
  elephant2.grows_hungry()
  elephant2.grows_hungry()
  elephant2.grows_hungry()
  print(elephant2)
  caretaker1.feed(elephant2)
  caretaker1.take_care_of(elephant2)
except Exception as ex:
  print("Error happened:", ex)