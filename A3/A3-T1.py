print("Program starting.")
print("Insert two integers.")

first = int(input("Insert first integer: "))
second = int(input("Insert second integer: "))

print("Comparing inserted integers.")

if first == second:
    print("Integers are the same")
elif first > second:
    print("First integer is greater.")
else:
    print("Second integer is greater.")


print("\nAdding integers together")
total = first + second
print(f"{first} + {second} = {total}")

    
print("\nChecking the parity of the sum...")
if total % 2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")

print("Program ending.")
