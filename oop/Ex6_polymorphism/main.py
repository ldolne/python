from Models import Enclosure, Elephant, Giraffe, CareTaker, Tools

# MAIN
i = 0
while i < 3:
    caretaker1 = CareTaker("Luna", "2002-08-20")
    giraffe1 = Giraffe("Titi", caretaker1, 3.5)
    elephant1 = Elephant("Gipsi", caretaker1, 1.5)
    enclosure1 = Enclosure("Bel Enclos", 2, 120)

    enclosure1.add_animal(giraffe1)
    enclosure1.add_animal(elephant1)

    for animal in enclosure1.animals_in_enclosure:
        if isinstance(animal, Elephant) or isinstance(animal, Giraffe):
            animal.random_behavior()

    Tools.pause(2)
    Tools.clear_console()
    i += 1
print("End of program")