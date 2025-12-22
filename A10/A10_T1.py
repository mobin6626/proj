def main():
    # Prompt for filename
    filename = input("Insert a filename: ").strip()
    
    try:
        # Read file and process content
        with open(filename, 'r') as file:
            lines = []
            for line in file:
                stripped = line.strip()
                if stripped:  # Ignore empty lines
                    lines.append(stripped)
        
        # Display vertically
        print("\nVertical display:")
        for item in lines:
            print(item)
        
        # Display horizontally
        print("\nHorizontal display:")
        if lines:
            print(", ".join(lines))
        else:
            print("(No data)")
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()