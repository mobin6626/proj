def askName():
    """Prompts the user to insert a name and returns it."""
    name = input("Insert name: ")
    return name

def greetUser(PName):
    """Greets the user with the provided name."""
    print(f"Hello-{PName}!")
    return None

def main():
    """Main program logic."""
    print("Program-starting.\n")
    
    name = askName()
    greetUser(name)
    
    print("Program-ending.")
    return None

main()
