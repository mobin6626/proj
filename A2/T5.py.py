print("program starting")
word = input("Insert a closed compound word: ")
rev_word = word[::-1]
leng = len(word)
print(f"The word you inserted is '{word}' and in reverse it is '{rev_word}'")
print(f"the length is {leng}")
print(f"the last word is {word[leng - 1:]}")
print("Take substring from the inserted word by inserting..")
start = int(input("Start point: "))
end = int(input("End point: "))
step = int(input("Step size: "))
subtracted = word[start:end:step]
print(f"The word '{word}' sliced to the defined substring is '{subtracted}'")
print("program ending")