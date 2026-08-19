class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name=name
        self.power=power
        self.health=health
        # TODO: Initialize the superhero's attributes here
        pass


# TODO: Create Superhero instances
hero1=SuperHero("Batman","Intelligence",100)
hero2=SuperHero("Superman","Strength",150)

# TODO: Print out the attributes of each superhero
print(hero1.name)
print(hero1.power)
print(hero1.health)
print(hero2.name)
print(hero2.power)
print(hero2.health)
















""" Implement Superhero Class
In this challenge, you'll complete the implementation of a SuperHero class and create superhero instances. Your tasks are as follows:

1. Complete the SuperHero class:

Add attributes name, power, and health to the __init__ method.
2. Create superhero instances:

Instantiate a superhero with the name "Batman", power "Intelligence", and health 100.
Instantiate a superhero with the name "Superman", power "Strength", and health 150.
3. Display superhero information:

Print out each superhero's name, power, and health on a separate line.
Note: You can remove the pass in the __init__ method after adding your code.

Expected Output
Batman
Intelligence
100
Superman
Strength
150

Hints
In the __init__ method, remember to use self to assign the attributes. For example: self.attribute_name = value

To create a hero: hero1 = SuperHero("Hero Name", "Superpower", 100)

To print hero info: print(f"{hero1.name} has the power of {hero1.power} and {hero1.health} health.")

 """