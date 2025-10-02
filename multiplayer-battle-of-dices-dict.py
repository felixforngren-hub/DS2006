from dice import rollD6
import csv
import os
import copy  

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

player_info = {
    "name": "",
    "email": "",
    "country": "",
    "wins": 0,
    "rolls": []
}

players = []
number_of_players = num_players 

# For loop to obtain the player names using deepcopy of the template
for i in range(number_of_players):
    player = copy.deepcopy(player_info)  
    name_in = input(f"What is the name of player {i+1}? ").strip()
    player["name"] = name_in if name_in else f"Player {i+1}"
    player["email"] = input(f"What is the e-mail of player {i+1}? ").strip()
    player["country"] = input(f"What is the country of player {i+1}? ").strip()
    players.append(player)

WIN_TARGET = 3  
rounds_played = 0

rounds = []

def standings_str():
    return " | ".join([f"{p['name']}: {p['wins']}" for p in players])

# Loop 
while max(p["wins"] for p in players) < WIN_TARGET:
    input("\nPress ENTER to roll for all players...")

    rounds_played += 1
    print(f"\n— Round {rounds_played} —")

    rolls = {}
    for p in players:
        r = rollD6()
        rolls[p["name"]] = r
        p["rolls"].append(r) 
        print(f"{p['name']} rolled: {r}")

    # Decide round winner
    top = max(rolls.values())
    names_with_top = [name for name, r in rolls.items() if r == top]

    if len(names_with_top) == 1:
        winner_name = names_with_top[0]
        for p in players:
            if p["name"] == winner_name:
                p["wins"] += 1
                break
        print(f"🏆 {winner_name} wins the round!")
    else:
        winner_name = "Tie"
        print("🤝 It's a tie (multiple top rolls).")

    totals = {p["name"]: p["wins"] for p in players}

    rounds.append({
        "round": rounds_played,
        "rolls": rolls,                         
        "winner": winner_name,
        "totals": totals,                      
        "players_snapshot": copy.deepcopy(players)  
    })

    # Show standings
    print("Score:", standings_str())

    if max(p["wins"] for p in players) < WIN_TARGET:
        input("Press ENTER to continue...")

# Match end 
champion = max(players, key=lambda p: p["wins"])["name"]
print(f"\n🎉 {champion} is the new Battle of Dices Champion! It took {rounds_played} rounds.")

# Quick overview 
names = [p["name"] for p in players]  
print("\nSaved lists:")
print("Rounds:     ", [r["round"] for r in rounds])
print("Winners:    ", [r["winner"] for r in rounds])
print("Totals per round:")
for i, r in enumerate(rounds, start=1):
    totals = r["totals"]
    totals_str = " | ".join([f"{name}={totals[name]}" for name in names])
    print(f"  After round {i}: {totals_str}")

# Round by round summary 
print("\nRound-by-round summary:")
for r in rounds:
    rolls_str = ", ".join([f"{name}={r['rolls'][name]}" for name in names])
    totals_str = " ".join([f"{name}:{r['totals'][name]}" for name in names])
    print(f"Round {r['round']}: {rolls_str} -> {r['winner']} | Score {totals_str}")

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
    names +                          
    ["Winner"] +
    [f"{name}_Total" for name in names] 
)

with open(filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for r in rounds:
        row = (
            [r["round"]] +
            [r["rolls"][name] for name in names] +
            [r["winner"]] +
            [r["totals"][name] for name in names]
        )
        writer.writerow(row)

print(f"✅ Summary saved to '{filename}'")

# Save players.csv (namn, e-post, country) i samma mapp
players_filename = os.path.join(folder if folder else "", "players.csv")
with open(players_filename, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Email", "Country"])
    for p in players:
        writer.writerow([p["name"], p["email"], p["country"]])

print(f"✅ Players saved to '{players_filename}'")