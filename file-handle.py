
# Open the original file and read its content
with open("input.txt", "r") as original_file:
    content = original_file.read()

# Modify the content (e.g., make it uppercase)
modified_content = content.upper()

# Write the modified content to a new file
with open("output.txt", "w") as new_file:
    new_file.write(modified_content)

print("File has been read and written successfully.")

#exception handling
filename = input("Enter the filename you want to read: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Sorry, the file does not exist.")