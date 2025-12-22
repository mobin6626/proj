import sys

def bubblesort(PValues: list[int], PAsc: bool = True) -> None:
    """
    Sort PValues in-place using bubble sort algorithm.
    
    Args:
        PValues: List of integers to sort
        PAsc: If True, sort in ascending order; if False, sort in descending order
    """
    n = len(PValues)
    
    # If list is empty or has 1 element, it's already sorted
    if n <= 1:
        return
    
    # Outer loop for passes
    for i in range(n - 1):
        # Inner loop for comparisons
        # We go up to n - i - 1 because the last i elements are already sorted
        for j in range(0, n - i - 1):
            # Determine if we need to swap based on sort order
            if PAsc:
                # Ascending order: swap if current > next
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
            else:
                # Descending order: swap if current < next
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]


def read_numbers_from_file(filename: str) -> list[int]:
    """
    Read integers from a file.
    
    Args:
        filename: Name of the file to read
        
    Returns:
        List of integers read from the file
    """
    numbers = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove whitespace and skip empty lines
                line = line.strip()
                if line:
                    try:
                        numbers.append(int(line))
                    except ValueError:
                        print(f"Warning: Skipping non-integer value: '{line}'")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)
    
    return numbers


def write_numbers_to_file(filename: str, numbers: list[int]) -> None:
    """
    Write integers to a file.
    
    Args:
        filename: Name of the file to write to
        numbers: List of integers to write
    """
    try:
        # Create output filename by adding '_sorted' before extension
        if '.' in filename:
            name_parts = filename.rsplit('.', 1)
            output_filename = f"{name_parts[0]}_sorted.{name_parts[1]}"
        else:
            output_filename = f"{filename}_sorted"
        
        with open(output_filename, 'w') as file:
            for number in numbers:
                file.write(f"{number}\n")
        
        print(f"Sorted data written to: {output_filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")
        sys.exit(1)


def main():
    """
    Main program to read numbers from a file, sort them, and write back.
    """
    filename = None
    
    # Check command line arguments
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    elif len(sys.argv) == 1:
        # No command line arguments, prompt for filename
        filename = input("Enter the filename to sort: ").strip()
    else:
        print("Usage: python script.py [filename]")
        print("If no filename is provided, you will be prompted for one.")
        sys.exit(1)
    
    if not filename:
        print("Error: No filename provided.")
        sys.exit(1)
    
    # Read numbers from file
    print(f"Reading numbers from '{filename}'...")
    numbers = read_numbers_from_file(filename)
    
    if not numbers:
        print("No valid integers found in the file.")
        sys.exit(0)
    
    print(f"Read {len(numbers)} numbers from the file.")
    
    # Ask for sort order
    while True:
        order_input = input("Sort in ascending order? (y/n): ").strip().lower()
        if order_input in ['y', 'yes', '']:
            ascending = True
            print("Sorting in ascending order...")
            break
        elif order_input in ['n', 'no']:
            ascending = False
            print("Sorting in descending order...")
            break
        else:
            print("Please enter 'y' for ascending or 'n' for descending.")
    
    # Create a copy for display (original will be modified in-place)
    original = numbers.copy()
    
    # Sort the numbers
    bubblesort(numbers, ascending)
    
    # Display results
    print(f"\nOriginal list (first 10): {original[:10]}")
    print(f"Sorted list (first 10): {numbers[:10]}")
    
    # Ask if user wants to save to file
    save_input = input("\nSave sorted data to file? (y/n): ").strip().lower()
    if save_input in ['y', 'yes']:
        write_numbers_to_file(filename, numbers)
    
    print("Done!")


main()