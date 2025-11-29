print("program starting")
name = input("What is your name: ")
num1 = float(input("Enter a float Number: "))
num2 = float(input("Enter another float Number: "))
print(f"OK {name} you gave me {num1} and {num2}")
result = round(num1 * num2, 2)

print(f"multiplying first and second number results in: {result}")
print("program ending")