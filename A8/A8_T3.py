def main() -> None:
    """Main program for analyzing number files."""
    print("Program starting.")
    
    values_list = []  # Store the read values
    
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            # Read values from file
            values_list = readValues()
        elif choice == 2:
            # Amount of values
            amount = amountOfValues(values_list)
            print(f"Amount of values {amount}\n")
        elif choice == 3:
            # Calculate sum
            total = calculateSum(values_list)
            print(f"Sum of values {total}\n")
        elif choice == 4:
            # Calculate average
            average = calculateAverage(values_list)
            print(f"Average of values {average}\n")
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def showOptions() -> None:
    """Display menu options."""
    print("\nOptions:")
    print("1 - Read values")
    print("2 - Amount of values")
    print("3 - Calculate sum of values")
    print("4 - Calculate average of values")
    print("0 - Exit")

def askChoice() -> int:
    """Get user choice and return as integer."""
    user_input = input("Your choice: ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        return -1

def readValues() -> list[float]:
    """Read values from a file and return as list of floats."""
    filename = input("Insert filename: ")
    values = []
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        value = float(line)
                        values.append(value)
                    except ValueError:
                        print(f"Warning: Skipping invalid value '{line}'")
        
        print(f"Read {len(values)} values from {filename}\n")
        return values
    
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!\n")
        return []
    except Exception as e:
        print(f"Error reading file: {e}\n")
        return []

def amountOfValues(values: list[float]) -> int:
    """Return the amount of values in the list."""
    return len(values)

def calculateSum(values: list[float]) -> float:
    """Calculate and return the sum of values, rounded to 1 decimal."""
    if not values:
        return 0.0
    
    total = sum(values)
    return round(total, 1)

def calculateAverage(values: list[float]) -> float:
    """Calculate and return the average of values, rounded to 1 decimal."""
    if not values:
        return 0.0
    
    total = sum(values)
    average = total / len(values)
    return round(average, 1)

main()