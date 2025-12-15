def main():
    """
    Main function representing the main program logic including menu cycle.
    """
    print("Program starting.")
    
    # Initialize counter
    counter = 0
    
    while True:
        # Show options
        showOptions()
        
        # Get user choice
        choice = askChoice()
        
        # Process choice
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            # Show count
            print(f"Current count - {counter}\n")
        elif choice == 2:
            # Increase count
            counter += 1
            print(f"Count increased. New count - {counter}\n")
        elif choice == 3:
            # Reset count
            counter = 0
            print("Count reset to zero.\n")
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def showOptions():
    """
    Takes no arguments, shows the available options in the standard output
    and returns None.
    """
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")

def askChoice():
    """
    Takes no arguments, prompts user to insert choice and returns an integer
    regardless of the user feed.
    """
    user_input = input("Your choice: ")
    
    # Check if input is numeric
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        # Return a number that's not in our valid choices
        return -1

main()