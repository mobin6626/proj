print("Program starting.")

word = input("Insert Word (Empty Stops): ")
words = 0
characters = 0

while(word != ""):
    words += 1
    characters += len(word)
    word = input("Insert Word (Empty Stops): ")

print(f"{words} Words inserted!")
print(f"{characters} Characters inserted!")  

print("Program ending.")
