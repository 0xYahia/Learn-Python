from screwDriver import Screwdriver

slottedScrewdriver = Screwdriver("black", 15, "slotted", False, True)
slottedScrewdriver.rotates()
slottedScrewdriver.testsElectricity()

trinWingScrewdriver = Screwdriver("Yellow", 15, "Tri_wing", False, True)
trinWingScrewdriver.rotates()
trinWingScrewdriver.testsElectricity()

philipsScrewdriver = Screwdriver("Red", 36, "Phlips", True, False)
philipsScrewdriver.rotates()
philipsScrewdriver.testsElectricity()
