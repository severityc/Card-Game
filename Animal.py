class Animal:
    def __init__(self, name, size, weight, speed, lifespan, population):
        self.name = name
        self.size = size
        self.weight = weight
        self.speed = speed
        self.lifespan = lifespan
        self.population = population

        self.options = ["size", "weight", "speed", "lifespan", "population"]

    def print_stats(self):
        print("*" * 20)
        print(self.name)
        print("Size: " + str(self.size) + " feet")
        print("Weight: " + str(self.weight) + " pounds")
        print("Speed: " + str(self.speed) + " mph")
        print("Lifespan: " + str(self.lifespan) + " years")
        print("Total population: " + str(self.population))
        print("*" * 20)
        print("")

    def get_value(self, property_name):
        while property_name not in self.options:
            property_name = input("Not valid, enter proper attribute: ")

        value = getattr(self, property_name)
        return value

animals = []

def setUpAnimalCards():
    lion = Animal("lion", 7, 400, 32, 12, 21500)
    cheetah = Animal("cheetah", 5, 130, 70, 14, 10000)
    whale = Animal("whale", 30, 15000, 35, 90, 50000)

    animalsList = [lion, cheetah, whale]

    # extends combines two lists
    animals.extend(animalsList)

def get_animals_list():
    return animals
