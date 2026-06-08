from Models import Elephant, Giraffe, CareTaker, Tools

# MAIN
i = 0
while i < 3:
    caretaker1 = CareTaker("Luna", "2002-08-20")
    giraffe1 = Giraffe("Titi", caretaker1, 3.5)
    elephant1 = Elephant("Gipsi", caretaker1, 1.5)

    giraffe1.random_behavior()
    elephant1.random_behavior()

    Tools.pause(2)
    Tools.clear_console()
    i += 1
print("End of program")