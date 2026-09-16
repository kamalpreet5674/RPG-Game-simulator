class Entity:
    def __init__(self, name, level, hp, attack, skills):
        self.name = name
        self.level = level
        self.hp = hp
        self.attack = attack
        self.skills = skills




class Character(Entity):
    ...        