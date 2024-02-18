# define Planet class
class Planet:

    # initialize properties
    def __init__(self, name, distance, mass, diameter,
                 density, gravity, temperature, daylength,
                 orbitalperiod, mf, moons):
        self.name = name
        self.distance = distance
        self.mass = mass
        self.diameter = diameter
        self.density = density
        self.gravity = gravity
        self.temperature = temperature
        self.daylength = daylength
        self.orbitalperiod = orbitalperiod
        self.mf = mf
        self.moons = moons
        self.options = ["distance", "mass", "diameter", "gravity",
                        "temperature", "daylength", "moons"]

    # print_stats() method
    def print_stats(self):
      print("*" * 30)
      print(self.name)
      print("Distance from sun: " + str(self.distance) + " million km")
      print("Mass: " + str(self.mass) + " 10^24 kg")
      print("Diameter: " + str(self.diameter) + " km")
      print("Density: " + str(self.density) + " kg/m^3")
      print("Gravity: " + str(self.gravity) + " m/s^2")
      print("Mean temperature: " + str(self.temperature) + " C")
      print("Length of day: " + str(self.daylength) + " hours")
      print("Orbital period: " + str(self.orbitalperiod) + " days")
      print("Magnetic field: " + str(self.mf))
      print("Number of moons: " + str(self.moons))
      print("*" * 30)
      print("")

    # get() method returns value of the property for this specific object.
    # property_name = string
    def get_value(self, property_name):
        if property_name in self.options:
            value = getattr(self, property_name)
            # print(self.name + " " + property_name + ": " + str(value))
            return value

planets = []
def setUpPlanetCards():
  # create instances of Planet class (objects)
  mercury = Planet("Mercury", 57.9, 0.33, 4879, 5427,
                   3.7, 167, 4222.6, 88, True, 0)
  venus = Planet("Venus", 108.2, 4.87, 12104, 5243,
                 8.9, 464, 2802.0, 224.7, False, 0)
  earth = Planet("Earth", 149.6, 5.97, 12756, 5514,
                 9.8, 15, 24, 365.2, True, 1)
  mars = Planet("Mars", 227.9, 0.642, 6792, 3933,
                3.7, -65, 24.7, 687, False, 2)
  jupiter = Planet("Jupiter", 778.6, 1898, 142984, 1326,
                   23.1, -110, 9.9, 4331, True, 79)
  saturn = Planet("Saturn", 1433.5, 568, 120536, 687,
                  9, -140, 10.7, 10747, False, 82)
  uranus = Planet("Uranus", 2872.5, 86.8, 51118, 1271,
                  8.7, -195, 17.2, 30589, True, 27)
  neptune = Planet("Neptune", 4495.1, 102, 49258, 1638,
                   11, -200, 16.1, 59800, True, 14)
                
  # create list of Planet objects
  planetList = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
  planets.extend(planetList)
  
# returns list of Planet objects
def get_planets_list():
    return planets
