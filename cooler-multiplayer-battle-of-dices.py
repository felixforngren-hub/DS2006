# Battle of Dices cooler multiplayer

import csv
import os

try:
    from dice import rollD6, rollD8
except ImportError:
    from dice import rollD6
    import random
    def rollD8():
        return random.randint(1, 8)

print("🎲 Welcome to Battle of Dices! (multiplayer: D6 + D8) 🎲")

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

WIN_TARGET = 3  

rounds_played = 0

round_numbers = []           
round_d6 = []                
round_d8 = []                
round_totals = []            
winners = []                 
totals_history = []          

def standings_str():
    return " | ".join([f"{p['name']}: {p['wins']}" for p in players])

# Loop
while max(p["wins"] for p in players) < WIN_TARGET:
    input("\nPress ENTER to roll for all players...")

    rounds_played += 1
    d6_this_round = []
    d8_this_round = []
    totals_this_round = []

    print(f"\n— Round {rounds_played} —")
    for p in players:
        d6 = rollD6()
        d8 = rollD8()
        total = d6 + d8

        d6_this_round.append(d6)
        d8_this_round.append(d8)
        totals_this_round.append(total)

        print(f"{p['name']} rolled: D6={d6}, D8={d8} (total {total})")

    top_total = max(totals_this_round)
    idx_with_top = [i for i, t in enumerate(totals_this_round) if t == top_total]

    if len(idx_with_top) == 1:
        winner_idx = idx_with_top[0]
        players[winner_idx]["wins"] += 1
        round_winner = players[winner_idx]["name"]
        print(f"🏆 {round_winner} wins the round!")
    else:
        round_winner = "Tie"
        print("🤝 It's a tie (multiple top totals).")

    round_numbers.append(rounds_played)
    round_d6.append(d6_this_round)
    round_d8.append(d8_this_round)
    round_totals.append(totals_this_round)
    winners.append(round_winner)
    totals_history.append([p["wins"] for p in players])

    # Show standings
    print("Score (wins):", standings_str())

    if max(p["wins"] for p in players) < WIN_TARGET:
        input("Press ENTER to continue...")

# Match end 
champion = max(players, key=lambda p: p["wins"])["name"]
print(f"\n🎉 {champion} is the new Battle of Dices Champion! It took {rounds_played} rounds.")

# Quick overview 
print("\nSaved lists:")
print("Rounds:     ", round_numbers)
print("Winners:    ", winners)
print("Wins per round (running totals):")
for i, totals in enumerate(totals_history, start=1):
    totals_str = " | ".join([f"{players[j]['name']}={totals[j]}" for j in range(num_players)])
    print(f"  After round {i}: {totals_str}")

# Round by round summary 
print("\nRound-by-round summary:")
for i in range(len(round_numbers)):
    per_player_str = ", ".join(
        f"{players[j]['name']}: D6={round_d6[i][j]}, D8={round_d8[i][j]} (total {round_totals[i][j]})"
        for j in range(num_players)
    )
    totals_str = " ".join([f"{players[j]['name']}:{totals_history[i][j]}" for j in range(num_players)])
    print(f"Round {round_numbers[i]}: {per_player_str} -> {winners[i]} | Wins {totals_str}")

# Save CSV 
filename = input("\nEnter a filename to save the summary (e.g. results.csv): ").strip()
if not filename:
    filename = "battle_summary.csv"
elif "." not in filename:
    filename += ".csv"

folder = os.path.dirname(filename)
if folder:
    os.makedirs(folder, exist_ok=True)

header = ["Round"]
for p in players:
    header += [f"{p['name']}_D6", f"{p['name']}_D8", f"{p['name']}_Total"]
header += ["Winner"]
header += [f"{p['name']}_Wins" for p in players]

with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(len(round_numbers)):
        row = [round_numbers[i]]
        for j in range(num_players):
            row += [round_d6[i][j], round_d8[i][j], round_totals[i][j]]
        row += [winners[i]]
        row += totals_history[i]
        writer.writerow(row)

print(f"✅ Summary saved to '{filename}'")