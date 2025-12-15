def frameword(Pword):
    print("*" + Pword + "*")
    return None

def collectwords():
    words = []
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        words.append(word)
    return words

def main():
    print("Program starting.\n")
    
    words = collectwords()
    for word in words:
        frameword(word)
    
    print("\nProgram-ending.")
    return None

main()
