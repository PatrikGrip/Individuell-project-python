from game_functions import add_game, show_game, search_game, remove_game, edit_game, quit_program

# Tuple med text och funktion kopplade till texten
category_name = [
    ("Lägg till spel", add_game),
    ("Visa alla spel", show_game),
    ("Sök efter spel", search_game),
    ("Ta bort spel", remove_game),
    ("Redigera ett spel", edit_game),
    ("Avsluta program", quit_program)
]

while True:
    print("""
                                                                  
 ____  _ _   _      _____         _             _     _           
|    \\|_| |_| |_   |   __|___ ___| |___ ___ ___|_|___| |_ ___ ___ 
|  |  | |  _|  _|  |__   | . | -_| |  _| -_| . | |_ -|  _| -_|  _|
|____/|_|_| |_|    |_____|  _|___|_|_| |___|_  |_|___|_| |___|_|  
                         |_|               |___|                  
""")
    # Visa meny
    print("="*66 + "\n")
    for index in range(len(category_name)):
        print(" "*23 + f"{index + 1}. {category_name[index][0]}")
    print("\n" + "="*66)

    user_input = input("\nVälj ett alternativ: ")

    # Kollar om det är ett giltigt nummer
    if not user_input.isdigit():
        print("\nAnge ett giltigt nummer")
        input("Tryck på Enter för att fortsätta")
        continue

    choice = int(user_input)

    # Kollar om valet är mella 1 till så många val man har 
    if not (1 <= choice <= len(category_name)):
        print("\nNumret finns inte på listan")
        input("Tryck på Enter för att fortsätta")
        continue

    # Om användaren väljer en siffra anropas den funktionen 
    text, function = category_name[choice - 1]

    # Om should_quit return som True så kommer programmet avslutas. Den enda som return True är quit_program
    should_quit = function()

    if should_quit:
        break