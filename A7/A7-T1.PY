def main():
    print("Program starting.")
    print("Collect positive integers.")

    numbers: list[int] = []

    while True:
        value = int(input("Insert positive integer (negative stops): "))

        if value < 0:
            break
        numbers.append(value)

    print("Stopped collecting positive integers.")

    if len(numbers) == 0:
        print("No integers to display.")
    else:
        print(f"Displaying {len(numbers)} integers:")
        for index, num in enumerate(numbers):
            ordinal = index + 1
            print(f"Index {index} => Ordinal {ordinal} => Integer {num}")

    print("Program ending.")

main()
