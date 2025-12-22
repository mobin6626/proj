import random
import sys

random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:
    """
    Randomly places mines (represented by 9) in the PMineField.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    total_cells = rows * cols
    
    # Ensure we don't try to place more mines than cells
    if PMines > total_cells:
        PMines = total_cells
    
    mines_placed = 0
    while mines_placed < PMines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        if PMineField[row][col] != 9:  # If not already a mine
            PMineField[row][col] = 9
            mines_placed += 1

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """
    Calculates the number of adjacent mines for each non-mine cell.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    
    # Directions for 8 neighbors (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    for r in range(rows):
        for c in range(cols):
            # Skip mines
            if PMineField[r][c] == 9:
                continue
            
            mine_count = 0
            
            # Check all 8 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if neighbor is within bounds and is a mine
                if 0 <= nr < rows and 0 <= nc < cols:
                    if PMineField[nr][nc] == 9:
                        mine_count += 1
            
            PMineField[r][c] = mine_count

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    """
    Generates a complete minefield with the specified dimensions and mine count.
    """
    # 1. Clear the 2D-matrix
    PMineField.clear()
    
    # 2. Initialize with zeros
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)
    
    # 3. Lay mines
    layMines(PMineField, PMines)
    
    # 4. Calculate nearbys
    calculateNearbys(PMineField)

def readValues(PValues: list[list[int]]) -> None:
    """
    Read a minefield from a file.
    This function is used if you want to load pre-generated boards.
    """
    filename = input("Insert filename to load: ").strip()
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            PValues.clear()
            for line in lines:
                # Parse comma-separated values
                row = [int(val.strip()) for val in line.strip().split(',') if val.strip()]
                if row:  # Skip empty lines
                    PValues.append(row)
        print(f"Loaded minefield from {filename}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: File contains invalid data.")

def saveBoard(board: list[list[int]]) -> None:
    """
    Save the current board to a file in comma-separated format.
    """
    if not board:
        print("Error: No board to save.")
        return
    
    filename = input("Insert results filename: ").strip()
    if not filename:
        print("Error: No filename provided.")
        return
    
    try:
        with open(filename, 'w') as f:
            for row in board:
                # Convert each number to string and join with commas
                line = ','.join(str(cell) for cell in row)
                f.write(line + '\n')
        print(f"Board saved to '{filename}'")
    except Exception as e:
        print(f"Error saving file: {e}")

def displayBoard(board: list[list[int]]) -> None:
    """
    Display the current board in a readable format.
    """
    if not board:
        print("No board generated yet.")
        return
    
    print("Generated minesweeper board:")
    for row in board:
        # Format each row as a list
        print(f"[{', '.join(str(cell) for cell in row)}]")

def main() -> None:
    """
    Menu-driven program for generating Minesweeper boards.
    """
    print("Program starting.")
    
    current_board = []  # Store the current generated board
    
    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save generated board")
        print("0 - Exit")
        
        choice = input("Your choice: ").strip()
        
        if choice == "0":
            print("Exiting program.")
            break
        
        elif choice == "1":
            try:
                rows = int(input("Insert rows: "))
                cols = int(input("Insert columns: "))
                mines = int(input("Insert mines: "))
                
                if rows <= 0 or cols <= 0:
                    print("Error: Rows and columns must be positive integers.")
                    continue
                
                if mines < 0:
                    print("Error: Mines must be a non-negative integer.")
                    continue
                
                if mines > rows * cols:
                    print(f"Warning: More mines ({mines}) than cells ({rows*cols}). ")
                    print(f"Will place maximum possible mines.")
                
                generateMinefield(current_board, rows, cols, mines)
                print(f"Generated {rows}x{cols} board with {mines} mines.")
                
            except ValueError:
                print("Error: Please enter valid integers.")
        
        elif choice == "2":
            displayBoard(current_board)
        
        elif choice == "3":
            saveBoard(current_board)
        
        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")
    
    print("Program ending.")

main()