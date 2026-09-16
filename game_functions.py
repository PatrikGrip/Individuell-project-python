from game import GameClass
from storage import save_games, load_games
from utility import wait_for_input, get_valid_choice, clear_screen

# Läser in sparade spel. Om det inte finns några spel skapar den en tom lista.
games_list = load_games()

# Spel lista med premade spel eftersom jag blev trött på att lägga till flera spel varje gång jag starta programmet
#games_list = [
#    GameClass("Minecraft", "2009", ["Sandbox", "Survival", "Adventure"], "10"),
#    GameClass("Apex Legends", "2019", ["Battle-Royale", "Shooter", "FPS"], "7"),
#    GameClass("The Sims 4", "2014", ["Life Simulation", "Sandbox", "Management"], "8"),
#    GameClass("Counter Strike: Global Offensive", "2012", ["Shooter", "FPS", "Tactical"], "9"),
#]



def add_game():
    print("\n"*10)
    clear_screen()
    print("="*30)
    print("LÄGG TILL SPEL")
    print("="*30 + "\n")

    name = input("Vad heter spelet du vill lägga till? ")
    print()
    year = input("Vilket år kom spelet ut? ")
    print()
    genre_input = input("Genre (t.ex. Action, RPG, Äventyr, Shooter): ")

    # Delar upp genre texten till en lista där det finns ett komma så att det går att skriva fler genrer än en.
    # strip tar bort mellanslagen och if g.strip() tar bort tomma element if fall att det är fler än en komma
    genre = [g.strip() for g in genre_input.split(", ") if g.strip()]
    print()
    rating = input("Vilken betyg skulle du ge detta spel? 1 - 10 ")
    
    new_game = GameClass(name, year, genre, rating)
    games_list.append(new_game)
    save_games(games_list)

    print("\n"*10)
    clear_screen()
    print(f"Du har lagt till spelet {name} i din lista.")

    wait_for_input()




def show_game():
    print("\n"*10)
    clear_screen()
    print("="*30)
    print("DINA SPEL")
    print("="*30 + "\n")

    if not games_list:
        print("Du har inga spel i din lista")
        wait_for_input()
        return

    # Varje alternativ är en tuple som är indelad i: Text, sorteringsnyckel och reverse
    sorting_category = [
        ("Namn (A-Ö)", lambda game: game.name, False),
        ("Namn (Ö-A)", lambda game: game.name, True),

        # Behöver använda int annars sparas det som strängar från input och sorterar knasigt 
        ("Årtal. Äldsta först", lambda game: int(game.year), False),
        ("Årtal. Nyast först", lambda game: int(game.year), True),
        ("Betyg. Bäst till sämst", lambda game: int(game.rating), True),
        ("Betyg. Sämst till bäst", lambda game: int(game.rating), False)
    ]

    for index in range(len(sorting_category)):
        print(f"{index + 1}. {sorting_category[index][0]}")
        
    
    choice = get_valid_choice("\nHur vill du visa dina spel? ", len(sorting_category))
    
    if choice is None:
        wait_for_input()
        return

    sorting_option = sorting_category[choice - 1]

    sorting_name, sorting_function, sorting_reverse = sorting_option

    print("\n"*10)
    clear_screen()
    print(f"\nDu valde att sortera med {sorting_name}\n")

    # Skapar en ny lista som är sorterad så att originala listan inte förändras
    sorted_games = sorted(games_list, key=sorting_function, reverse=sorting_reverse)

    for game in sorted_games:
        print(game)

    wait_for_input()





def search_game():
    print("\n"*10)
    clear_screen()
    print("="*30)
    print("SÖK EFTER SPEL")
    print("="*30)

    if not games_list:
        print("Du har inga spel i din lista")
        wait_for_input()
        return

    search_term = input("\nSök efter spel: ")

    results = []

    for game in games_list:

        # Gjorde om allting till lowercase så att sökningen fungerar även om bokstäverna är stora eller små
        # Jag valde att anvnda in så att så länge det matchade någonstans, hittar den rätt.
        if search_term.lower() in game.name.lower():
            results.append(game)

    if not results:
        print("\nInga spel hittades")
    else:
        for game in results:
            print(game)
    
    wait_for_input()




def remove_game():
    print("\n"*10)
    clear_screen()
    print("="*30)
    print("TA BORT SPEL")
    print("="*30)

    for game in range(len(games_list)):
        print(f"{game + 1} {games_list[game]}")

    choice = get_valid_choice("\nTryck på en siffra kopplat till det spelet du vill ta bort. ", len(games_list))

    if choice is None:
        wait_for_input()
        return

    # Valde pop istället för remove eftersom jag ville skriva ut vad som försvann
    removed_game = games_list.pop(choice - 1)
    save_games(games_list)
    print(f"\nSpelet {removed_game.name} har tagits bort från din lista.")
    

    wait_for_input()




def edit_game():
    print("\n"*10)
    clear_screen()
    print("="*30)
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

    if choice is None:
        wait_for_input()
        return

    game_to_edit = games_list[choice - 1]



    # Ännu en tuple som innnehåller: texten som visas, namn på attributen och nuvarande värdet.
    # Eftersom vi inte vet vad användaren ska redigera sparas det till setattr senare
    category_name = [
    ("Namn", "name", game_to_edit.name),
    ("År", "year", game_to_edit.year),

    # eftersom genre är en lista gör jag om den till en sträng här
    ("Genre", "genre", ", ".join(game_to_edit.genre)),
    ("Betyg", "rating", game_to_edit.rating),
    ]

    print("\n"*10)
    clear_screen()
    print(f"\nDu har valt {game_to_edit}\n")
    

    for index in range(len(category_name)):
        print(f"{index + 1}. {category_name[index][0]}: {category_name[index][2]}")

    choice = get_valid_choice("Vad vill du redigera? ", len(category_name))

    if choice is None:
        wait_for_input()
        return

    edit_option = category_name[choice - 1]
    option_label, option_name, current_value = edit_option

    new_value = input("\n"*3 + f"Nuvarande {option_label}: {current_value}\nSkriv ett nytt värde: ")


    # Om användaren bara trycker enter vill vi behålla det gamla värdet istället att skriva en tom sträng
    if not new_value:
        new_value = current_value

    if option_name == "genre":
        # samma kod som i add_game() alltså genre sparas i en lista
        new_value = [g.strip() for g in new_value.split(",")]

    # Ändrar attributen namn som finns i option_name till ett nytt värde som ändras med new_value.
    setattr(game_to_edit, option_name, new_value)
    save_games(games_list)

    wait_for_input()




def quit_program():
    print("\nProgrammet avslutas")
    # Den enda funktionen som return True till huvudmenyn vilket därmed avslutar programmet.
    return True