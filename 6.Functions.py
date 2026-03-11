# ------------------ Defining Functions ------------------
# Basic function
def greet():
    print("Hello, World!")

greet()  # Calling the function

# Function with parameters
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")  # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}.")

add_numbers(5, 3)  # Output: The sum of 5 and 3 is 8.

# ------------------ Return Values ------------------
# Function with a return value
def multiply(a, b):
    return a * b

product = multiply(4, 5)
print("Product:", product)  # Output: Product: 20

# Returning multiple values
def calculate(a, b):
    return a + b, a - b, a * b

sum_result, diff_result, prod_result = calculate(10, 5)
print("Sum:", sum_result)       # Output: Sum: 15
print("Difference:", diff_result)  # Output: Difference: 5
print("Product:", prod_result)  # Output: Product: 50

# ------------------ Scope and Lifetime of Variables ------------------
# Global vs Local Variables
x = 10  # Global variable

def my_function():
    y = 5  # Local variable
    print("Inside function - x:", x)  # Accessing global variable
    print("Inside function - y:", y)

my_function()
print("Outside function - x:", x)
# print("Outside function - y:", y)  # This will raise an error (y is local)

# ------------------ Lambda Functions ------------------
# Lambda function (anonymous function)
square = lambda x: x ** 2
print("Square of 5:", square(5))  # Output: Square of 5: 25

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)  # Output: Squared numbers: [1, 4, 9, 16, 25]

# ------------------ Built-in Functions ------------------
# len() - Length of a sequence
fruits = ["apple", "banana", "cherry"]
print("Number of fruits:", len(fruits))  # Output: Number of fruits: 3

# range() - Generate a sequence of numbers
for i in range(3):
    print(i)  # Output: 0, 1, 2

# map() - Apply a function to all items in a list
def double(x):
    return x * 2

numbers = [1, 2, 3]
doubled_numbers = list(map(double, numbers))
print("Doubled numbers:", doubled_numbers)  # Output: Doubled numbers: [2, 4, 6]

# filter() - Filter items based on a condition
def is_even(x):
    return x % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)  # Output: Even numbers: [2]