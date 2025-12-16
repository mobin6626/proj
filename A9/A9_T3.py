import sys

print("Program starting.")

filename = input("Insert filename: ")

try:
    # Try to open and read the file
    with open(filename, 'r') as file:
        content = file.read()
    
    # Display the content with filename header
    print(f"## {filename} ##")
    print(content.strip())
    print(f"## {filename} ##")
    
except FileNotFoundError:
    # File doesn't exist
    print(f"Error: File '{filename}' doesn't exist!")
    sys.exit(1)
    
except PermissionError:
    # No permission to read the file
    print(f"Error: No permission to read '{filename}'!")
    sys.exit(1)
    
except Exception as e:
    # Any other error
    print(f"Error reading file: {e}")
    sys.exit(1)

print("Program ending.")