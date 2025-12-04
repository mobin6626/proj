print("Program starting...")

name = input("Enter your name: ")

print("\nMenu:\nWelcome - 1\nExit - 0")
choice = input("Your choice: ")

if choice == "1":
    print(f"Welcome, {name}!")
elif choice == "0":
    print("Goodbye!")
else:
    print("Unknown option.")

print("Program ending...")
