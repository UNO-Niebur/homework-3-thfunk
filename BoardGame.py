# Homework 3 - Board Game System
# Name: Taran Funk
# Date: 4/5/2026

import random
import time


def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data

def saveGameData(filename, data):
    """Writes the current game state back to the file."""
    with open(filename, "w") as file:
        for item in data:
            file.write(f"{item}\n")


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    for item in data:
        print(item)

def getCurrentData(data):
    """Extracts the current game state from the data."""
    position = int(data[0].split(':')[0])
    playerHealth = int(data[1].split(':')[0])
    heals = int(data[2].split(':')[0])
    guardHealth = int(data[4].split(':')[0])
    bossHealth = int(data[7].split(':')[0])
    return position, playerHealth, heals, guardHealth, bossHealth 

def movePlayer(data):
    """Example function to simulate moving a player."""
    print("\nMove player function not fully implemented.")
    movement = input("Type 'W', 'A', 'S', or 'D' to move: ").upper()
    return movement

def updateGameState(position, playerHealth, heals, guardHealth, bossHealth, data):
    """Updates the game state based on player movement."""
    data[0] = f"{position}:{data[0].split(':')[1]}"
    data[1] = f"{playerHealth}:{data[1].split(':')[1]}"
    data[2] = f"{heals}:{data[2].split(':')[1]}"
    data[4] = f"{guardHealth}:{data[4].split(':')[1]}"
    data[7] = f"{bossHealth}:{data[7].split(':')[1]}"
    return data     
    


def main():
    filename = "events.txt" 

    gameData = loadGameData(filename)
    displayGame(gameData)
    position, playerHealth, heals, guardHealth, bossHealth = getCurrentData(gameData)
    movement = ""

    while movement != 'Q' and playerHealth > 0 and bossHealth > 0:
        if position == 0:
            print("\nWelcome to the Dungeon Game. At any point, you can type 'Q' to quit.\n")
            print("It's time to test your strength. A guard stands before you. Do you choose to fight or flee?\n")
            movement = input("Type 'F' to fight or 'R' to run: ").upper()
            while movement not in ['F', 'R', 'Q']:
                movement = input("Invalid choice. Please type 'F' to fight or 'R' to run: ").upper()
            if movement == 'F':
                time.sleep(3)
                position = 1
            elif movement == 'R':
                print("\nThe guard blocks your path... and now has the first strike!")
                time.sleep(3)
                attack = random.randint(1, 5)
                playerHealth -= attack
                print(f"The guard attacks you for {attack} damage. Your health is now {playerHealth}.")
                position = 1

        if position == 1:
            print("\nYou are now in battle with the guard. It's your turn to attack.\n")
            print(f"The guard has {guardHealth} health, and you have {playerHealth} health.\n")
            while guardHealth > 0 and playerHealth > 0:
                attack = random.randint(1, 5)
                guardHealth = max(0, guardHealth - attack)
                print(f"You attack the guard for {attack} damage. The guard's health is now {guardHealth}.\n")
                time.sleep(2)
                if guardHealth <= 0:
                    position = 2
                    print("\nYou have defeated the guard! You walk past the guard into town.\n")
                else:
                    attack = random.randint(1, 5)
                    playerHealth = max(0, playerHealth - attack)
                    print(f"The guard attacks you for {attack} damage. Your health is now {playerHealth}.\n")
                    time.sleep(2)
            if guardHealth <= 0:
                position = 2
                print("\nYou have defeated the guard!\n")

        if position == 2:
            print("\n You have entered town. Here you find two health potions which will heal you back to full health\n")
            heals = 2
            time.sleep(3)
            print("\nAhead of you is a heavy iron door, and behind it is the boss. Do you choose to move ahead or heal yourself before entering?\n")
            movement = input("Type 'M' to move ahead or 'H' to heal: ").upper()
            while movement not in ['M', 'H', 'Q']:
                movement = input("Invalid choice. Please type 'M' to move ahead or 'H' to heal: ").upper()
            if movement == 'M':
                print("\nYou chose to move ahead. You open the door and step into the boss's lair.\n")
                position = 3
            elif movement == 'H':
                playerHealth = 15
                heals -= 1
                print("\nYou chose to heal yourself. You drink a health potion and restore your health to full. You have one health potion remaining.\n")
                time.sleep(3)
                print("You open the door and step into the boss's lair.")
                position = 3

        if position == 3:
            print("\nYou are now in battle with the boss. It's your turn to attack.\n")
            print(f"The boss has {bossHealth} health, and you have {playerHealth} health.\n")
            while bossHealth > 0 and playerHealth > 0:
                movement = input("Type 'A' to attack or 'H' to heal: ").upper()
                while movement not in ['A', 'H', 'Q']:
                    movement = input("Invalid choice. Please type 'A' to attack or 'H' to heal: ").upper()
                if movement == 'H':
                    if heals > 0:
                        playerHealth = 15
                        heals -= 1
                        print(f"\nYou chose to heal yourself. You drink a health potion and restore your health to full. You have {heals} health potion remaining.\n")
                        time.sleep(3)
                    else:
                        print("\nYou have no health potions left! You must attack the boss.\n")
                        time.sleep(3)
                if movement == 'A':
                    attack = random.randint(1, 5)
                    bossHealth = max(0, bossHealth - attack)
                    print(f"You attack the boss for {attack} damage. The boss's health is now {bossHealth}.\n")
                    time.sleep(3)
                    if bossHealth <= 0:
                        position = 4
                        print("\nYou have defeated the boss! You are victorious!\n")
                    else:
                        attack = random.randint(1, 8)
                        playerHealth = max(0, playerHealth - attack)
                        print(f"The boss attacks you for {attack} damage. Your health is now {playerHealth}.\n")
                        time.sleep(3)
                if movement == 'Q':
                    break

    if movement == 'Q':
        updateGameState(position, playerHealth, heals, guardHealth, bossHealth, gameData)
        saveGameData(filename, gameData)
        print("\nYou have chose to save and quit the game.")
    if playerHealth <= 0:
        position = 0
        playerHealth = 15
        heals = 0
        guardHealth = 10
        bossHealth = 15
        updateGameState(position, playerHealth, heals, guardHealth, bossHealth, gameData)
        saveGameData(filename, gameData)
        print("\nYou have been defeated. Better luck next time.\nGame over.")
    if bossHealth <= 0:
        position = 4
        print("\nI'll get you next...\n")
        time.sleep(3)
        print("time...\n")
        position = 0
        playerHealth = 15
        heals = 0
        guardHealth = 10
        bossHealth = 15
        updateGameState(position, playerHealth, heals, guardHealth, bossHealth, gameData)
        saveGameData(filename, gameData)
    

    # Player Interration
    #choice = "y"
    #while choice.lower() == "y":
    #    movement = movePlayer(gameData)
    #    gameData = updateGameState(gameData, movement)
    #    displayGame(gameData)
    #    choice = input("\nMove player? (y/n): ")

if __name__ == "__main__":
    main()
