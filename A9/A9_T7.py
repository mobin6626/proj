import sys
import os

def show_help() -> None:
    """Display help message with usage instructions."""
    print("Usage: python A9_T7.py <source_file> <destination_file>")
    print("Copies content from source file to destination file.")

def copy_file(src_file: str, dst_file: str) -> bool:
    """
    Copy content from source file to destination file.
    Returns True if successful, False otherwise.
    """
    # Check if source file exists
    if not os.path.exists(src_file):
        print(f'Error: Source file "{src_file}" not found!')
        return False
    
    # Check if destination file exists
    if os.path.exists(dst_file):
        print(f'Destination file "{dst_file}" already exists.')
        choice = input("Overwrite (y/n)?: ").strip().lower()
        if choice != 'y':
            print("Copy cancelled.")
            return False
    
    try:
        # Read source file
        with open(src_file, 'r', encoding='utf-8') as src:
            content = src.read()
        
        # Write to destination file
        with open(dst_file, 'w', encoding='utf-8') as dst:
            dst.write(content)
        
        print(f'Copied file "{src_file}" to "{dst_file}".')
        return True
        
    except FileNotFoundError:
        print(f'Error: File not found!')
        return False
    except PermissionError:
        print(f'Error: No permission to access file!')
        return False
    except Exception as e:
        print(f'Error during copy: {e}')
        return False

def main() -> None:
    """Main program for CLI copy tool."""
    print("Program starting.")
    
    # Check argument count
    if len(sys.argv) != 3:
        print(f"Error: Invalid amount of arguments ({len(sys.argv) - 1} given, expected 2).")
        show_help()
        sys.exit(1)
    
    # Get file names from arguments
    src_file = sys.argv[1]
    dst_file = sys.argv[2]
    
    print(f'Source file "{src_file}"')
    print(f'Destination file "{dst_file}"')
    
    # Attempt to copy file
    if copy_file(src_file, dst_file):
        print("Copy successful!")
    else:
        print("Copy failed!")
        sys.exit(-1)
    
    print("Program ending.")

main()