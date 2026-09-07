import random

names = [
    # Aapke original names
    "Ragnar", "Thor", "Kratos", "Ezio", 
    
    # Norse aur Gaming / Legendary Names
    "Odin", "Loki", "Freya", "Bjorn", "Ivar", "Floki", "Harald", "Sigurd",
    "Geralt", "Nathan", "Dante", "Vergil", "Leon", "Chris", "Sephiroth",
    "Altair", "Connor", "Arno", "Bayek", "Alexios", "Eivor", "Basim", "Atreus","iron man",
    
    # Historical / Mythological Names
    "Achilles", "Hercules", "Perseus", "Alexander", "Caesar", "Spartacus", 
    "Leonidas", "Hannibal", "Cyrus", "Ramses", "Arthur", "Lancelot", "Merlin",
    
    # Modern / Strong Names
    "Marcus", "Dominic", "Viktor", "Dimitri", "Zane", "Xavier", "Damian", "Gabriel",
    "Lucian", "Malakai", "Rowan", "Silas", "Valentin", "Alistair"
]


stats = {
    "warrior": {
        1: {"HP": (120, 150), "ATK": (15, 20)},
        2: {"HP": (150, 180), "ATK": (20, 25)},
        3: {"HP": (180, 215), "ATK": (25, 31)},
        4: {"HP": (215, 250), "ATK": (31, 37)},
        5: {"HP": (250, 290), "ATK": (37, 44)}
    },

    "mage": {
        1: {"HP": (80, 110), "ATK": (22, 28)},
        2: {"HP": (105, 135), "ATK": (28, 34)},
        3: {"HP": (130, 165), "ATK": (34, 41)},
        4: {"HP": (160, 195), "ATK": (41, 48)},
        5: {"HP": (190, 230), "ATK": (48, 56)}
    },

    "archer": {
        1: {"HP": (100, 125), "ATK": (18, 24)},
        2: {"HP": (125, 150), "ATK": (24, 30)},
        3: {"HP": (150, 180), "ATK": (30, 36)},
        4: {"HP": (180, 215), "ATK": (36, 43)},
        5: {"HP": (215, 255), "ATK": (43, 50)}
    }
}


abilities = {
    "warrior": {
        1: [
            "Heavy_Strike", "Shield_Bash", "Armor_Up", "Taunt", "Battle_Cry",
            "Iron_Will", "Pummel", "Sunder_Armor", "Heroic_Strike", "Hamstring"
        ],
        2: [
            "Ground_Slam", "Blood_Lust", "Berserk_Mode", "Whirlwind", "Cleave",
            "Overpower", "Revenge", "Charge", "Demoralizing_Shout", "Shield_Wall"
        ],
        3: [
            "Colossus_Smash", "Bladestorm", "subsitution jutsu", "Shockwave", "Spell_Reflection",
            "Heroic_Leap", "Intervene", "Rend", "Disarm", "Ignore_Pain"
        ],
        4: [
            "Onslaught", "Rampage", "Execute", "Siegebreaker", "Dragon_Roar",
            "Storm_Bolt", "Bloodthirst", "Raging_Blow", "Chhidori", "Enrage"
        ],
        5: [
            "Titan_Grip", "Asgard_Fury", "Odin_Blessing", "Ragnarok_Slam", "Juggernaut_Charge",
            "God_Slayer", "Warlord_Command", "Immovable_Object", "Rasengan", "Valhalla_Call"
        ]
    },

    "mage": {
        1: [
            "Fireball", "Frostbolt", "Arcane_Missiles", "Mana_Shield", "Counterspell",
            "Blink", "Ignite", "Freeze_Ray", "Arcane_Intellect", "Mana_Regen"
        ],
        2: [
            "Pyroblast", "Ice_Nova", "Cone_of_Cold", "Scorch", "Fire_Blast",
            "Mirror_Image", "Invisibility", "Slow", "Polymorph", "Evocation"
        ],
        3: [
            "Blizzard", "Chain_Lightning", "Meteor_Strike", "Combustion", "Ice_Block",
            "Living_Bomb", "Blast_Wave", "Dragon_Breath", "Frost_Nova", "Arcane_Power"
        ],
        4: [
            "Deep_Freeze", "Time_Warp", "Supernova", "Phoenix_Flames", "Glacial_Spike",
            "Arcane_Orb", "Presence_of_Mind", "Ring_of_Frost", "Alter_Time", "Ice_Barrier"
        ],
        5: [
            "Black_Hole", "Cosmic_Rupture", "Chrono_Shift", "Infernal_Cataclysm", "Absolute_Zero",
            "Arcane_Singularity", "Elemental_Summon", "Mana_Void", "Astral_Alignment", "Supernova_Burst"
        ]
    },

    "archer": {
        1: [
            "Double_Shot", "Piercing_Arrow", "Eagle_Eye", "Evasion", "Poison_Arrow",
            "Explosive_Trap", "Wind_Walk", "Arrow_Rain", "Sniper_Shot", "Crippling_Shot"
        ],
        2: [
            "Multi_Shot", "Steady_Shot", "Aimed_Shot", "Concussive_Shot", "Disengage",
            "Cobra_Shot", "Freezing_Trap", "Aspect_of_the_Cheetah", "Serpent_Sting", "Camouflage"
        ],
        3: [
            "Barbed_Shot", "Chimaera_Shot", "Rapid_Fire", "Arcane_Shot", "Tar_Trap",
            "Kill_Command", "Flanking_Strike", "Binding_Shot", "Aspect_of_the_Turtle", "Misdirection"
        ],
        4: [
            "Black_Arrow", "Lock_and_Load", "Bursting_Shot", "Volley", "Trueshot",
            "Steel_Trap", "Wild_Fire_Bomb", "Harpoon", "Mongoose_Bite", "Butchery"
        ],
        5: [
            "Sky_Splitter", "Shadow_Stitch", "Zephyr_Dash", "Eclipse_Arrow", "Ballista_Strike",
            "Nature_Guise", "Phantom_Barrage", "Hailstorm_Rain", "Sonic_Boom", "Apex_Predator"
        ]
    }
}



class Character:
    
    def __init__(self,chr_class):
        
        chr_class = chr_class.lower() 
        if chr_class in [ "warrior", "mage","archer" ]:
         self.char_class = chr_class  
    
        else:   
            raise ValueError(f"{chr_class} is not a  write class") 
        
     
        self.level = 1
        self.name = random.choice(names)
        self.battles = 0
        
        # for attack and hp 
        character_stats = stats[self.char_class][self.level]
        self.hp = random.randint( character_stats["HP"][0],character_stats["HP"][1])
        self.attack = random.randint( character_stats["ATK"][0],character_stats["ATK"][1])
        # for attack and hp 
        
        # for Skills
        skill_stats = abilities[self.char_class][self.level]
        self.skill = []
        self.skill.append(random.choice(skill_stats))
        # for Skills
    
    
    
    def level_up(self):

     if self.level >= 5:
         return
 
     else:
         self.level += 1
 
         self.battles = 0
 
         new_stats = stats[self.char_class][self.level]
 
         self.hp = random.randint(
             new_stats["HP"][0],
             new_stats["HP"][1]
         )
 
         self.attack = random.randint(
             new_stats["ATK"][0],
             new_stats["ATK"][1]
         )
 
         skill_stats = abilities[self.char_class][self.level]
 
         new_skill = random.choice(skill_stats)
 
         self.skills.append(new_skill)
   
    


        
      
c = Character("warrior")
print("Start - Level:", c.level, "Skills:", c.skill)

for i in range(1,5):
    c.battles = 10
    c.level_up()
    print(f"Level: {c.level} | Skills: {c.skill}")      


# c = Character("mage")
# print("Character name = ",c.name)
# print("Type = ",c.char_class)
# print("HP = ",c.hp)
# print("Attack = ",c.attack)
# print("Skill = ", c.skill) 
# print("Level = ", c.level) 

# print() 
           
# c1 = Character("warrior")
# print("Character name = ",c1.name)
# print("Type = ",c1.char_class)
# print("HP",c1.hp)
# print("Attack = ",c1.attack)
# print("Level = ", c.level) 
# print("Skill = ", c1.skill)             

# c = Character("warrior")
# print("Before level up:")
# print("Level =", c.level)
# print("Skills =", c.skill)
# print("HP =", c.hp)

# c.battles = 10
# c.level_up()

# print("\nAfter level up:")
# print("Level =", c.level)
# print("Skills =", c.skill)
# print("HP =", c.hp)


# c.battles = 10
# c.level_up()

# print("Level =", c.level)
# print("\nAfter level up:")
# print("Level =", c.level)
# print("Skills =", c.skill)
# print("HP =", c.hp)

# c.battles = 10
# c.level_up()
# print("Level =", c.level)
# print("\nAfter level up:")
# print("Level =", c.level)
# print("Skills =", c.skill)
# print("HP =", c.hp)

# c.battles = 10
# c.level_up()
# print("Level =", c.level)
# print("\nAfter level up:")
# print("Level =", c.level)
# print("Skills =", c.skill)
# print("HP =", c.hp)

# c.battles = 10
# c.level_up()
# print("Level =", c.level)
# print("\nAfter level up:")
# print("Level =", c.level)
# print("Skills =", c.skill)
# print("HP =", c.hp)