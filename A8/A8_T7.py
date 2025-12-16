import svgwrite
from svgwrite import Drawing
import math

# Import functions from library
import geometry_lib

def main() -> None:
    """Main program for drawing shapes."""
    print("Program starting.")
    
    # Initialize drawing
    dwg = None
    drawing_initialized = False
    
    while True:
        show_options()
        choice = ask_choice()
        
        if choice == 0:
            print("Exiting program.\n")
            break
            
        elif choice == 1:
            # Draw square
            if not drawing_initialized:
                dwg = initialize_drawing()
                drawing_initialized = True
                print("New drawing created.\n")
            
            print("Insert square details:")
            left = get_float_input("- Left edge position: ")
            top = get_float_input("- Top edge position: ")
            side = get_float_input("- Side length: ")
            fill_color = input("- Insert fill: ").strip().lower()
            stroke_color = input("- Insert stroke: ").strip().lower()
            
            geometry_lib.draw_square(dwg, left, top, side, fill_color, stroke_color)
            print("Square added to drawing.\n")
            
        elif choice == 2:
            # Draw circle
            if not drawing_initialized:
                dwg = initialize_drawing()
                drawing_initialized = True
                print("New drawing created.\n")
            
            print("Insert circle details:")
            center_x = get_float_input("- Center X position: ")
            center_y = get_float_input("- Center Y position: ")
            radius = get_float_input("- Radius: ")
            fill_color = input("- Insert fill: ").strip().lower()
            stroke_color = input("- Insert stroke: ").strip().lower()
            
            geometry_lib.draw_circle(dwg, center_x, center_y, radius, fill_color, stroke_color)
            print("Circle added to drawing.\n")
            
        elif choice == 3:
            # Draw hexagon
            if not drawing_initialized:
                dwg = initialize_drawing()
                drawing_initialized = True
                print("New drawing created.\n")
            
            print("Insert hexagon details:")
            center_x = get_float_input("- Middle point X: ")
            center_y = get_float_input("- Middle point Y: ")
            apothem = get_float_input("- Apothem length: ")
            fill_color = input("- Insert fill: ").strip().lower()
            stroke_color = input("- Insert stroke: ").strip().lower()
            
            geometry_lib.draw_hexagon(dwg, center_x, center_y, apothem, fill_color, stroke_color)
            print("Hexagon added to drawing.\n")
            
            # Show calculated points (optional)
            show_hexagon_points(center_x, center_y, apothem)
            
        elif choice == 4:
            # Save SVG
            if not drawing_initialized:
                print("No drawing to save. Please draw something first.\n")
                continue
            
            filename = input("Insert filename: ").strip()
            if not filename.endswith('.svg'):
                filename += '.svg'
            
            print(f'Saving file to "{filename}"')
            confirm = input("Proceed (y/n)?: ").strip().lower()
            
            if confirm == 'y':
                success = geometry_lib.save_svg(dwg, filename)
                if success:
                    print("Vector saved successfully!\n")
                else:
                    print("Failed to save file.\n")
            else:
                print("Save cancelled.\n")
                
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def show_hexagon_points(center_x: float, center_y: float, apothem: float) -> None:
    """Calculate and display hexagon points."""
    import math
    
    # Calculate circumradius
    circumradius = apothem / (math.sqrt(3) / 2)
    
    print("\nHexagon points (rounded to integers):")
    for i in range(6):
        angle_deg = 30 + (i * 60)
        angle_rad = math.radians(angle_deg)
        
        x = center_x + circumradius * math.cos(angle_rad)
        y = center_y + circumradius * math.sin(angle_rad)
        
        point_names = ["Top Right", "Right", "Bottom Right", 
                      "Bottom Left", "Left", "Top Left"]
        
        print(f"{point_names[i]}: ({round(x)}, {round(y)})")

def show_options() -> None:
    """Display menu options."""
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def ask_choice() -> int:
    """Get user choice and return as integer."""
    user_input = input("Your choice: ")
    if user_input.isnumeric():
        return int(user_input)
    else:
        print("Unknown option!")
        return -1

def get_float_input(prompt: str) -> float:
    """Get float input from user."""
    while True:
        try:
            value = input(prompt)
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

def initialize_drawing() -> Drawing:
    """Initialize a new SVG drawing."""
    return svgwrite.Drawing(size=("200px", "200px"))

main()