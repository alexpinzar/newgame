import random

def roll():
    min_value = 1
    max_value = 6
    roll() == random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again")

max_score = 100
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:

    for players_index in range(players):
        print("\nPlayer", players_index + 1 , "turn has just started")
        print("Your total score is :", players_scores[players_index],"\n")
        current_score = 0
        while True:
             should_roll = input("Would you like to roll (y)? ")
             if should_roll.lower() != "e":
                     break
             
        value = roll()
        if value == 1:
            print("you rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
            print("You rolled a:", value)

        print("Your score is:" , current_score)    
     
    players_scores[players_index] += current_score
    print("Your total score is:", players_scores [players_index])

max_score = max(players_scores)
winning_index = players_scores.index(max_score)
print("Player number", winning_index + 1, 
      "is the winneer with a score of:" , max_score)
