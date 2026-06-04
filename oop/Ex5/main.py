from Models import Elephant, Giraffe, CareTaker, Tools

# MAIN
i = 0
while i < 3:
    caretaker1 = CareTaker("Luna", "2002-08-20")
    giraffe1 = Giraffe("Titi", caretaker1, 3.5)
    elephant1 = Elephant("Gipsi", caretaker1, 1.5)

    print("Size of neck:", giraffe1.neck_size)
    giraffe1.eat_leaves()
    giraffe1.drink_water()
    giraffe1.observe_environment()
    giraffe1.pick_up_object()
    giraffe1.death_probability()
    print("Size of tusks:", elephant1.tusk_size)
    elephant1.take_mud_bath
    elephant1.sucking_up_water()
    elephant1.observe_environment()
    elephant1.pick_up_object()
    elephant1.death_probability()

    Tools.pause(2)
    Tools.clear_console()
    i += 1
print("End of program")