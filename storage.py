import json

from game import GameClass

FILENAME = "games.json"

def save_games(games_list):

# Gör om alla klasser till en dict
    data = []

    for game in games_list:
        data.append({
            "name": game.name,
            "year": game.year,
            "genre": game.genre,
            "rating": game.rating
        })

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)