def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")

    print(f'Reading names from "{filename}".')
    print("Analysing names...")

    # Read file and collect names
    names = []
    with open(filename, "r") as file:
        for line in file:
            name = line.strip() # remove newline and spaces
            if name != "": # skip empty lines
                names.append(name)

    # Analysis
    count = len(names)
    shortest = min(names, key=len)
    longest = max(names, key=len)
    avg_length = sum(len(name) for name in names) / count

    print("Analysis complete!")

    # Report
    print("#### REPORT BEGIN ####")
    print(f"Name count {count}")
    print(f"Shortest name {len(shortest)} chars")
    print(f"Longest name {len(longest)} chars")
    print(f"Average name {avg_length:.2f} chars")
    print("#### REPORT END ####")

    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
