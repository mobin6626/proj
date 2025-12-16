LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(text):
    res = ""
    for c in text:
        if c in LOWER:
            res += LOWER[(LOWER.index(c) + 13) % 26]
        elif c in UPPER:
            res += UPPER[(UPPER.index(c) + 13) % 26]
        else:
            res += c
    return res


def main():
    print("Program starting.")
    print("Collecting plain text rows for ciphering.")

    rows = []
    while True:
        r = input("Insert row (empty stops): ")
        if r == "":
            break
        rows.append(r)

    cipher = [rot13(r) for r in rows]

    print("#### Ciphered-text ####")
    for c in cipher:
        print(c)
    print("#### Ciphered-text ####")

    save = input("Save to file? (y/n): ").lower()
    if save == "y":
        filename = input("Insert filename to save: ")
        with open(filename, "w") as f:
            f.writelines(c + "\n" for c in cipher)
        print("Ciphered text saved!")

    print("Program ending.")

main()
