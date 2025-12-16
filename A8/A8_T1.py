import time

def main():
    """
    Main function for the pause program.
    """
    print("Program starting.")
    
    pause_duration = 0.0  # Default pause duration
    
    while True:
        show_options()
        choice = get_choice()
        
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            pause_duration = set_pause_duration()
        elif choice == 2:
            activate_pause(pause_duration)
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def show_options():
    """
    Display the menu options.
    """
    print("\nOptions:")
    print("1 - Set pause duration")
    print("2 - Activate pause")
    print("0 - Exit")

def get_choice():
    """
    Get user choice and return as integer.
    """
    while True:
        user_input = input("Your choice: ")
        if user_input.isnumeric():
            return int(user_input)
        else:
            print("Unknown option!")
            return -1  # Return invalid choice

def set_pause_duration():
    """
    Ask user for pause duration and return it.
    """
    try:
        duration = float(input("Insert pause duration (s): "))
        if duration < 0:
            print("Duration cannot be negative!")
            return 0.0
        return duration
    except ValueError:
        print("Invalid input! Using default duration 0.0")
        return 0.0

def activate_pause(duration):
    """
    Activate the pause for given duration.
    """
    if duration <= 0:
        print("Pause duration not set or invalid.")
        return
    
    print(f"Pausing for {duration} seconds.")
    time.sleep(duration)
    print("Unpaused.")

main()