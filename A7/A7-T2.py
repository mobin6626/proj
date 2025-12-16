print("Program starting.")

# Read input
user_input = input("Insert comma separated integers: ")

# Split values
raw_values = user_input.split(",")

valid_integers: list[int] = []
invalid_values = []

# Parse and validate each value
for value in raw_values:
    trimmed = value.strip()
    try:
        number = int(trimmed)
        valid_integers.append(number)
    except ValueError:
        invalid_values.append(trimmed)

# Report invalid values (if any)
for invalid in invalid_values:
    print(f"Error: '{invalid}' is not a valid integer.")

# If no valid integers remain
if not valid_integers:
    print("No valid integers to analyse.")
    print("Program ending.")
    exit()

# Calculate sum and even/odd
total_sum = sum(valid_integers)
parity = "even" if total_sum % 2 == 0 else "odd"

# Output results
print(f"There are {len(valid_integers)} integers in the list.")
print(f"Sum of the integers is {total_sum} and it's {parity}")

print("Program ending.")
