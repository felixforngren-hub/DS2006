# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck!
#
# Rules:
# Each player throws one D6. Highest roll wins the round.
# First to 3 wins is the winner. (Ingen loop – vi upprepar block manuellt)

import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Score trackers
player1_wins = 0
player2_wins = 0

# Save rounds
rounds_data = []

game_over = False

# Round 1
if not game_over:
    ROUND_NUM = 1

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 2
if not game_over:
    ROUND_NUM = 2

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

 # Round 3
if not game_over:
    ROUND_NUM = 3  

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 4
if not game_over:
    ROUND_NUM = 4

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 5
if not game_over:
    ROUND_NUM = 5

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 6
if not game_over:
    ROUND_NUM = 6

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 7
if not game_over:
    ROUND_NUM = 7

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 8
if not game_over:
    ROUND_NUM = 8

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

    # Round 9
if not game_over:
    ROUND_NUM = 9

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 10
if not game_over:
    ROUND_NUM = 10

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 11
if not game_over:
    ROUND_NUM = 11

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 12
if not game_over:
    ROUND_NUM = 12

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 13
if not game_over:
    ROUND_NUM = 13

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 14
if not game_over:
    ROUND_NUM = 14

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battle of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")

# Round 15
if not game_over:
    ROUND_NUM = 15

    input("\nPress ENTER to roll the dice...")

    player1_roll = random.randint(1, 6)  # D6
    print("Player 1 rolled: " + str(player1_roll))

    player2_roll = random.randint(1, 6)  # D6
    print("Player 2 rolled: " + str(player2_roll))

    # Who got the highest roll?
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

    # Print current score
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Save round info
    rounds_data.append({
        "round": ROUND_NUM,
        "p1": player1_roll,
        "p2": player2_roll,
        "winner": round_winner,
        "score_after": (player1_wins, player2_wins)
    })

    # Winner check
    if player1_wins == 3:
        print("Player 1 is the newest Battl2e of Dices Champion! ")
        game_over = True
    elif player2_wins == 3:
        print("Player 2 is the newest Battle of Dices Champion! ")
        game_over = True
    else:
        input("\nPress ENTER to continue...")
    
# Final results
if not game_over:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")

print("\nSaved rounds data:")
print(rounds_data)