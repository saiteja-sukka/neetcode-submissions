class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger=self.hunger-1
        print("Fluffy has been fed.")
        print(f"Fluffy's hunger level: {self.hunger}")
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()
























""" Object Methods
Methods are functions that belong to a class or object. They define the behavior of the class or object.

Defining methods in a class
Let's update our SuperHero class to include two methods, use_power() and take_damage(amount):

class SuperHero:
    def __init__(self, name, power, health, speed):
        self.name = name
        self.power = power
        self.health = health
        self.speed = speed

    def use_power(self):
        print(f"{self.name} uses {self.power}!")

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} takes {amount} damage. Health is now {self.health}.")
We can create an object of the SuperHero class and call the methods on it:

iron_man = SuperHero("Iron Man", "super strength", 100, 90)

iron_man.use_power()     # Output: Iron Man uses super strength!
iron_man.take_damage(20) # Output: Iron Man takes 20 damage. Health is now 80.
Let's break down what's happening in this code:

The use_power() method:

Takes no parameters (except self, which we'll explain in a future lesson).
Prints a message saying the superhero is using their power.
The take_damage(amount) method:

Takes a parameter amount and subtracts it from the object's health.
Prints a message about the damage taken and the object's new health.
Methods are called on an object using dot notation, like iron_man.use_power(). If a method takes parameters, they are passed in the same way as function arguments e.g. iron_man.take_damage(20).

Challenge
Please see the starter code of the Pet class and complete the following in the feed method:

Decrease the pet's hunger by 1
Print the string 'Fluffy has been fed.'.
Print the current hunger level of my_pet, in this format: 'Fluffy's hunger level: X'
And then call the feed method three times on my_pet.

After completing the task your code should give the following expected output.

Expected Output
Fluffy has been fed.
Fluffy's hunger level: 4
Fluffy has been fed.
Fluffy's hunger level: 3
Fluffy has been fed.
Fluffy's hunger level: 2

Method vs Function
Methods are just functions that are defined inside a class. A function defined outside of a class is not a method. """