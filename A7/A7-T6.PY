import random
random.seed(1234)

# -----------------------------
# ASCII art for choices
# -----------------------------
ASCII_ART = {
    1: """    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)""",
    2: """     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)""",
    3: """    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""
}

CHOICES = {1: "rock", 2: "paper", 3: "scissors"}

# -----------------------------
# Game results tracker
# -----------------------------
class PlayerStats:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.draws = 0

# -----------------------------
# Determine winner
# -----------------------------
def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "draw"
    elif (player_choice == 1 and bot_choice == 3) or \
         (player_choice == 2 and bot_choice == 1) or \
         (player_choice == 3 and bot_choice == 2):
        return "player"
    else:
        return "bot"

# -----------------------------
# Game loop
# -----------------------------
def main():
    print("Program starting.")
    print("Welcome to the rock-paper-scissors game!")
    
    player_name = input("Insert player name: ").strip()
    print(f"Welcome {player_name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    
    player_stats = PlayerStats(player_name)
    bot_stats = PlayerStats("RPS-3PO")
    
    while True:
        print("Options:")
        print("1 - Rock")
        print("2 - Paper")
        print("3 - Scissors")
        print("0 - Quit game")
        
        try:
            choice = int(input("Your choice: ").strip())
        except ValueError:
            print("Invalid input. Please enter 0, 1, 2, or 3.\n")
            continue
        
        if choice == 0:
            break
        if choice not in [1, 2, 3]:
            print("Invalid option. Please choose 1, 2, 3 or 0.\n")
            continue
        
        bot_choice = random.randint(1, 3)
        
        print("\nRock! Paper! Scissors! Shoot!\n")
        print("#" * 25)
        print(f"{player_name} chose {CHOICES[choice]}.\n")
        print(ASCII_ART[choice])
        print("#" * 25)
        print(f"RPS-3PO chose {CHOICES[bot_choice]}.\n")
        print(ASCII_ART[bot_choice])
        print("#" * 25 + "\n")
        
        winner = determine_winner(choice, bot_choice)
        if winner == "draw":
            print(f"Draw! Both players chose {CHOICES[choice]}.\n")
            player_stats.draws += 1
            bot_stats.draws += 1
        elif winner == "player":
            print(f"{player_name} {CHOICES[choice]} beats RPS-3PO {CHOICES[bot_choice]}.\n")
            player_stats.wins += 1
            bot_stats.losses += 1
        else:
            print(f"RPS-3PO {CHOICES[bot_choice]} beats {player_name} {CHOICES[choice]}.\n")
            bot_stats.wins += 1
            player_stats.losses += 1
    
    # -----------------------------
    # Display final results
    # -----------------------------
    print("\nResults:")
    print(f"{player_stats.name} - wins ({player_stats.wins}), losses ({player_stats.losses}), draws ({player_stats.draws})")
    print(f"{bot_stats.name} - wins ({bot_stats.wins}), losses ({bot_stats.losses}), draws ({bot_stats.draws})")
    print("\nProgram ending.")

# -----------------------------
# Start program
# -----------------------------
main()
