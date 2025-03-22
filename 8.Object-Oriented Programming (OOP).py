# ------------------ Classes and Objects ------------------
# Defining a class
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says woof!")

# Creating objects (instances of the class)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5
dog1.bark()       # Output: Buddy says woof!
dog2.bark()       # Output: Max says woof!

# ------------------ Inheritance ------------------
# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Derived class (inherits from Animal)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says meow!")

# Creating objects
animal = Animal("Generic Animal")
cat = Cat("Whiskers")

# Calling methods
animal.speak()  # Output: Generic Animal makes a sound.
cat.speak()     # Output: Whiskers says meow!

# ------------------ Encapsulation ------------------
# Encapsulation with private attributes
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")

    # Public method to get balance
    def get_balance(self):
        return self.__balance

# Creating an object
account = BankAccount("Alice", 1000)

# Accessing public methods
account.deposit(500)  # Output: Deposited 500. New balance: 1500
account.withdraw(200)  # Output: Withdrew 200. New balance: 1300
print("Current balance:", account.get_balance())  # Output: Current balance: 1300

# Trying to access private attribute directly (will raise an error)
# print(account.__balance)  # AttributeError

# ------------------ Polymorphism ------------------
# Polymorphism with inheritance
class Bird:
    def fly(self):
        print("This bird can fly.")

class Penguin(Bird):
    def fly(self):
        print("Penguins cannot fly.")

# Function demonstrating polymorphism
def bird_fly(bird):
    bird.fly()

# Creating objects
bird = Bird()
penguin = Penguin()

# Calling the function
bird_fly(bird)     # Output: This bird can fly.
bird_fly(penguin)  # Output: Penguins cannot fly.