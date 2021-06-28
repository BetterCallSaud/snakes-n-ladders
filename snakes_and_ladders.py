"""
    @ Author: Saud Hashmi
    @ Date Created: 28.06.2021
    @ Topic: Create a Two-Player Game (MLH INIT 2022)

    Game: Snakes and Ladders

    About: I will use dictionaries to define positions for the start and ends of the snakes and ladders. A total of 7 snakes and 7 ladders shall be used in the 1 to 100 cells (excluding 1 and 100 as they mark the starting and finishing point)

    It will be a 2 player text user interface game.
"""

# Importing randint for random throw of dice
from random import randint

# Dictionary for defined positions for snakes and ladders
# Key: starting pos, Value: ending pos
snakes = {25: 5, 34: 1, 47: 19, 65: 52, 87: 57, 91: 61, 99: 69}
ladders = {3: 51, 6: 27, 20: 60, 36: 55, 38: 48, 63: 95, 68: 98}

# Player class
class Player():
    """Player Class"""
    def __init__(self, name):
        self.pos = 1
        self.name = name

"""Welcome function"""
def welcome() -> None:
    print("\nWELCOME TO SNAKES AND LADDERS")
    print("It's a 2 player game.\nWe will begin with asking your names.\n")

"""Function for checking if a snake is on the current position"""
def isSnakeOnPos(player) -> bool:
    for key in snakes.keys():
        if (player.pos == key): return True
        return False

"""Function for checking if a ladder is on the current position"""
def isLadderOnPos(player) -> bool:
    for key in ladders.keys():
        if (player.pos == key): return True
        return False

"""Function for executing the snake position decrement"""
def snakeEats(player, cond) -> None:
    if (cond):
        player.pos = snakes[player.pos]
        print(f"\nThe snake eats you! You end up at {player.pos}.")

"""Function for executing the ladder position increment"""
def climbLadder(player, cond) -> None:
    if (cond):
        player.pos = ladders[player.pos]
        print(f"\nYou climb up the ladder! You end up at {player.pos}.")

if __name__ == "__main__":
    # Lists for storing Player objects
    players = []

    # Calling the welcome function
    welcome()

    # Prompting player names
    p1 = input("Enter your name Player 1: ")
    p2 = input("Enter your name Player 2: ")

    # Adding p1 and p2 to players
    players.append(Player(p1))
    players.append(Player(p2))

    # playerIndex tells us what player will play; True for P1 and False for P2
    playerIndex = 0

    # Game loop
    while True: 

        player = players[playerIndex]

        # Checking if curr position is not 1 and 100
        if player.pos != 100:
            
            # Turn for players
            print(f"\nIt's your turn, {player.name}!")
            print(f"You are on position {player.pos}.\n")
            input("Press Enter to roll the dice...")
            print("-"*30)

            # Roll of the dice and printing it
            roll = randint(1, 6)
            print("You rolled:", roll)

            # Checking if roll does not go over 100
            if (player.pos + roll <= 100):
                player.pos += roll
            else:
                print("\nYour throw goes over 100. You will get your chance again!")

            isSnake = isSnakeOnPos(player)
            isLadder = isLadderOnPos(player)

            # Calling both snake and ladder action functions. One will only activate if the 'cond' parameter is True
            snakeEats(player, isSnake)
            climbLadder(player, isLadder)

            # Changing player chance
            if (playerIndex == 0): playerIndex = 1
            else: playerIndex = 0

        else:
            # Player won the game
            print(f"\n{player.name} won the game! Congrats...")
            break
