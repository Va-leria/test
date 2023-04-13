# With the help of inheritance, we can set the same functionality to different classes.

# Example_1:
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Wooof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
print("1------------------")

# A class that inherits attributes or methods of another class is called a SUBCLASS.
# The class from which attributes or methods are inherited is called a SUPERCLASS.
# !!! If the inherited class has the same attributes or methods as the heir class, the heir class overrides them:
# Example_2:
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Wooof!")

class Dogs(Wolf):
    def bark(self):
        print("Grrr...")

husky = Dogs("Max", "grey")
husky.bark()
print("2-----------------")

# Inheritance may also be indirect.
# Example_3:
class A:
    def method(self):
        print("A method")

class B(A):
    def another_method(self):
        print("B method")

class C(B):
    def third_method(self):
        print("C method")

c = C()
c.method()
c.another_method()
c.third_method()
print("3---------------")

# The super function is a useful inheritance function that points to the parent class.
# Example_4:
class D:
    def spam(self):
        print(1)

class E(D):
    def spam(self):
        print(2)
        super().spam() # calls the spam superclass method

E().spam()
print("4----------------")

# Example_5 with super():
class User(object):
    def __init__(self, email):
        self.email = email
        print("init complete")

    def sign_in(self):
        print("logged in")

class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email)
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f'{self.arrows} remaining')

wizard1 = Wizard("Merlin", 50, "merlin@gmail.com")
archer1 = Archer("Robin", 500, "robin@gmail.com")

print(wizard1.email)
print(archer1.email)
print("5------------------")

# Example_6 with multiply inheritance:
class Userr(object):
    def sign_in(self):
        print("logged in")

class Wizardd(Userr):
    def __init__(self, name, power,):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')

class Archerr(Userr):
    def __init__(self, name, arrows):
        self.arrows = arrows
        self.name = name

    def check_arrows(self):
        print(f'{self.arrows} remaining')

class Hybridd(Wizardd, Archerr):
    def __init__(self, name, power, arrows):
        Wizardd.__init__(self, name, power)
        Archerr.__init__(self, name, arrows)

wizard2 = Wizardd("Merlin", 50)
archer2 = Archerr("Robin", 500)
hybrid2 = Hybridd("bo", 23, 431)

wizard2.attack()
print(archer2.name)
hybrid2.check_arrows()
hybrid2.attack()
print("6------------------")