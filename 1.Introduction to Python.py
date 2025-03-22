# ------------------ Writing Your First Python Program ------------------
print("Hello, World!")

# ------------------ Comments and Docstrings ------------------
# This is a single-line comment

"""
This is a multi-line comment (docstring).
It can span multiple lines and is often used to describe the purpose of a program or function.
"""

# Example of a docstring for a function
def greet(name):
    """
    This function greets the user.
    :param name: The name of the user
    """
    print(f"Hello, {name}!")

greet("Alice")

# ------------------ Indentation and Code Structure ------------------
def check_number(num):
    if num > 0:
        print("The number is positive.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is negative.")

check_number(5)
check_number(-3)
check_number(0)