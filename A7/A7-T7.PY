# -----------------------------
# Simple Enigma Demo
# -----------------------------
import string

ALPHABET = string.ascii_uppercase

# -----------------------------
# Read configuration
# -----------------------------
def read_config(filename):
    rotors = []
    reflector = ""
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line.startswith("Rotor1:"):
                rotors.append(line.split(":")[1].strip())
            elif line.startswith("Rotor2:"):
                rotors.append(line.split(":")[1].strip())
            elif line.startswith("Rotor3:"):
                rotors.append(line.split(":")[1].strip())
            elif line.startswith("Reflector:"):
                reflector = line.split(":")[1].strip()
    return rotors, reflector

# -----------------------------
# Rotate rotors
# -----------------------------
def rotate_rotors(positions):
    positions[0] += 1
    if positions[0] >= 26:
        positions[0] = 0
        positions[1] += 1
        if positions[1] >= 26:
            positions[1] = 0
            positions[2] += 1
            if positions[2] >= 26:
                positions[2] = 0

# -----------------------------
# Encode a single character
# -----------------------------
def encode_char(ch, rotors, reflector, positions):
    idx = ALPHABET.index(ch)

    # Forward pass through rotors
    for i in range(3):
        rotor = rotors[i]
        idx = (idx + positions[i]) % 26
        ch = rotor[idx]
        idx = ALPHABET.index(ch)

    # Reflector
    ch = reflector[idx]
    idx = ALPHABET.index(ch)

    # Reverse pass through rotors
    for i in reversed(range(3)):
        rotor = rotors[i]
        idx_in_rotor = rotor.index(ALPHABET[idx])
        idx = (idx_in_rotor - positions[i]) % 26

    return ALPHABET[idx]

# -----------------------------
# Main program
# -----------------------------
def main():
    print("Insert config(filename): ", end="")
    filename = input().strip()
    rotors, reflector = read_config(filename)

    print("Insert plugs (y/n)?: ", end="")
    plugs = input().strip().lower()
    if plugs == "y":
        print("Extra plugs not implemented.")
    else:
        print("No extra plugs inserted.")

    print("Enigma initialized.\n")

    while True:
        print("Insert row (empty stops): ", end="")
        row = input().strip().upper()
        if row == "":
            break

        positions = [0, 0, 0]
        converted = ""

        for ch in row:
            if ch not in ALPHABET:
                converted += ch
                continue
            enc_ch = encode_char(ch, rotors, reflector, positions)
            print(f'Character "{ch}" illuminated as "{enc_ch}"')
            converted += enc_ch
            rotate_rotors(positions)

        print(f"Converted row - \"{converted}\".\n")

    print("Enigma closing.")

# -----------------------------
# Start
# -----------------------------
main()
