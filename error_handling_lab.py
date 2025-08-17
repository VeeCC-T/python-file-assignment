# Error Handling Lab
# Ask the user for a filename and safely try to read it

filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("\n--- File Content ---\n")
        print(content)
        print("\n--- End of File ---")
except FileNotFoundError:
    print("❌ Error: The file does not exist.")
except IOError:
    print("❌ Error: Could not read the file.")
