# ------------------ Lists ------------------
# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])  # Output: apple
print("Last fruit:", fruits[-1])  # Output: cherry

# Modifying elements
fruits[1] = "blueberry"
print("Updated fruits:", fruits)  # Output: ['apple', 'blueberry', 'cherry']

# List methods
fruits.append("orange")  # Add an item to the end
print("After append:", fruits)

fruits.insert(1, "mango")  # Insert an item at a specific position
print("After insert:", fruits)

fruits.remove("blueberry")  # Remove an item
print("After remove:", fruits)

fruits.pop()  # Remove the last item
print("After pop:", fruits)

# List slicing
print("First two fruits:", fruits[:2])  # Output: ['apple', 'mango']

# List comprehension
squares = [x**2 for x in range(5)]
print("Squares:", squares)  # Output: [0, 1, 4, 9, 16]

# ------------------ Tuples ------------------
# Creating a tuple
coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)

# Accessing elements
print("X coordinate:", coordinates[0])  # Output: 10.0

# Tuples are immutable (cannot be changed)
# coordinates[0] = 15.0  # This will raise an error

# Packing and unpacking
x, y = coordinates
print("X:", x, "Y:", y)  # Output: X: 10.0 Y: 20.0

# ------------------ Sets ------------------
# Creating a set
unique_numbers = {1, 2, 3, 3, 4}
print("Unique numbers:", unique_numbers)  # Output: {1, 2, 3, 4}

# Adding elements
unique_numbers.add(5)
print("After adding 5:", unique_numbers)

# Removing elements
unique_numbers.remove(3)
print("After removing 3:", unique_numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))        # Output: {1, 2, 3, 4, 5}
print("Intersection:", set1.intersection(set2))  # Output: {3}
print("Difference:", set1.difference(set2))      # Output: {1, 2}

# ------------------ Dictionaries ------------------
# Creating a dictionary
person = {"name": "Alice", "age": 25, "is_student": True}
print("Person:", person)

# Accessing values
print("Name:", person["name"])  # Output: Alice

# Modifying values
person["age"] = 26
print("Updated person:", person)

# Adding new key-value pairs
person["city"] = "New York"
print("After adding city:", person)

# Dictionary methods
print("Keys:", person.keys())    # Output: dict_keys(['name', 'age', 'is_student', 'city'])
print("Values:", person.values())  # Output: dict_values(['Alice', 26, True, 'New York'])
print("Items:", person.items())   # Output: dict_items([('name', 'Alice'), ('age', 26), ...])

# Removing items
person.pop("is_student")
print("After popping is_student:", person)