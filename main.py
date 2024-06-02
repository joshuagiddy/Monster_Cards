"""Main program for Monster Card Catalogue"""
import easygui as eg

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
    # Card details which will be inputted by user
    card_details = ""
    enter_card_details = eg.multenterbox("Enter card details", "Add Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"])

    # If user cancels input
    if enter_card_details is None:
        eg.msgbox("Card not added", "Add Card")
        return
    # Try statement to deal with invalid input
    try:
        card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                        "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    except ValueError:
        eg.msgbox("Invalid input, Strength, Speed, Stealth and Cunning must be integers. Card not added.",
                  "Add Card")
        add_card()

    # Adding the new card to the dictionary
    monster_cards[enter_card_details[0]] = card_details
    eg.msgbox("Card added successfully!", "Add Card")


def delete_card():
    # Asking the user which card they would like to delete out of the Monsters Cards Catalogue
    card_to_delete = eg.buttonbox("Which card would you like to delete?", "Delete Card", list(monster_cards.keys()))

    # Check if the selected card exists before deleting
    if card_to_delete in monster_cards:
        # Deleting the card
        del monster_cards[card_to_delete]
        eg.msgbox(f"{card_to_delete} has been deleted", "Delete Card")
    else:
        # Display error message if the selected card does not exist
        eg.msgbox(f"Error: Please select a card to delete", "Delete Card")


def view_catalogue():
    card_details_formatted = ""
    # Using for loops to get input for new card details
    for card in monster_cards:
        card_details_formatted += f"{card}:\n"
        # Using for loops to format the card details
        for key, value in monster_cards[card].items():
            card_details_formatted += f"{key}: {value}\n"
        card_details_formatted += "\n"
    # Displaying the card details
    eg.msgbox(card_details_formatted, )


def search_cards():
    try:
        # Main program
        card = eg.choicebox("Select card", "Search Cards", list(monster_cards.keys()))
        if card is None:
            raise ValueError("Operation cancelled.")

        # formatting the card details
        card_details_formatted = ""
        card_details_formatted += f"{card}:\n"
        # Using for loops to format the card details
        for key, value in monster_cards[card].items():
            card_details_formatted += f"{key}: {value}\n"
        # Asking the user if they would like to Edit or Delete the card
        choice = eg.choicebox(card_details_formatted, "Search Cards", ["Delete Card", "Edit Card", "Exit"])
        # If delete card selected, it will run the delete card function
        if choice == "Delete Card":
            delete_card()
        # If the edit card is selected, it will run the edit card function
        elif choice == "Edit Card":
            edit_card(card)
        # Exiting function
        elif choice == "Exit":
            pass
    except ValueError:
        eg.msgbox("Operation cancelled.", "Search Cards")


def edit_card(card_name):
    # This is where the card details will be stored
    card_details = ""
    card_defaults = [card_name]
    # For loop to input the card details
    for stat in list(monster_cards[card_name].keys()):
        card_defaults.append(monster_cards[card_name][stat])
    # Ask user what new card details they want to edit
    enter_card_details = eg.multenterbox("Enter card details", "Edit Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"], card_defaults)
    # Try statement to deal with invalid input
    try:
        card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                        "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    except ValueError:
        eg.msgbox("Invalid input, Strength, Speed, Stealth and Cunning must be integers. Card not added.", "Edit Card")
        add_card()
    # Output the new card details
    monster_cards[enter_card_details[0]] = card_details


def display_card_details(card_name):
    # Displaying the card details
    card_details_formatted = ""
    # Using for loops to format the card details
    card_details_formatted += f"{card_name}:\n"
    for key, value in monster_cards[card_name].items():
        card_details_formatted += f"{key}: {value}\n"
        # Asking if card details are correct
    choice = eg.buttonbox(f"Are these card details correct?\n"
                          f"{card_details_formatted}", "", ["Yes", "No"])
    # if statement to check if card details are correct
    if choice == "Yes":
        pass
    elif choice == "No":
        edit_card(card_name)


# Main Program
def main():
    # Selecting which option the user wants
    while True:
        choice = eg.buttonbox("Welcome to the Monster Cards catalogue\n"
                              "Please select an option:", "Monster Cards Catalogue",
                              ["Add Card", "View Catalogue", "Search cards", "Exit"])
        # Options to select
        if choice == "Add Card":
            add_card()
        elif choice == "View Catalogue":
            view_catalogue()
        elif choice == "Search cards":
            search_cards()
        elif choice == "Exit":
            break


main()
