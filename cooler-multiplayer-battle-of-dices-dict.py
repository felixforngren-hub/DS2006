# Battle of Dices cooler multiplayer 

import csv
import os
import copy  

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

player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []  
}

players = []
for i in range(1, num_players + 1):
    p = copy.deepcopy(player_info)
    name_in = input(f"Enter nickname for player {i}: ").strip()
    p["name"] = name_in if name_in else f"Player {i}"
    p["email"] = input(f"Enter email for {p['name']} (optional): ").strip()
    p["country"] = input(f"Enter country for {p['name']} (optional): ").strip()
    players.append(p)

WIN_TARGET = 3
rounds_played = 0

# One dict per round
rounds = []

def standings_str():
    return " | ".join([f"{p['name']}: {p['wins']}" for p in players])

# Game loop
while max(p["wins"] for p in players) < WIN_TARGET:
    input("\nPress ENTER to roll for all players...")

    rounds_played += 1
    print(f"\n— Round {rounds_played} —")

    rolls = {}
    totals_this_round = []

    for p in players:
        d6 = rollD6()
        d8 = rollD8()
        total = d6 + d8

        rolls[p["name"]] = {"d6": d6, "d8": d8, "total": total}
        totals_this_round.append(total)

        p["rolls"].append({"d6": d6, "d8": d8, "total": total})

        print(f"{p['name']} rolled: D6={d6}, D8={d8} (total {total})")

    # Decide round winner
    top_total = max(totals_this_round)
    names_with_top = [name for name, r in rolls.items() if r["total"] == top_total]

    if len(names_with_top) == 1:
        winner_name = names_with_top[0]
        for p in players:
            if p["name"] == winner_name:
                p["wins"] += 1
                break
        print(f"🏆 {winner_name} wins the round!")
    else:
        winner_name = "Tie"
        print("🤝 It's a tie (multiple top totals).")

    # Running wins totals after this round
    wins_totals = {p["name"]: p["wins"] for p in players}

    rounds.append({
        "round": rounds_played,
        "rolls": rolls,
        "winner": winner_name,
        "wins_totals": wins_totals,
        "players_snapshot": copy.deepcopy(players)
    })

    # Show standings
    print("Score (wins):", standings_str())

    if max(p["wins"] for p in players) < WIN_TARGET:
        input("Press ENTER to continue...")

# Match end 
champion = max(players, key=lambda p: p["wins"])["name"]
print(f"\n🎉 {champion} is the new Battle of Dices Champion! It took {rounds_played} rounds.")

names = [p["name"] for p in players]

print("\nSaved lists:")
print("Rounds:     ", [r["round"] for r in rounds])
print("Winners:    ", [r["winner"] for r in rounds])
print("Wins per round (running totals):")
for i, r in enumerate(rounds, start=1):
    totals = r["wins_totals"]
    totals_str = " | ".join([f"{name}={totals[name]}" for name in names])
    print(f"  After round {i}: {totals_str}")

print("\nRound-by-round summary:")
for r in rounds:
    per_player_str = ", ".join(
        f"{name}: D6={r['rolls'][name]['d6']}, D8={r['rolls'][name]['d8']} (total {r['rolls'][name]['total']})"
        for name in names
    )
    totals_str = " ".join([f"{name}:{r['wins_totals'][name]}" for name in names])
    print(f"Round {r['round']}: {per_player_str} -> {r['winner']} | Wins {totals_str}")

# Save summary CSV 
filename = input("\nEnter a filename to save the summary (e.g. results.csv): ").strip()
if not filename:
    filename = "battle_summary.csv"
elif "." not in filename:
    filename += ".csv"

folder = os.path.dirname(filename)
if folder:
    os.makedirs(folder, exist_ok=True)

header = ["Round"]
for name in names:
    header += [f"{name}_D6", f"{name}_D8", f"{name}_Total"]
header += ["Winner"]
header += [f"{name}_Wins" for name in names]

with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rounds:
        row = [r["round"]]
        for name in names:
            row += [r["rolls"][name]["d6"], r["rolls"][name]["d8"], r["rolls"][name]["total"]]
        row += [r["winner"]]
        row += [r["wins_totals"][name] for name in names]
        writer.writerow(row)

print(f"✅ Summary saved to '{filename}'")

#Save players.csv (Name, Email, Country) in same folder
players_filename = os.path.join(folder if folder else "", "players.csv")
with open(players_filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Country"])
    for p in players:
        writer.writerow([p["name"], p["email"], p["country"]])

print(f"✅ Players saved to '{players_filename}'")