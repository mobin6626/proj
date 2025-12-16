print("Program starting.\n")

total = 0.0

while True:
    try:
        value = input("Insert a floating-point value (0 to stop): ")
        
        # Try to convert to float
        num = float(value)
        
        if num == 0:
            break
        
        total += num
        
    except ValueError:
        print(f"Error! '{value}' couldn't be converted to float.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
        break

print(f"\nFinal sum is {total:.2f}")
print("Program ending.")