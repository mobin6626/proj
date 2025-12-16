def main() -> None:
    """Main program with save before exit functionality."""
    print("Program starting.")
    
    lines = []  # Store user lines
    
    try:
        while True:
            show_options()
            
            try:
                choice = input("Your choice: ")
                
                if choice == "0":
                    print("Exiting program.")
                    break
                    
                elif choice == "1":
                    # Insert line
                    text = input("Insert text: ")
                    lines.append(text)
                    print()
                    
                elif choice == "2":
                    # Save lines
                    if not lines:
                        print("No lines to save.\n")
                        continue
                    
                    filename = input("Insert filename: ")
                    save_lines(filename, lines)
                    print(f"Lines saved to {filename}\n")
                    
                else:
                    print("Unknown option!\n")
                    
            except KeyboardInterrupt:
                # Handle CTRL+C during input
                handle_keyboard_interrupt(lines)
                break
                
    except KeyboardInterrupt:
        # Handle CTRL+C at menu level
        handle_keyboard_interrupt(lines)
    
    print("Program ending.")

def show_options() -> None:
    """Display menu options."""
    print("Options:")
    print("1 - Insert line")
    print("2 - Save lines")
    print("0 - Exit")

def save_lines(filename: str, lines: list) -> None:
    """Save lines to a file."""
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')
    except Exception as e:
        print(f"Error saving file: {e}")

def handle_keyboard_interrupt(lines: list) -> None:
    """Handle KeyboardInterrupt with save prompt."""
    print("^CKeyboard interrupt and unsaved progress!", end='')
    
    if not lines:
        print("\nNo lines to save.")
        return
    
    print()
    confirm = input("Save before quit(y/n)?: ").strip().lower()
    
    if confirm == 'y':
        filename = input("Insert filename: ")
        save_lines(filename, lines)
        print(f"Lines saved to {filename}")

main()