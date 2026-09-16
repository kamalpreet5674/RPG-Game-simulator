
from character import Character
from file_handler import save_character, load_character
import os


# ===== START SCREEN =====

print("===== RPG GAME =====")
print("1. Continue")
print("2. New Game")

start = int(input("Choose: "))


# ===== CONTINUE =====

if start == 1:

    if os.path.exists("character.json"):
        character = load_character()
        print("Character loaded successfully.")

    else:
        print("No saved character found.")
        print("Please start a New Game.")


# ===== NEW GAME =====

elif start == 2:

    print("Choose your class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")

    choice = input("Choose: ")

    if choice == "1":
        character = Character("warrior")

    elif choice == "2":
        character = Character("mage")

    elif choice == "3":
        character = Character("archer")

    else:
        raise ValueError("Invalid class choice")


else:
    raise ValueError("Invalid start choice")


# ===== MAIN MENU =====

while True:

    print("\n===== RPG GAME =====")
    print("1. Character info")
    print("2. Battle")
    print("3. Save")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":

        print(f"Character name: {character.name}")
        print(f"Character class: {character.char_class}")
        print(f"Level: {character.level}")
        print(f"HP: {character.hp}")
        print(f"Attack: {character.attack}")
        print(f"Skills: {character.skills}")

    elif choice == "2":
        pass

    elif choice == "3":

        save_character(character)
        print("The character has been saved successfully.")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
