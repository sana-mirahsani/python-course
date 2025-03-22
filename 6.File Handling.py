# ------------------ Reading and Writing Files ------------------
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a sample file.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:\n", content)

# Reading line by line
with open("example.txt", "r") as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())  # strip() removes extra newline characters

# ------------------ File Modes ------------------
# Append mode
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

# Reading after appending
with open("example.txt", "r") as file:
    print("File content after appending:\n", file.read())

# Binary mode (writing and reading binary data)
with open("binary_example.bin", "wb") as file:
    file.write(b"Binary data example")

with open("binary_example.bin", "rb") as file:
    print("Binary content:", file.read())

# ------------------ Working with Directories ------------------
import os

# Check if a file exists
if os.path.exists("example.txt"):
    print("example.txt exists!")

# Get the current working directory
print("Current working directory:", os.getcwd())

# List files in a directory
print("Files in current directory:", os.listdir())

# Create a new directory
os.mkdir("new_directory")
print("Created new_directory")

# Rename a directory
os.rename("new_directory", "renamed_directory")
print("Renamed new_directory to renamed_directory")

# Remove a directory
os.rmdir("renamed_directory")
print("Removed renamed_directory")