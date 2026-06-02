from Models import Elephant, Giraffe, CareTaker

# MAIN
caretaker1 = CareTaker("Luna", "2002-08-20")
giraffe1 = Giraffe("Titi", caretaker1, 3.5)
elephant1 = Elephant("Gipsi", caretaker1, 1.5)

print("Size of neck:", giraffe1.neck_size)
giraffe1.eat_leaves()
giraffe1.drink_water()
giraffe1.observe_environment()

print("Size of tusks:", elephant1.tusk_size)
elephant1.take_mud_bath
elephant1.sucking_up_water()
elephant1.observe_environment()