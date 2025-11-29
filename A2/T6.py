print("Program starting.")
    
# Get hex color input from user
hex_color = input("Insert a hex color: ").strip().upper()
    
# Validate the input
if len(hex_color) != 7 or hex_color[0] != '#' or not all(c in '0123456789ABCDEF' for c in hex_color[1:]):
    print("Invalid hex color format. Expected format: #RRGGBB (e.g., #FFA500)")
    print("Program ending.")
    
    
# Extract RGB components
red = hex_color[1:3]
green = hex_color[3:5]
blue = hex_color[5:7]
    
# Display the results
print("Colors")
print(f" - Red {red}")
print(f" - Green {green}")
print(f" - Blue {blue}")
    
print("Program ending.")