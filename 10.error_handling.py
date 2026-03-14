# ------------------ Handling Exceptions ------------------
# Basic try-except block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# ------------------ Finally ------------------
# try-except-finally block
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    print("This will always execute.")
    file.close()  # Ensure the file is closed

# ------------------ Raising Exceptions ------------------
# Raising an exception manually
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        print("You are a minor.")
    else:
        print("You are an adult.")

try:
    check_age(-5)
except ValueError as e:
    print(e)  # Output: Age cannot be negative!

# ------------------ Custom Exceptions ------------------
# Creating a custom exception
class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative!"):
        self.message = message
        super().__init__(self.message)

# Using the custom exception
def validate_number(num):
    if num < 0:
        raise NegativeNumberError()
    print("Number is valid.")

try:
    validate_number(-10)
except NegativeNumberError as e:
    print(e)  # Output: Number cannot be negative!
