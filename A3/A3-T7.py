print("Program Starting...\n")
print("Testing decision structures")

num = int(input("Insert an integer: "))

print("\nOptions:")
print("1 - In one multi-branched decision structure")
print("2 - In multiple independent if-statements")
print("0 - Exit")

choice = input("Your choice: ")

# Multi-branched if-elif-else
if choice == "1":
    print("Using one multi-branched decision structure.")
    if num < 0:
        result = num - 10
    elif num == 0:
        result = 0
    elif num < 100:
        result = num + 100
    elif num < 500:
        result = num + 22
    else:
        result = num * 2
    print(f"Result is: {result}")

# Multiple independent if statements
elif choice == "2":
    print("Using multiple independent if-statements.")
    result = None
    if num < 0:
        result = num - 10
    if num == 0:
        result = 0
    if num < 100:
        result = num + 100
    if num < 500:
        result = num + 22
    if num >= 500:
        result = num * 2
    print(f"Result is: {result}")

elif choice == "0":
    print("Exiting...")

else:
    print("Unknown option.")

print("\nProgram ending.")
