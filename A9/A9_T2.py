import sys

print("Program starting.")

try:
    # Get exit code from user
    user_input = input("Insert exit code(0-255): ")
    
    # Convert to integer
    exit_code = int(user_input)
    
    # Validate range
    if 0 <= exit_code <= 255:
        print("Clean exit")
        sys.exit(exit_code)
    else:
        print(f"Error: {exit_code} is not within 0-255 range.")
        sys.exit(1)
        
except ValueError:
    print(f"Error: '{user_input}' is not a valid number.")
    sys.exit(1)
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
    sys.exit(1)