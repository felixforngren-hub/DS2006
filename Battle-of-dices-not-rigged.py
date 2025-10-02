# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck!
#
# Rules:
# - Each player throws one D6.
# - The player with the highest roll wins the round.
# - First to 3 wins is the winner.

from dice import rollD6  

print("🎲 Welcome to Battle of Dices! 🎲")

player1_wins = 0
player2_wins = 0
rounds_played = 0  

# List of round
round_numbers = []   
p1_rolls = []        
p2_rolls = []        
winners = []         
p1_totals = []       
p2_totals = []       

# Loop until someone wins
while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")

    player1_roll = rollD6()
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = rollD6()
    print("Player 2 rolled: " + str(player2_roll))

    # Winner of the round
    if player1_roll > player2_roll:
        player1_wins += 1
        round_winner = "Player 1"
        print("Player 1 wins this round!")
        print("Because ", player1_roll, " is greater than ", player2_roll)
    elif player1_roll == player2_roll:
        round_winner = "Tie"
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins += 1
        round_winner = "Player 2"
        print("Player 2 wins this round!")
        print("Because ", player2_roll, " is greater than ", player1_roll)

    rounds_played += 1
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save every round
    round_numbers.append(rounds_played)
    p1_rolls.append(player1_roll)
    p2_rolls.append(player2_roll)
    winners.append(round_winner)
    p1_totals.append(player1_wins)
    p2_totals.append(player2_wins)

    # Pause if we dont have a winner
    if player1_wins < 3 and player2_wins < 3:
        input("\nPress ENTER to continue...")

# Finish results
if player1_wins == 3:
    print(f"Player 1 is the newest Battle of Dices Champion! It took {rounds_played} rounds.")
else:
    print(f"Player 2 is the newest Battle of Dices Champion! It took {rounds_played} rounds.")

# Show saved list
print("\nSaved lists:")
print("Rounds:     ", round_numbers)
print("P1 rolls:   ", p1_rolls)
print("P2 rolls:   ", p2_rolls)
print("Winners:    ", winners)
print("P1 totals:  ", p1_totals)
print("P2 totals:  ", p2_totals)

# Road of summary
print("\nRound-by-round summary:")
for i in range(len(round_numbers)):
    print(f"Round {round_numbers[i]}: P1={p1_rolls[i]}, P2={p2_rolls[i]} -> {winners[i]} | Score {p1_totals[i]}-{p2_totals[i]}")

# Save summary to file 
import os

filename = input("\nEnter a filename to save the summary (e.g. results.csv): ").strip()
if not filename:
    filename = "battle_summary.csv"
elif "." not in filename:
    filename += ".csv"

folder = os.path.dirname(filename)
if folder:
    os.makedirs(folder, exist_ok=True)

with open(filename, "w", encoding="utf-8") as f:
    f.write("Round,P1,P2,Winner,P1_Total,P2_Total\n")
    for i in range(len(round_numbers)):
        f.write(f"{round_numbers[i]},{p1_rolls[i]},{p2_rolls[i]},{winners[i]},{p1_totals[i]},{p2_totals[i]}\n")

print(f"✅ Summary saved to '{filename}'")
