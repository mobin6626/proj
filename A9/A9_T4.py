TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    """Collect and validate Celsius temperature."""
    user_input = input("Insert Celsius: ")
    
    # Try to convert to float
    try:
        celsius = float(user_input)
    except ValueError:
        raise ValueError(f"could not convert string to float: '{user_input}'")
    
    # Check if within range
    if not (TEMP_MIN <= celsius <= TEMP_MAX):
        raise Exception(f"{celsius} temperature out of range.")
    
    return celsius

# Main program
print("Program starting.")

try:
    temperature = collectCelsius()
    print(f"You inserted {temperature} °C")
    
except ValueError as e:
    print(f"Error: {e}")
    
except Exception as e:
    print(f"Error: {e}")

print("Program ending.")