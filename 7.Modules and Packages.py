# ------------------ Importing Modules ------------------
# Importing a module
import math

# Using functions from the math module
print("Square root of 16:", math.sqrt(16))  # Output: 4.0
print("Value of pi:", math.pi)             # Output: 3.141592653589793

# Importing specific functions
from random import randint

# Using the randint function
random_number = randint(1, 10)
print("Random number between 1 and 10:", random_number)

# ------------------ Standard Library Modules ------------------
# Using the datetime module
import datetime

# Get current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Formatting dates
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)

# Using the os module
import os

# Get current working directory
print("Current working directory:", os.getcwd())

# List files in a directory
print("Files in current directory:", os.listdir())

# ------------------ Creating Your Own Modules ------------------
# Create a file named my_module.py
# my_module.py content:
"""
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b
"""

# Importing your own module
import my_module

# Using functions from your module
my_module.greet("Alice")  # Output: Hello, Alice!
result = my_module.add(5, 3)
print("Result of addition:", result)  # Output: 8

# ------------------ Creating Packages ------------------
# Create a package named my_package
# Directory structure:
"""
my_package/
    __init__.py
    module1.py
    module2.py
"""

# __init__.py content:
"""
from .module1 import greet
from .module2 import add
"""

# module1.py content:
"""
def greet(name):
    print(f"Hello, {name}!")
"""

# module2.py content:
"""
def add(a, b):
    return a + b
"""

# Importing from your package
from my_package import greet, add

# Using functions from your package
greet("Bob")  # Output: Hello, Bob!
result = add(10, 20)
print("Result of addition:", result)  # Output: 30