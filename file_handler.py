import json


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



from character import Character
if __name__ == "__main__":
    c = Character("mage")

    print("Character name = ", c.name)
    print("Type = ", c.char_class)
    print("HP = ", c.hp)
    print("Attack = ", c.attack)
    print("Skills = ", c.skills)
    print("Level = ", c.level)
    
    save_character(c)





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


if __name__ == "__main__":
    loaded = load_character()

    print(loaded.name)
    print(loaded.char_class)
    print(loaded.level)
    print(loaded.hp)
    print(loaded.attack)
    print(loaded.battles)
    print(loaded.skills)    