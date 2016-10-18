import math
import random
import collections

unsortedplayer = (("Name", ""),
          ("Health", 100),
          ("Alive" , True),
          ("XP", 0),
          ("XP to Level Up", 12),
          ("Level", 1),
          ("Attack Points", 5 + random.randint(1,10)))

player = collections.OrderedDict(unsortedplayer)


#def player_gen(player):
  #  player["Name"] = name
   # player["Health"] = 100
    #player["Alive"] = True
   # player["XP"] = 0
    #player["XP to Level Up"] = 12
   # player["Level"] = 1
    #player["Attack Points"] = 5 + random.randint(1,10)
    #return
# This function is called once at the start of the game and assigns semi-random points to each variable. Feel free to change the points to create a better game balance when we get there, they are basically arbitrary.
# The player's name is taken for the scoreboard, but should default to player if left blank

def player_update(playerchoice, enemychoice, xp = 0):
	player["Health"] -= playerchoice
	player["Health"] += enemychoice
	if player["Health"] <= 0:
		player["Alive"] = False
	if player["XP"] >= player["XP tp Level Up"]:
		level_up()
	return
# This function should be called when the players temporary stats need to be updated, such as when in combat or using a healing item
# There should be no change in values when parameters are not entered

def level_up():
	hp = player["Level"] + random.randint(0, player["Level"])
	player["Health"] += hp
	player["Attack Points"] += player["Level"] + random.randint(0, (math.floor(player["Level"]/2)))
	player["Level"] = player["Level"] + 1
	player["XP"] = player["XP to Level Up"] - player["XP"]
	player["XP to Level Up"] = player["Level"] + player["XP to Level Up"] + 12
	return

def main():
    player["Name"] = input("What is your name: ").capitalize()
    print("Welcome to the game,", player["Name"])
    print("----------------------------------------------------------------")
    print("                         HOW TO PLAY")
    print("----------------------------------------------------------------")
    print("")
    print("Fight against the computer in an battle using a range of atacks")
    print("Different types of attack will do various ammounts of damage")
    print("You can also choose to skip the attack and heal")
    print("After each sucessful attack you will gain attack points and EXP")
    print("These points will help you level up")
    print("Any move you make can miss, so choose wisely!")
    print("----------------------------------------------------------------")
    print("")
    for key, value in player.items():
        print(key + ":", value)

    again = True

    # Set up the play again loop
    while again:

    
        winner = None
        player["Health"] = 100
        enemyhealth = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            turn_player = True
            turn_enemy = False
            print("You will go first.")
        else:
            turn_player = False
            turn_enemy = True
            print("Your enemy will go first.")
        print("Your health: ", player["Health"])
        print("Enemy health: ", enemyhealth)

        #main game loop
        while player["Health"] != 0 or enemyhealth != 0):
            heal = False
            miss = False
        moves = {"Punch": random.random.randint(15,25),
                 "Kick": random.randint(12,35),
                 "Karate Chop": random.randint(10,30),
                 "Heal": random.randint(20,30)}
        if turn_player:
            print("You can: ")
            print("1. Punch (15-25 damage)")
            print("2. Kick (12-35 damage)")
            print("3. Karate Chop (10-30)")
            print("4. Heal (Heal by 20-30")
            playerchoice = input("Select a move: ").lower()
            chance_of_miss = random.randint(1,5) # 1 in 5 chance player misses

            if chance_of_miss == 1:
                miss = True
            else:
                miss = False

            if miss:
                playerchoice = 0 # player misses and deals no damage
                print("You missed!")
            else:
                if playerchoice in ("1", "punch"):
                    playerchoice = moves["Punch"]
                    print("You used Punch. Damage:", playerchoice)
                elif playerchoice in ("2", "kick"):
                    playerchoice = moves["Kick"]
                    print("You used kick. Damage:", playerchoice)
                elif playerchoice in ("3", "karate chop"):
                    playerchoice = moves["Karate Chop"]
                    print("You karate chopped your enemy. Ouch! Damage: ", playerchoice)
                elif playerchoice in ("4", "heal"):
                    heal = True # heal activated
                    playerchoice = moves["Heal"]
                else:
                    print("\nThat is not a valid move. Please try again.")
                    continue
        else: #enemy turn
            move_miss = random.randint(1,5)
            if move_miss == 1:
                miss = True
            else:
                miss = False
                
            if miss:
                    enemychoice = 0 # the computer misses and deals no damage
                    print("The computer missed!")
            else:
                if enemyhealth
                
            
main()
