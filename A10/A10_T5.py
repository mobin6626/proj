def factorial(n):
    """Recursive factorial calculation."""
    if n < 0:
        return "Undefined for negative numbers"
    return 1 if n <= 1 else n * factorial(n - 1)

def main():
    while True:
        try:
            num = input("Enter a non-negative integer (or 'q' to quit): ")
            if num.lower() == 'q':
                break
            
            n = int(num)
            if n < 0:
                print("Factorial is not defined for negative numbers.")
                continue
                
            result = factorial(n)
            print(f"{n}! = {result}")
            
        except ValueError:
            print("Please enter a valid integer.")
        except RecursionError:
            print("Number too large for recursion depth.")

main()