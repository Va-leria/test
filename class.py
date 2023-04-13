# The class describes the object, but is independent of it.
# in other words, a class is an instance, description or definetion of an object.
# You can use the calss as a sample to create different objects.

# Example_1:
class Cat:
    animal = True # object attribute (it's static)
    def __init__(self, color, legs, name):
        if (self.animal):
            self.color = color # attribute (it's dynamic)
            self.legs = legs
            self.name = name

    def greeting(self):
        print(f'Hi! My name is {self.name}')

felix = Cat("ginger", 4, "Felix") # object of the class
rover = Cat("dog-colored", 4, "Rover") # object of the class

# The __init__ method is the most important method of the class.
# It's called when an instance (object) of a class is created; the class name is used as a function.
# All methods must have 'self' as their first parameter; although 'self' isn't directly passed, 
# Python adds the 'self' statement to the list itself. Within the method definition, the 'self' 
# statement refers to the instance of the class calling the method. 
# Class instance take attributes - fragments of data associated with them.
# In Example_1, Cat instances have colour and legs attributes. They can be obtained by specifying a point
# and attribute name after the instance.
# Thus, inside the __init__ method, you can use the initial value of instance attributes using self.attribute:
print(felix.color)
print(felix.animal)
rover.greeting()
print("1---------------------")

# METHODS
# You can also use other methods that extend the functionality of classes.
# Remember that the first parameter of all methods should be 'self'.
# Use the same syntax (dot) as for attributes.

# Example_2:
class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Wooof!")

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()
print("2--------------------")

# Example_3:
class Cat:
    species = "mammal"
    def __init__(self, name, age):
        self.name = name
        self.age = age

felix = Cat("Felix", 7)
rick = Cat("Rick", 1)
belka = Cat("Belka", 15)

def oldest_cat(*args):
    return max(args)

print(f"The oldest cat is {oldest_cat(felix.age, rick.age, belka.age)}")

cats = [felix, rick, belka]
print(cats[0].age)
print("3----------------------")

# Example_4:
class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sound):
        return f'{sound}'

class Sally(Cat):
    def sing(self, sound):
        return f'{sound}'

class Luna(Cat):
    def sing(self, sound):
        return f'{sound}'

simon = Simon("Simon", 3)
sally = Sally("Sally", 7)
luna = Luna("Luna", 1)

my_cats = [simon, sally, luna]

my_pets = Pets(my_cats)
my_pets.walk()
print(luna.sing("Meow"))
print("4---------------------")

# Example_5:
class Strng:
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

xx = Strng()
xx.get_string()
xx.print_string()

# HIDING DATA
# Conditonally, private methods and attributes are drawn uo with a single underscore at the beggining of the name.
# These are private methods that shouldn't interact with external part of the program. 
# But ofthen this rule is conditional; the external part of the program can access them.
# The only real feature of these methods is that "from module_name import *" won't import 
# variables that begin with a single underscore.

# Example_5:
