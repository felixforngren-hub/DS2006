from dice import rollD6  
import csv
import os

print("🎲 Welcome to Battle of Dices! (multiplayer) 🎲")

# Input: number of players 
while True:
    try:
        num_players = int(input("How many players? (at least 2): ").strip())
        if num_players >= 2:
            break
        print("You must enter at least 2 players.")
    except ValueError:
        print("Please enter a whole number, e.g., 2, 3, 4...")

# Input: Choose nicknames 
players = []
for i in range(1, num_players + 1):
    name = input(f"Enter nickname for player {i}: ").strip()
    if not name:
        name = f"Player {i}"
    players.append({"name": name, "wins": 0})

WIN_TARGET = 3  # first to 3 wins

rounds_played = 0

round_numbers = []          
round_rolls = []            
winners = []                
totals_history = []         

def standings_str():
    return " | ".join([f"{p['name']}: {p['wins']}" for p in players])

# Loop 
while max(p["wins"] for p in players) < WIN_TARGET:
    input("\nPress ENTER to roll for all players...")

    rounds_played += 1
    rolls_this_round = []

    print(f"\n— Round {rounds_played} —")
    for p in players:
        r = rollD6()
        rolls_this_round.append(r)
        print(f"{p['name']} rolled: {r}")

    # Decide round winner
    top = max(rolls_this_round)
    idx_with_top = [i for i, r in enumerate(rolls_this_round) if r == top]

    if len(idx_with_top) == 1:
        winner_idx = idx_with_top[0]
        players[winner_idx]["wins"] += 1
        round_winner = players[winner_idx]["name"]
        print(f"🏆 {round_winner} wins the round!")
    else:
        round_winner = "Tie"
        print("🤝 It's a tie (multiple top rolls).")

    # Save logs
    round_numbers.append(rounds_played)
    round_rolls.append(list(rolls_this_round))
    winners.append(round_winner)
    totals_history.append([p["wins"] for p in players])

    # Show standings
    print("Score:", standings_str())

    if max(p["wins"] for p in players) < WIN_TARGET:
        input("Press ENTER to continue...")

# Match end 
champion = max(players, key=lambda p: p["wins"])["name"]
print(f"\n🎉 {champion} is the new Battle of Dices Champion! It took {rounds_played} rounds.")

# Quick overview 
print("\nSaved lists:")
print("Rounds:     ", round_numbers)
print("Winners:    ", winners)
print("Totals per round:")
for i, totals in enumerate(totals_history, start=1):
    totals_str = " | ".join([f"{players[j]['name']}={totals[j]}" for j in range(num_players)])
    print(f"  After round {i}: {totals_str}")

# Round by round summary 
print("\nRound-by-round summary:")
for i in range(len(round_numbers)):
    rolls_str = ", ".join([f"{players[j]['name']}={round_rolls[i][j]}" for j in range(num_players)])
    totals_str = " ".join([f"{players[j]['name']}:{totals_history[i][j]}" for j in range(num_players)])
    print(f"Round {round_numbers[i]}: {rolls_str} -> {winners[i]} | Score {totals_str}")

# Save CSV 
filename = input("\nEnter a filename to save the summary (e.g. results.csv): ").strip()
if not filename:
    filename = "battle_summary.csv"
elif "." not in filename:
    filename += ".csv"

folder = os.path.dirname(filename)
if folder:
    os.makedirs(folder, exist_ok=True)

header = (
    ["Round"] +
    [p["name"] for p in players] +           
    ["Winner"] +
    [f"{p['name']}_Total" for p in players]  
)

with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(round_numbers)):
        row = (
            [round_numbers[i]] +
            round_rolls[i] +
            [winners[i]] +
            totals_history[i]
        )
        writer.writerow(row)

print(f"✅ Summary saved to '{filename}'")

