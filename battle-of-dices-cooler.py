# Battle of Dices is going to be an amazing 2 player game, 
# where two players face each other using only their sheer luck! 
# 
# The rules are:
# 
# Each player throws two dice (of different sizes).
# The player with the highest sum wins the round.  
# The first player to win 3 times is the winner.
#
# Our main task today is to implement the code necessary to bring this
# amazing game alive!

from dice import rollD6, rollD8  

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0
rounds_played = 0

# Repeat rounds until someone reach 3 wins:
while player1_wins < 3 and player2_wins < 3:
    input("\nPress ENTER to roll the dice...")

    # Player 1 rolls two different dice (D6 and D8)
    player1_roll_1 = rollD6()
    player1_roll_2 = rollD8()
    player1_sum = player1_roll_1 + player1_roll_2
    print("Player 1 rolled: " + str(player1_roll_1) + " and " + str(player1_roll_2))
    print("Player 1 total: " + str(player1_sum))

    # Player 2 rolls the same two different dice
    player2_roll_1 = rollD6()
    player2_roll_2 = rollD8()
    player2_sum = player2_roll_1 + player2_roll_2
    print("Player 2 rolled: " + str(player2_roll_1) + " and " + str(player2_roll_2))
    print("Player 2 total: " + str(player2_sum))

    # So far so good right? But how to check who got the highest sum?
    if player1_sum > player2_sum:
        player1_wins += 1
        print("Player 1 wins this round!")
        print("Because ", player1_sum, " is greater than ", player2_sum)
    elif player1_sum == player2_sum:
        print("Amaaazzinng! This round has a tie!")
    else:
        player2_wins = player2_wins + 1
        print("Player 2 wins this round!")
        print("Because ", player2_sum, " is greater than ", player1_sum)

    # Round counting
    rounds_played += 1

    # We can print the game score:
    print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

    # Pause before next round (only if no one has won yet)
    if player1_wins < 3 and player2_wins < 3:
        input("\nPress ENTER to continue...")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
    print("It took ", rounds_played, " rounds.")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
    print("It took ", rounds_played, " rounds.")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")
