########################################################
# Task A9_T5
# Developer First_name Last_name
# Date 2024-01-15
########################################################

def get_color_value(color_name: str) -> int:
    """Get and validate a color value (0-255)."""
    try:
        value = int(input(f"Insert {color_name}: "))
        
        if not (0 <= value <= 255):
            raise ValueError(f"{color_name} value {value} out of range (0-255)")
        
        return value
        
    except ValueError as e:
        # Re-raise the exception with a generic message
        raise ValueError("Invalid input") from e

# Main program
print("Program starting.")

try:
    # Collect RGB values
    red = get_color_value("red")
    green = get_color_value("green")
    blue = get_color_value("blue")
    
    # All values are valid, display RGB details
    print("RGB Details:")
    print(f"- Red {red}")
    print(f"- Green {green}")
    print(f"- Blue {blue}")
    print(f"- Hex #{red:02x}{green:02x}{blue:02x}")
    
except ValueError:
    # Any invalid input triggers this
    print("Couldn't perform the designed task due to the invalid input values.")
    
except Exception:
    # Catch any other unexpected errors
    print("An unexpected error occurred.")

print("Program ending.")