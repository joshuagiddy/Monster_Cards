"""5_Search_Cards_v4
This version is now allowing an error message when cancelling the program."""
import easygui

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
# Function for edit card
def edit_card(card_name):
    card_details = ""
    card_defaults = [card_name]
    for stat in list(monster_cards[card_name].keys()):
        card_defaults.append(monster_cards[card_name][stat])
    enter_card_details = easygui.multenterbox("Enter card details: : (Out of the Monster Cards Catalogue)", "Edit Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"], card_defaults)

    # Assuming valid input for simplicity, no try-except block
    card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                    "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}

    monster_cards[enter_card_details[0]] = card_details
# Function to delete card
def delete_card(card_to_delete):
    # Asking the user which card they would like to delete out of the Monsters Cards Catalogue
    card_to_delete = easygui.buttonbox("Confirming, Which card would you like to delete?", "Delete Card", list(monster_cards.keys()))
    # Deleting the card
    del monster_cards[card_to_delete]
    easygui.msgbox(f"{card_to_delete} has been deleted", "Delete Card")

# Function for card details
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
    easygui.msgbox(card_details_formatted, )
    print(card_details_formatted)

# Search Card Function
import easygui


def search_cards():
    try:
        # Main program
        card = easygui.choicebox("Select card", "Search Cards", list(monster_cards.keys()))
        if card is None:
            raise ValueError("Operation cancelled.")

        # formatting the card details
        card_details_formatted = ""
        card_details_formatted += f"{card}:\n"
        # Using for loops to format the card details
        for key, value in monster_cards[card].items():
            card_details_formatted += f"{key}: {value}\n"
        # Asking the user if they would like to Edit or Delete the card
        choice = easygui.choicebox(card_details_formatted, "Search Cards", ["Delete Card", "Edit Card", "Exit"])
        # If delete card selected, it will run the delete card function
        if choice == "Delete Card":
            delete_card(card)
        # If the edit card is selected, it will run the edit card function
        elif choice == "Edit Card":
            edit_card(card)
        # Exiting function
        elif choice == "Exit":
            pass
    except ValueError:
        easygui.msgbox("Operation cancelled.", "Search Cards")




search_cards()
