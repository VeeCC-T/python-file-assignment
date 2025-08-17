# File Read & Write Challenge
# Reads input.txt, converts content to UPPERCASE, writes to output.txt

with open("input.txt", "r") as infile:
    content = infile.read()

# Modify content (make uppercase)
modified_content = content.upper()

with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

print("✅ File has been modified and saved as output.txt")
