import json
import os

FILE_NAME = "player_stats.json"

def load_stats():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return {"games_played": 0, "wins": 0, "losses": 0}

def save_stats(stats):
    with open(FILE_NAME, "w") as file:
        json.dump(stats, file, indent=4)

def update_stats(won):
    stats = load_stats()
    stats["games_played"] += 1
    if won:
        stats["wins"] += 1
    else:
        stats["losses"] += 1
    save_stats(stats)

# Приклад використання
update_stats(won=True)
print("Оновлена статистика:", load_stats())
