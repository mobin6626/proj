def main():
    print("Program starting.")

    first = input("Enter first name: ")
    last = input("Enter last name: ")
    filename = input("Enter filename: ")

    
    with open(filename, "w") as file:
        file.write(first + "\n")
        file.write(last + "\n")
        file.write("\n") 

    print("Program ending.")
    return None

main()
