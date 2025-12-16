def main():
    print("Program starting.")
    print("This program can read a file.")

    filename = input("Enter filename: ")

    print(f'#### START "{filename}" ####')
    print("####")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Error: File not found.")

    print(f'#### END "{filename}" ####')
    print("####")

    print("Program ending.")
    return None

main()
