# Course: CS 30
# Period: 1
# Date Created: 20/10/23
# Date Last Modified: 20/10/28
# Name: Subanaya Thirunavukkarasu
# Description: Final project for CS 30

# imports
from characters import Character, Inventory
import maps

print("It's 2080. Welcome to The City, a place so polluted")
print("that fog covers everything, and oxygen tanks are required\n\n")
print("Objective: Escape The City\n")
print("Explore the map and defeat the enemy of any location")
print("to escape The City.\n")
print("To begin, choose a character\n")


# character descriptions
character_one = Character('Evelyn', 'ambitious', 'strength', 100)
print(character_one.__str__())

character_two = Character('Avery', 'funny', 'speed', 100)
print(character_two.__str__())


# this list will be used later in the Function
# user_action_3. The character chosen will affect the
# outcome of the user's choices when fighting enemies
chosen_character = []


# this list will be user later in the function
# user_action_3. The items in the inventory will affect
# the user's choices when fighting enemies
character_inventory = []


# prompt for user to choose a character
prompt_1 = "Your character: "


def user_action_1(character):
    """user chooses a character to play,
    character's inventory is printed"""
    choice = f"{character}"
    return choice.title()

while True:
    response = input(prompt_1)
    if response.lower() == "avery":
        avery_inventory = Inventory(
            'Avery', 'Glowstick', 'Bubble Gum',
            'Releases posion when it breaks through skin', '30', '0',
            'Hubba bubba bubble gum- a healing item', '0', '25'
            )
        print(avery_inventory.__str__())
        chosen_character.append('avery')
        character_hp = 100

    elif response.lower() == "evelyn":
        evelyn_inventory = Inventory(
            'Evelyn', 'Dagger', 'Rotten Apple',
            'An old but sharp dagger', '40', '0',
            'A commonly found health item', '0', '10'
            )
        print(evelyn_inventory.__str__())
        chosen_character.append('evelyn')
        character_hp = 100

    else:
        print("That response is not valid. Please type in a valid response")
    break


# print out the location maps
maps.print_map(maps.main_map)

# Locations
locations = ['City Tower', 'Shopping Centre', 'Sewer']


# Prompt for user to choose a location
print("Locations:")
for location in locations:
    print(location.title())

prompt_2 = "Choose a location: "


def user_action_2(location):
    """user chooses a location to play the game in"""
    choice = f"{location}"
    return choice.title()

while True:
    response = input(prompt_2)
    if response.lower() == "sewer":
        print("\nWelcome to the Sewer")

    elif response.lower() == "shopping centre":
        print("\nWelcome to the Shopping Centre")

    elif response.lower() == "city tower":
        print("Welcome to the City Tower")

    else:
        print("That response is not valid. Please type in a valid response")
    break


# Actions

# The state of the oxygen tank will affect the
# user when they want to attack the enemy
# The state of the oxygen will be affected if
# the player chooses to explore
oxygen_tank = 100

# The enemy's hap will go down if the player attacks it
# The enemy will be defeated when it's hp is 0
enemy_hp = 100

# The actions that the user can choose from
actions = [
    'Explore the Supplies Room', 'Fill up Oxygen Tank', 'Attack the Enemy'
    ]

# Prompt for user to choose an action
prompt_3 = "\nComplete one of the following actions:\n"
for action in actions:
    prompt_3 += f"\n{action}"
prompt_3 += "\n\n"


def user_action_3(action):
    """user chooses an action in their location"""
    choice = f"{action}"
    return choice.title()

while True:
    response = input(prompt_3)

    if response.lower() == 'explore the supplies room':
        print("\nYou found a mysterious blue potion.")
        potion = input("Do you drink it? yes/no? ")
        if potion.lower() == 'yes':
            print("\nYou drank the potion. You feel... stronger")
            character_inventory.append('potion')
        elif potion.lower() == 'no':
            print("\nYou chose not to drink the potion")
        elif potion.lower() == 'quit':
            break
    oxygen_tank = 50

    if response.lower() == 'fill up oxygen tank':
        if oxygen_tank == 100:
            print("\nYour Oxygen Tank is already full")
        elif oxygen_tank < 100:
            print("\nYour Oxygen Tank has been filled.")
            oxygen_tank = 100

    elif response.lower() == 'attack the enemy':

        if 'potion' not in character_inventory:
            print("\nYou are too weak to fight the enemy...")
            print("You need to find something to make you stronger.")

        elif 'potion' in character_inventory:
            if oxygen_tank == 100:
                print("\nYou are ready to fight the enemy. ")
            first_attack_prompt = "\nDo you attack the enemy"
            first_attack_prompt += " sneakily or with force? "
            first_attack = input(first_attack_prompt)

            if first_attack.lower() == 'sneakily':
                if 'avery' in chosen_character:
                    print("\nYour attack was successful. ")
                    print("The enemy's hp went from 100 to  50")
                    enemy_hp = 50
                elif 'evelyn' in chosen_character:
                    print("\nYour attack was unsuccessful. ")
                    print("The enemy's hp remains at 100")
                    enemy_hp = 100
            elif first_attack.lower() == 'with force':
                if 'avery' in chosen_character:
                    print("\nYour attack was unsuccessful. ")
                    print("The enemy's hp remains at 100")
                    enemy_hp = 100
                elif 'evelyn' in chosen_character:
                    print("\nYour attack was successful. ")
                    print("The enemy's hp went from 100 to 50")
                    enemy_hp = 50

            elif first_attack.lower() == 'quit':
                break

            first_defence_prompt = "\nThe enemy reponds quickly. "
            first_defence_prompt += " It attacks you with it's sword. "
            first_defence_prompt += " Do you attack back or dodge? "
            first_defence = input(first_defence_prompt)

            if first_defence.lower() == 'attack':
                print("\nYou atacked the enemy back. ")
                print("Unfortunately, that was the wrong choice, ")
                print("the enemy damges you for 100 hp.")
                character_hp = 0
                print("\nThe enemy defeated you. ")
                print("Maybe try again with a different strategy.")
                break
            elif first_defence.lower() == 'dodge':
                if oxygen_tank == 100:
                    print("\nYou dodged the enemy's attack!")
                    print("No hp points were lost")
                elif oxygen_tank == 50:
                    print("\nYou are too out of breath to dodge. ")
                    print("The enemy damages you for 100 hp.")
                    character_hp = 0
                    print("\nThe enemy defeated you. ")
                    print("Maybe try again with a different strategy.")
                    break

            elif first_defence.lower() == 'quit':
                break

            second_attack_prompt = "\nWill you be ruthless or merciful "
            second_attack_prompt = "for your second attack? "
            second_attack = input(second_attack_prompt)

            if second_attack.lower() == 'ruthless':
                if enemy_hp == 100:
                    print("\nThe enemy's hp decreased by 50")
                    print("The enemy is strong enough to attack you back. ")
                    print("He attacks you for 100 hp.")
                    character_hp = 0
                    print("\nThe enemy defeated you. ")
                    print("Maybe try again with a different strategy.")
                    break
                if enemy_hp == 50:
                    print("\nThe enemy's hp decreases by 50")
                    enemy_hp = 0

            elif second_attack.lower() == 'merciful':
                print("\nYou chose to show some mercy ")
                print("while attacking the enemy. ")
                print("However, the enemy takes advantage of your mercy and ")
                print("attacks you for 100 hp")
                character_hp = 0
                print("\nThe enemy defeated you. ")
                print("Maybe try again with a different strategy.")
                break

            elif second_attack.lower() == 'quit':
                break

            if enemy_hp == 0:
                print("\nCongratulations! You defeated the enemy, ")
                print("thus defeating the game.")
                break

    elif response.lower() == 'quit':
        break
