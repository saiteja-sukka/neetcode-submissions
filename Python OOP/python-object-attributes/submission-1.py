class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)
print(f"Initial Attributes: Whiskers ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
whiskers.hunger=3
whiskers.energy=10
print(f"Modified Attributes: Whiskers ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
# TODO: Print Whiskers' initial attributes

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

# TODO: Print Whiskers' modified attributes

















""" Object Attributes
Attributes are the properties that define or belong to an object. In our superhero example, we have the following attributes for a superhero: name, power, health, and speed.

Accessing Attributes
To access an object's attributes, we use dot notation: object_name.attribute_name. Let's create a superhero and access its attributes:

class SuperHero:
    def __init__(self, name: str, power: str, health: int, speed: int):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)

print(iron_man.name)    # Iron Man
print(iron_man.power)   # repulsor beams
Modifying Attributes
We can also modify an attribute's value using the same dot notation:

iron_man.health = 90
iron_man.power = "advanced repulsor technology"

print(iron_man.health)  # 90
print(iron_man.power)   # advanced repulsor technology
Attribute Types
While Python won't give us any errors when changing the data type of an attribute, we should avoid doing so to avoid unexpected behavior.

iron_man.name = 42       # Allowed but bad practice
iron_man.health = "full" # Allowed but bad practice
Challenge
You are given a Pet class and an object from that class whiskers.

Print the attributes of whiskers with the formatting below.
Decrease the hunger attribute by 3, and increase the energy attribute by 2.
Print the attributes of whiskers again with the formatting below.
Expected Output:

Initial Attributes: Whiskers (cat) - Hunger: 6, Energy: 8
Modified Attributes: Whiskers (cat) - Hunger: 3, Energy: 10

Hints
Access: pet_object.attribute

Modify: pet_object.attribute = new_value or pet_object.attribute += value

Print: f"Attributes: {pet_object.name} ({pet_object.species}) - Hunger: {pet_object.hunger}, Energy: {pet_object.energy}"
 """
