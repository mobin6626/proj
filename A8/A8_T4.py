from datetime import datetime
import datetime_lib

def main() -> None:
    """Main program for timestamp analysis."""
    print("Program starting.")
    
    timestamps = []
    filename = ""
    
    # Ask for filename at the start
    filename = input("Insert filename: ")
    datetime_lib.readTimestamps(filename, timestamps)
    
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 0:
            print("Exiting program.\n")
            break
        elif choice == 1:
            # Calculate by year
            if not timestamps:
                print("No timestamps loaded. Please read a file first.\n")
                continue
                
            try:
                year = int(input("Insert year: "))
                count = datetime_lib.calculateYears(year, timestamps)
                print(f"Amount of timestamps during year '{year}' is {count}\n")
            except ValueError:
                print("Invalid year. Please enter a number.\n")
                
        elif choice == 2:
            # Calculate by month
            if not timestamps:
                print("No timestamps loaded. Please read a file first.\n")
                continue
                
            month = input("Insert month: ").strip()
            if month in datetime_lib.MONTHS:
                count = datetime_lib.calculateMonths(month, timestamps)
                print(f"Amount of timestamps during month '{month}' is {count}\n")
            else:
                print(f"Invalid month. Please use full month name (e.g., 'April').\n")
                print(f"Valid months: {', '.join(datetime_lib.MONTHS)}\n")
                
        elif choice == 3:
            # Calculate by weekday
            if not timestamps:
                print("No timestamps loaded. Please read a file first.\n")
                continue
                
            weekday = input("Insert weekday: ").strip()
            if weekday in datetime_lib.WEEKDAYS:
                count = datetime_lib.calculateWeekdays(weekday, timestamps)
                print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")
            else:
                print(f"Invalid weekday. Please use full weekday name (e.g., 'Monday').\n")
                print(f"Valid weekdays: {', '.join(datetime_lib.WEEKDAYS)}\n")
                
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def showOptions() -> None:
    """Display menu options."""
    print("\nOptions:")
    print("1 - Calculate amount of timestamps during year")
    print("2 - Calculate amount of timestamps during month")
    print("3 - Calculate amount of timestamps during weekday")
    print("0 - Exit")

def askChoice() -> int:
    """Get user choice and return as integer."""
    user_input = input("Your choice: ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        return -1

main()