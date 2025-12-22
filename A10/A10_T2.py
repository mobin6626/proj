########################################################
# Task A10_T2
# Developer Mina Mehdizadeh
# Date 2025-12-15
########################################################

import sys


def readValues(PFilename: str, PValues: list[int]) -> None:
    """
    Read integers from file, filter empty rows, and add to PValues list.
    """
    try:
        with open(PFilename, "r") as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if line:  # Skip empty rows
                    try:
                        value = int(line)
                        PValues.append(value)
                    except ValueError:
                        print(f"Error: Line {line_num} contains invalid integer: '{line}'")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)
    
    return None


def sumOfValues(PValues: list[int]) -> int:
    """
    Calculate the sum of all values in the list.
    """
    total = 0
    for value in PValues:
        total += value
    return total


def productOfValues(PValues: list[int]) -> int:
    """
    Calculate the product of all values in the list.
    """
    if not PValues:  # Empty list
        return 0
    
    product = 1
    for value in PValues:
        product *= value
    
    return product


def main() -> None:
    """
    Main program for analyzing integers in a text file.
    """
    # 1. Initialize
    Values: list[int] = []
    
    # 2. Operate
    print("Program starting.")
    
    # 2.1 ask filename
    filename = input("Insert filename: ")
    
    # 2.2 read values
    readValues(filename, Values)
    
    # 2.3 calculate sum of values
    total_sum = sumOfValues(Values)
    
    # 2.4 calculate product of values
    total_product = productOfValues(Values)
    
    # 2.5 display results
    print("# --- Sum of numbers --- #")
    print(total_sum)
    print("# --- Sum of numbers --- #")
    
    print("# --- Product of numbers --- #")
    print(total_product)
    print("# --- Product of numbers --- #")
    
    # 3. Cleanup
    Values.clear()
    print("Program ending.")
    
    return None

main()