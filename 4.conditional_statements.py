# ------------------ Conditional Statements ------------------
# Example: if, elif, else
sunny = True

if sunny:
    print("Today is sunny!")
else:
    print("Today is not sunny :(")

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