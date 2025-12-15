def showOptions():
    print("\nOptions:")
    print("1.- Insert-word")
    print("2.- Show current word")
    print("3.- Show current word in reverse")
    print("0.- Exit")
    return None

def askChoice():
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        print("Unknown option!")
        return -1

def main():
    print("Program starting.\n")
    
    word = "" # initialize empty string
    
    while True:
        showOptions()
        choice = askChoice()
        
        if choice == 1:
            word = input("Insert word: ")
        elif choice == 2:
            print(f'Current word: "{word}"')
        elif choice == 3:
            print(f'Word reversed: "{word[::-1]}"')
        elif choice == 0:
            print("Exiting program.")
            break
        else:
            print("Unknown option!")
    
    print("Program ending.")
    return None

main()
