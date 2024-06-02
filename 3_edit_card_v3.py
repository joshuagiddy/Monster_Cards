"""3_edit_card_v3
This version is now adding a try statement which allows the user for invalid error when inputting the card details.
If the user inputs a letter in a question that requires an interger, it will reset with an error message."""
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
# Add card function
def add_card():
    # Card details which will be inputted by user
    card_details = ""
    enter_card_details = easygui.multenterbox("Enter card details", "Add Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"])

    # If user cancels input
    if enter_card_details is None:
        easygui.msgbox("Card not added", "Add Card")
        return
    # Try statement to deal with invalid input
    try:
        card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                        "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    except ValueError:
        easygui.msgbox("Invalid input, Strength, Speed, Stealth and Cunning must be integers. Card not added.",
                       "Add Card")
        add_card()

    # Adding the new card to the dictionary
    monster_cards[enter_card_details[0]] = card_details
    easygui.msgbox("Card added successfully!", "Add Card")
# Edit card function
def edit_card(card_name):
    # This is where the card details will be stored
    card_details = ""
    card_defaults = [card_name]
    # For loop to input the card details
    for stat in list(monster_cards[card_name].keys()):
        card_defaults.append(monster_cards[card_name][stat])
    # Ask user what new card details they want to edit
    enter_card_details = easygui.multenterbox("Enter card details", "Edit Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"], card_defaults)
# Try statement to deal with invalid input
    try:
        card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                        "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    except ValueError:
        easygui.msgbox("Invalid input, Strength, Speed, Stealth and Cunning must be integers. Card not added.","Edit Card")
        add_card()
# Output the new card details
    monster_cards[enter_card_details[0]] = card_details
    easygui.msgbox("Card edited successfully!", "Edit Card")


edit_card("Stoneling")

