from game import GameClass
#from storage import (
#    save_games,
#    load_games
#)

from utility import wait_for_input, get_valid_choice

#games_list = load_games()

# Spel lista med premade spel eftersom jag blev trött på att lägga till flera spel varje gång jag starta programmet
games_list = [
    GameClass("Minecraft", "2009", ["Sandbox", "Survival", "Adventure"], "10"),
    GameClass("Apex Legends", "2019", ["Battle-Royale", "Shooter", "FPS"], "7"),
    GameClass("The Sims 4", "2014", ["Life Simulation", "Sandbox", "Management"], "8"),
    GameClass("Counter Strike: Global Offensive", "2012", ["Shooter", "FPS", "Tactical"], "9"),
]



def add_game():
    print("\n"*10 + "="*30)
    print("LÄGG TILL SPEL")
    print("="*30 + "\n")

    name = input("Vad heter spelet du vill lägga till? ")
    print()
    year = input("Vilket år kom spelet ut? ")
    print()
    genre_input = input("Genre (t.ex. Action, RPG, Äventyr, Shooter): ")
    genre = [g.strip() for g in genre_input.split(", ") if g.strip()]
    print()
    rating = input("Vilken betyg skulle du ge detta spel? 1 - 10 ")
    
    # Skapar ett game objekt
    new_game = GameClass(name, year, genre, rating)
    games_list.append(new_game)

    print(("\n"*30) + f"Du har lagt till spelet {name} i din lista.")

    wait_for_input()




def show_game():
    print("\n"*10 + "="*30)
    print("DINA SPEL")
    print("="*30 + "\n")

    if not games_list:
        print("Du har inga spel i din lista")
        wait_for_input()
        return

    # Tuplen är indelad i: Namn, sorteringsfunktion, reversed true eller false.
    sorting_category = [
        ("Namn (A-Ö)", lambda game: game.name, False),
        ("Namn (Ö-A)", lambda game: game.name, True),
        ("Årtal. Äldsta först", lambda game: int(game.year), False),
        ("Årtal. Nyast först", lambda game: int(game.year), True),
        ("Betyg. Bäst till sämst", lambda game: int(game.rating), True),
        ("Betyg. Sämst till bäst", lambda game: int(game.rating), False)
    ]

    for index in range(len(sorting_category)):
        print(f"{index + 1}. {sorting_category[index][0]}")
        
    
    choice = get_valid_choice("\nHur vill du visa dina spel? ", len(sorting_category))
    
    if choice == None:
        wait_for_input()
        return

    sorting_option = sorting_category[choice - 1]

    sorting_name, sorting_function, sorting_reverse = sorting_option

    print(f"Du valde att sortera med {sorting_name}")
    sorted_games = sorted(games_list, key=sorting_function, reverse=sorting_reverse)

    for game in sorted_games:
        print(game)

    wait_for_input()





# fixa sök på genre, spel som innehåller den bokstaven, 
def search_game():
    print("Här kan du söka på dina spel")
    wait_for_input()




def remove_game():
    for game in range(len(games_list)):
        print(f"{game + 1} {games_list[game]}")

    choice = get_valid_choice("\nTryck på en siffra kopplat till det spelet du vill ta bort. ", len(games_list))

    if choice == None:
        wait_for_input()
        return

    removed_game = games_list.pop(choice - 1)
    print(f"\nSpelet {removed_game.name} har tagits bort från din lista.")
    

    wait_for_input()




def edit_game():
    print("\n"*10 + "="*30)
    print("REDIGERA SPEL")
    print("="*30 + "\n")

    if not games_list:
        print("Du har inga spel i din lista")
        wait_for_input()
        return
    else:
        for game in range(len(games_list)):
            print(f"{game + 1} {games_list[game]}")

    choice = get_valid_choice("\nVilket spel vill du redigera? ", len(games_list))

    if choice == None:
        wait_for_input()
        return

    game_to_edit = games_list[choice - 1]



    category_name = [
    ("Namn", "name", game_to_edit.name),
    ("År", "year", game_to_edit.year),
    ("Genre", "genre", ", ".join(game_to_edit.genre)),
    ("Betyg", "rating", game_to_edit.rating),
    ]

    print(f"\nDu har valt {game_to_edit}")
    

    for index in range(len(category_name)):
        print(f"{index + 1}. {category_name[index][0]}: {category_name[index][2]}")

    choice = get_valid_choice("Vad vill du redigera? ", len(category_name))

    if choice == None:
        wait_for_input()
        return

    edit_option = category_name[choice - 1]

    # en till tuple unpacking
    option_label, option_name, current_value = edit_option

    new_value = input(f"Nuvarande {option_label}: {current_value}\nSkriv ett nytt värde: ")

    if option_name == "genre":
        new_value = [g.strip() for g in new_value.split(",")]

    setattr(game_to_edit, option_name, new_value)

    wait_for_input()




def quit_program():
    print("\nProgrammet avslutas")
    return True