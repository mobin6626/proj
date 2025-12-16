import svgwrite
from svgwrite import Drawing

# Import functions from library
import svg_lib

def main() -> None:
    """Main SVG drawing program."""
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
            
            print("Insert square")
            left = get_float_input("- Left edge position: ")
            top = get_float_input("- Top edge position: ")
            side = get_float_input("- Side length: ")
            fill_color = input("- Fill color: ").strip().lower()
            stroke_color = input("- Stroke color: ").strip().lower()
            
            svg_lib.drawSquare(dwg, left, top, side, fill_color, stroke_color)
            print("Square added to drawing.\n")
            
        elif choice == 2:
            # Draw circle
            if not drawing_initialized:
                dwg = initialize_drawing()
                drawing_initialized = True
                print("New drawing created.\n")
            
            print("Insert circle")
            center_x = get_float_input("- Center X position: ")
            center_y = get_float_input("- Center Y position: ")
            radius = get_float_input("- Radius: ")
            fill_color = input("- Fill color: ").strip().lower()
            stroke_color = input("- Stroke color: ").strip().lower()
            
            svg_lib.drawCircle(dwg, center_x, center_y, radius, fill_color, stroke_color)
            print("Circle added to drawing.\n")
            
        elif choice == 3:
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
                success = svg_lib.saveSvg(dwg, filename)
                if success:
                    print("Vector saved successfully!\n")
                else:
                    print("Failed to save file.\n")
            else:
                print("Save cancelled.\n")
                
        else:
            print("Unknown option!\n")
    
    print("Program ending.")

def show_options() -> None:
    """Display menu options."""
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Save svg")
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
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def initialize_drawing() -> Drawing:
    """Initialize a new SVG drawing."""
    return svgwrite.Drawing(size=("400px", "300px"))

main()