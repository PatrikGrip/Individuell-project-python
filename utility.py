import os

def wait_for_input():
    input("\nTryck Enter för att fortsätta ")

def get_valid_choice(prompt, max_value):
    user_input = input(prompt)

    if not user_input.isdigit():
        print("Ange ett giltigt nummer")
        return None

    choice = int(user_input)

    if not (1 <= choice <= max_value):
        print("Numret finns inte på listan.")
        return None

    return choice

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")