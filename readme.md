# ⚔️ RPG Character Battle System

A Python-based RPG game where you create characters, battle enemies, level up, and unlock new skills.

---

## 🚦 Project Status

| Feature | Status |
|---|---|
| Character Creation | Completed |
| Stats System (Random + Level-based) |  Completed |
| Skills System | ❌ Not Started |
| Level Up System | ❌ Not Started |
| Battle System | ❌ Not Started |
| Challenge Mode | ❌ Not Started |
| Multiple Characters | ❌ Not Started |
| Save / Load System (JSON) | ❌ Not Started |
| Main Menu | ❌ Not Started |

---

## 📁 Project Structure

```
rpg_game/
├── character.py      # Character class, Stats, Skills
├── battle.py         # Battle logic, Enemy generation
├── file_handler.py   # Save / Load JSON
├── main.py           # Main menu — connects everything
└── README.md         # This file
```

---

## 🎮 Features

### 1. Character Creation
- Player provides: **Name** and **Class**
- All other stats are **randomly generated** based on class + level range
- Same class can produce weak or strong characters — every character is unique

### 2. Classes (3 Total)
| Class | Play Style |
|---|---|
| ⚔️ Warrior | High HP, moderate attack — tank type |
| 🧙 Mage | Lower HP, high attack — glass cannon |
| 🏹 Archer | Balanced — medium HP and attack |

### 3. Stats System
- Stats are **randomly rolled** within a level-based range
- Higher level = higher range = stronger character
- Stats: **HP, Attack** (more may be added later)

| Level | HP Range | Attack Range |
|---|---|---|
| 1 | 80 – 120 | 10 – 20 |
| 2 | 130 – 180 | 21 – 35 |
| 3 | 190 – 250 | 36 – 55 |
| 4 | 260 – 330 | 56 – 80 |
| 5 | 340 – 420 | 81 – 110 |

### 4. Level Up System
- **10 battles completed = 1 Level Up**
- Max level: **5**
- On level up:
  - Stats **re-roll** from new higher range
  - **New skill unlocked**

### 5. Skills System
Each class has 5 skills — one unlocked per level:

| Level | ⚔️ Warrior | 🧙 Mage | 🏹 Archer |
|---|---|---|---|
| 1 | Basic Strike | Magic Bolt | Quick Shot |
| 2 | Shield Bash | Fire Ball | Double Arrow |
| 3 | War Cry | Ice Storm | Eagle Eye |
| 4 | Berserker | Thunder Strike | Poison Arrow |
| 5 | Titan Smash | Void Blast | Death Shot |

### 6. Battle System
- Player **selects their character** to fight
- **Default mode:** Enemy is same class + same level (fair fight)
- **Challenge mode:** Player can choose to fight a higher level enemy (more risk, more reward)
- Enemy stats are randomly generated just like player characters

### 7. Multiple Characters
- Player can **manually create and save multiple characters**
- Before each battle, player selects which character to use

### 8. Save / Load System
- All character data saved in **JSON format**
- Player can quit and continue later — progress is not lost

---

## 🔧 How to Run

```bash
# Make sure you are inside the project folder
cd rpg_game

# Run the game
python main.py
```

---

## 📌 Notes
- Project is being built step by step
- Features will be marked ✅ as they are completed
- Structure or features may be updated as development continues