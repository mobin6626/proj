from Calculator import add, subtract, multiply, divide

def main() -> None:
    """Main calculator program."""
    print("Program starting.")
    
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            # Add
            a = askValue("Insert first addend value: ")
            b = askValue("Insert second addend value: ")
            result = add(a, b)
            print(f"{a} + {b} = {result}\n")
        elif choice == 2:
            # Subtract
            a = askValue("Insert minuend value: ")
            b = askValue("Insert subtrahend value: ")
            result = subtract(a, b)
            print(f"{a} - {b} = {result}\n")
        elif choice == 3:
            # Multiply
            a = askValue("Insert multiplicant value: ")
            b = askValue("Insert multiplier value: ")
            result = multiply(a, b)
            print(f"{a} * {b} = {result}\n")
        elif choice == 4:
            # Divide
            a = askValue("Insert dividend value: ")
            b = askValue("Insert divisor value: ")
            if b == 0:
                print("Cannot divide by zero!\n")
            else:
                result = divide(a, b)
                print(f"{a} / {b} = {result}\n")
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def showOptions() -> None:
    """Display calculator menu options."""
    print("\nOptions:")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")
    print("0 - Exit")

def askChoice() -> int:
    """Get user choice and return as integer."""
    user_input = input("Your choice: ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        return -1

def askValue(PPrompt: str) -> float:
    """Ask user for a value and return as float."""
    while True:
        try:
            return float(input(PPrompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


main()