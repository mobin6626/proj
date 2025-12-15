word = 0
characters = 0
average = 0

Word = input("Insert a word: ")
while Word != "":
    word += 1
    characters += len(Word)
    average += len(Word)
    Word = input("Insert a Word (Empty Stops) :")

if word != 0:
    average = average / word

print(f"{word} Words")
print(f"{characters} characters")
print(f"{round(average, 2)} Average")