import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of player(2-5): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=5:
            break
        else:
            print("Enter a correct Number!!")
    else:
        print("INVALID! Enter Again")

max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score : 

    for player_idx in range(players) :
        print("\nPlayer number ", player_idx + 1, " turn has just started!!")
        print( " Your Total score is : ", player_score[player_idx], "\n")
        curren_score = 0
        
        while True :
            should_roll = input("Would you like to roll (y/n) ? ")
            if should_roll.lower() != 'y' :
                break
            
            value = roll()
            
            if value == 1:
                print("You got a '1' ! Your Turn is Done !")
                curren_score = 0
                break
            
            else :
                curren_score += value
                print("You rolled a : ", value, "\n")
            print("Your Score is : ", curren_score)
            
        player_score[player_idx] += curren_score
        print("Your Total Score is : ", player_score[player_idx])
        
max_score = max(player_score)
winig_inx = player_score.index(max_score)

print("Player NUmber ", winig_inx + 1, " is the Winner of the game!!!!!")