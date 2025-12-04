# Program: String comparison

print("Program starting...")
print("String comparison")

# Step 1: Get a word from user
word = input("Insert a word: ")

# Step 2: Get a character from user
char = input("Insert a character: ")

# Step 3: Check if character exists in word
if char in word:
    print(f"Word '{word}' contains character '{char}'")
else:
    print(f"Word '{word}' does not contain character '{char}'")

# Step 4: Make second word by inserting the character
word2 = word + char
print(f"The second word: '{word2}'")

# Step 5: Compare words alphabetically
if word < word2:
    print(f"The first word '{word}' is before the second word '{word2}' alphabetically.")
elif word > word2:
    print(f"The second word '{word2}' is before the first word '{word}' alphabetically.")
else:
    print(f"Both inserted words are the same alphabetically.")

print("Program ending.")
