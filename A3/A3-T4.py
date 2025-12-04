def reverse_name(name):
    return name[::-1]

def first_char(name):
    return name[0] if name else ''

def name_length(name):
    return len(name)

def menu():
    print("Program starting.")
    name = input("Before the menu, please insert your name: ")

    while True:
        print("""
Options:
1--Print welcome message
2--Print the name backwards
3--Print the first character
4--Show the amount of characters in the name
0--Exit
        """)

        choice = input("Your choice: ")
        
        if choice == '1':
            print(f"Welcome {name}!")
        elif choice == '2':
            print(f"Your name backwards is \"{reverse_name(name)}\"")
        elif choice == '3':
            print(f"The first character in name \"{name}\" is \"{first_char(name)}\"")
        elif choice == '4':
            print(f"There are {name_length(name)} characters in the name \"{name}\"")
        elif choice == '0':
            print("Program ending.")
            break
        else:
            print("Invalid choice, please try again.")

menu()
