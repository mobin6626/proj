def collatz(n):
    steps = 0
    sequence = [n]

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)
        steps += 1

    return sequence, steps


print("Program starting.")
n = int(input("Insert a positive integer: "))

sequence, steps = collatz(n)

# Print sequence in required format
print(" -> ".join(str(num) for num in sequence))
print(f"Sequence had {steps} total steps.\n")
print("Program ending.")
