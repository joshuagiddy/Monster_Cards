import easygui as eg

TITLE = "Monster Cards Catalogue"

monster_cards = {
    "Stoneling": {"Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
    "Vexscream": {"Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
    "Dawnmirage": {"Strength": 5, "Speed": 15, "Stealth": 18, "Cunning": 22},
    "Blazegolem": {"Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
    "Websnake": {"Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
    "Moldvine": {"Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
    "Vortexwing": {"Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
    "Rotthing": {"Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
    "Froststep": {"Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
    "Wispghoul": {"Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2},
}


def add_card():
    card_details = ""
    enter_card_details = eg.multenterbox("Enter card details", TITLE,
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"])
    try:
        card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                        "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    except ValueError:
        eg.msgbox("Invalid input, Strength, Speed, Stealth and Cunning must be integers. Card not added.", TITLE)
        add_card()

    monster_cards[enter_card_details[0]] = card_details

    display_card_details(enter_card_details[0])


def delete_card(card_to_delete):
    del monster_cards[card_to_delete]
    eg.msgbox(f"{card_to_delete} has been deleted", TITLE)


def view_catalogue():
    card_details_formatted = ""
    for card in monster_cards:
        card_details_formatted += f"{card}:\n"
        for key, value in monster_cards[card].items():
            card_details_formatted += f"{key}: {value}\n"
        card_details_formatted += "\n"
    eg.msgbox(card_details_formatted, TITLE)
    eg.msgbox(card_details_formatted)


def search_cards():
    card = eg.choicebox("Select card", TITLE, list(monster_cards.keys()))
    card_details_formatted = ""
    card_details_formatted += f"{card}:\n"
    for key, value in monster_cards[card].items():
        card_details_formatted += f"{key}: {value}\n"
    choice = eg.choicebox(card_details_formatted, TITLE, ["Delete Card", "Edit Card", "Exit"])
    if choice == "Delete Card":
        delete_card(card)
    elif choice == "Edit Card":
        edit_card(card)
    elif choice == "Exit":
        pass


def edit_card(card_name):
    card_details = ""
    card_defaults = [card_name]
    for stat in list(monster_cards[card_name].keys()):
        card_defaults.append(monster_cards[card_name][stat])
    enter_card_details = eg.multenterbox("Enter card details", TITLE,
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"], card_defaults)

    try:
        card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                        "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    except ValueError:
        eg.msgbox("Invalid input, Strength, Speed, Stealth and Cunning must be integers. Card not added.", TITLE)
        add_card()

    monster_cards[enter_card_details[0]] = card_details
    display_card_details(enter_card_details[0])


def display_card_details(card_name):
    card_details_formatted = ""
    card_details_formatted += f"{card_name}:\n"
    for key, value in monster_cards[card_name].items():
        card_details_formatted += f"{key}: {value}\n"
    choice = eg.buttonbox(f"Are these card details correct?\n"
                          f"{card_details_formatted}", TITLE, ["Yes", "No"])
    if choice == "Yes":
        pass
    elif choice == "No":
        edit_card(card_name)


def main():
    while True:
        choice = eg.buttonbox("Welcome to the Monster Cards catalogue\n"
                              "Please select an option:", TITLE,
                              ["Add Card", "View Catalogue", "Search cards", "Exit"])
        if choice == "Add Card":
            add_card()
        elif choice == "View Catalogue":
            view_catalogue()
        elif choice == "Search cards":
            search_cards()
        elif choice == "Exit":
            break


main()