# FOUR EMPERORS JOURNEY - FIXED VERSION
print("Travel starting.")

import os

# ===== 1. CREATE ALL FILES FIRST =====
# Create progress file if it doesn't exist
if not os.path.exists("player_progress.txt"):
    with open("player_progress.txt", "w") as f:
        f.write("current_location;next_location;passphrase\n")
        f.write("0;1;qvfpvcyvar\n")

# Create ALL message files (with their specific passphrases)
message_files = {
    "1_qvfpvcyvar.gkg": """Cneg 0 - Lrne bs gur Sbhe Rzcrebef:

Va NQ 68, nsgre Areb'f qrngu, Ebzr cyhatrq vagb punbf.
Jvgu ab pyrne urve, gur rzcver fnj encvq cbjre fgehttyrf.
Tnyon gbbx gur guebar svefg, sbyybjrq ol Bgub, Ivgryyvhf, naq svanyyl Irfcnfvna,
rnpu onggyvat sbe pbageby va jung orpnzr gur Lrne bs gur Sbhe Rzcrebef.""",
    
    "2_qvfpvcyvar.gkg": """Cneg 1 - Bgub'f Erserfu:

Bgub erherq sbe bayl guerr zbaguf, sebz Wnahnel gb Ncevy 69 NQ.
Ur erag jnexrq ol gur Svefg Onggvpr bs Qrevqnpuhz ntnvafg Ivgryyvhf.
Gubhtu bhagbzovrq, Bgub pubfr fhqvghe bire shegure pvivy jne,
orybatvat uvf qrngu jbhyq fcner Ebzr zber oybqfunq.""",
    
    "3_qvfpvcyvar.gkg": """Cneg 2 - Ivgryyvhf'f Rkprrf:

Ivgryyvhf, xabja sbe tyhggl naq rkentbaane, ernarq rvtug zbaguf.
Ur fcrag yninivtvrq ba onapragrf juvyr gur rzcver fhssrerq.
Uvf qrsrng ol Irfcnfvna'f sbeprf yrnq gb uve ohgny qrngu,
qenttrq guebhtu Ebzr'f fgerrgf ol gur irel pvivragf ur snvyrq.""",
    
    "4_qvfpvcyvar.gkg": """Cneg 3 - Irfcnfvna'f Erfgberagvba:

Irfcnfvna sbhaqrq gur Synivna Qnfal, erfgbingrq fgngvghngvba gb Ebzr.
Ur vafvtugrq pbafgehpgvba bs gur Pybfrfgurz, shaarq ol gur Wrfuvc Gnk.
Uve cevgnoyl ehyr raqrq gur Lrne bs gur Sbhe Rzcrebef,
orpnhfrvat n arj ne bs Ebzne cebcregl gung yrnfrq n qnlyr."""
}

# Create each .gkg file if it doesn't exist
for filename, content in message_files.items():
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            f.write(content)

# ===== 2. READ CURRENT PROGRESS =====
with open("player_progress.txt", "r") as f:
    lines = f.readlines()

# Skip header and get last progress line
if len(lines) < 2:
    current_loc = 0
    next_loc = 1
    passphrase = "qvfpvcyvar"
else:
    # Get the last data line (most recent progress)
    last_line = lines[-1].strip()
    parts = last_line.split(";")
    current_loc = int(parts[0])
    next_loc = int(parts[1])
    passphrase = parts[2]

# ===== 3. SHOW CURRENT LOCATION =====
locations = [
    "home", 
    "Galba's palace", 
    "Otho's palace", 
    "Vitellius' palace", 
    "Vespasian's palace"
]
print(f"Currently at {locations[current_loc]}.")

# ===== 4. CHECK IF COMPLETE =====
if current_loc == 4:
    print("All palaces have been visited!")
    print("Travel ending.")
    exit()

# ===== 5. TRAVEL =====
print(f"Travelling to {locations[next_loc]}...")
print(f"...Arriving to the {locations[next_loc]}.")

# ===== 6. DECODE PASSPHRASE =====
print("Passing the guard at the entrance.")

# ROT13 function
def rot13(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result

plain_passphrase = rot13(passphrase)
print(f'"{plain_passphrase.upper()}!"')

# ===== 7. FIND AND READ MESSAGE =====
print("Looking for the message in the palace...")

# The filename to look for depends on the passphrase in the progress file
msg_filename = f"{next_loc}_{passphrase}.gkg"

try:
    with open(msg_filename, "r") as f:
        encoded_message = f.read()
    
    print("Ah, there it is! Seems cryptic.")
    
except FileNotFoundError:
    print(f"ERROR: Cannot find {msg_filename}")
    print("Available files:")
    for file in os.listdir("."):
        if file.endswith(".gkg"):
            print(f"  - {file}")
    print("Travel ending.")
    exit()

# ===== 8. DECODE MESSAGE =====
plain_message = rot13(encoded_message)
print("[Game] Progress autosaved!")
print("Deciphering Emperor's message...")

# ===== 9. CREATE NEXT PASSPHRASE =====
# Next passphrase is ROT13 of current plain passphrase
next_passphrase = rot13(plain_passphrase.lower())

# ===== 10. SAVE PROGRESS =====
next_next_loc = next_loc + 1 if next_loc < 4 else 4
with open("player_progress.txt", "a") as f:
    f.write(f"{next_loc};{next_next_loc};{next_passphrase}\n")

# ===== 11. SAVE PLAIN MESSAGE =====
plain_filename = f"{next_loc}-{plain_passphrase}.txt"
with open(plain_filename, "w") as f:
    f.write(plain_message)

print("Looks like I've got now the plain version copy of the Emperor's message.")

# Show first line
first_line = plain_message.split('\n')[0]
print(f'Message: "{first_line}"')

print("Time to leave...")
print("Travel ending.")