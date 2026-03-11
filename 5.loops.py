# ------------------ Conditional Statements ------------------
# Example: if, elif, else
age = 18

if age < 13:
    print("You are a child.")
elif 13 <= age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Nested Conditions
num = 10

if num > 0:
    print("The number is positive.")
    if num % 2 == 0:
        print("It is also even.")
    else:
        print("It is also odd.")
else:
    print("The number is not positive.")

# ------------------ Loops ------------------
# for Loop
# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over a range
for i in range(5):  # range(5) generates numbers 0 to 4
    print(i)

# while Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1  # Increment count by 1

# ------------------ Loop Control Statements ------------------
# break Statement
for i in range(10):
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)

# continue Statement
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# pass Statement
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print(i)