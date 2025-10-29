source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
with open(source_file, "r") as src:
    with open(destination_file, "w") as dest:
        content = src.read()
        dest.write(content)

print(f"Contents of '{source_file}' copied to '{destination_file}' successfully!")
