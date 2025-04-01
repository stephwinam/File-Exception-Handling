# Ask for a filename
filename = input("Enter the filename: ")

try:
    # Open the file for reading
    with open(filename, "r") as file:
        content = file.read()

    # Modify content (convert to uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    new_filename = "modified_" + filename
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)

    print(f"Modified content saved in {new_filename}")

except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: Cannot read the file.")
