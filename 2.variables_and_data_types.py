# ------------------ Variables and Data Types ------------------
# Integers
age = 25
print("Age:", age)
print("Type of age:", type(age))  # Output: <class 'int'>

# Floating-Point Numbers
height = 5.9
print("Height:", height)
print("Type of height:", type(height))  # Output: <class 'float'>

# Strings
name = "Alice"
print("Name:", name)
print("Type of name:", type(name))  # Output: <class 'str'>

# Booleans
is_student = True
print("Is student:", is_student)
print("Type of is_student:", type(is_student))  # Output: <class 'bool'>

# Type Conversion
num_str = "123"
num_int = int(num_str)  # Convert string to integer
print("Converted integer:", num_int)
print("Type of num_int:", type(num_int))  # Output: <class 'int'>

# ------------------ Input and Output ------------------
# Taking User Input
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

# Formatting Output
# Using f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")

# Using .format() method
print("Name: {}, Age: {}".format(name, age))

# Using %-formatting (older style)
print("Name: %s, Age: %s" % (name, age))

# ------------------ Operators ------------------
# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b)        # Output: 13
print("Subtraction:", a - b)     # Output: 7
print("Multiplication:", a * b)  # Output: 30
print("Division:", a / b)        # Output: 3.333...
print("Floor Division:", a // b) # Output: 3
print("Modulus:", a % b)         # Output: 1
print("Exponent:", a ** b)       # Output: 1000

# Comparison Operators
print("Is a > b?", a > b)        # Output: True
print("Is a == b?", a == b)      # Output: False
print("Is a != b?", a != b)      # Output: True

# Logical Operators
x = True
y = False
print("x and y:", x and y)       # Output: False
print("x or y:", x or y)         # Output: True
print("not x:", not x)           # Output: False

# Assignment Operators
c = 5
c += 2  # Equivalent to c = c + 2
print("c after += 2:", c)        # Output: 7

c *= 3  # Equivalent to c = c * 3
print("c after *= 3:", c)        # Output: 21