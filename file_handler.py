import json

from character import Character


def save_character(character):
    character_data = {
        "name": character.name,
        "char_class": character.char_class,
        "level": character.level,
        "hp": character.hp,
        "attack": character.attack,
        "battles": character.battles,
        "skills": character.skills
    }

    with open("character.json", "w") as file:
        json.dump(character_data, file, indent=4)


def load_character():
    with open("character.json", "r") as file:
        character_data = json.load(file)

    character = Character(character_data["char_class"])

    character.name = character_data["name"]
    character.level = character_data["level"]
    character.hp = character_data["hp"]
    character.attack = character_data["attack"]
    character.battles = character_data["battles"]
    character.skills = character_data["skills"]

    return character