print("Program starting.")
print("\nCheck multiplicative persistence.")

n = input("Insert an integer: ")

# Handle negative
if n[0] == '-':
    n = n[1:]
    print("(Using absolute value)")

count = 0

while len(n) > 1:
    count += 1
    
    # Multiply all digits
    total = 1
    for digit in n:
        total *= int(digit)
    
    # Show the step
    print(" * ".join(n) + " = " + str(total))
    
    # Next number
    n = str(total)

if count > 0:
    print("No more steps.")
    print(f"\nThis program took {count} step(s)")
else:
    print("Already a single digit.")

print("\nProgram ending.")