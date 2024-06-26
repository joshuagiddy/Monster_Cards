"""2_Add_Card_v1
We are now adding A add card if statement which allows the user to add a card to the monster cards catalogue.
It isn't very advanced, all it does is asks for the card details but doesn't respond when you have a filled
in the answers."""

import easygui

# Dictionary containing monster cards and their attributes
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

card_details = ""
# Using easygui to get input for new card details
enter_card_details = easygui.multenterbox("Enter card details", "Add Card", ["Card Name", "Strength", "Speed", "Stealth", "Cunning"])

# Check if all input fields are filled and all numeric fields are integers
if enter_card_details is not None and all(enter_card_details[1:]) and all(value.isdigit() for value in enter_card_details[1:]):
    # Creating a dictionary for the new card's details
    card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                    "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
    # Adding the new card to the dictionary
    monster_cards[enter_card_details[0]] = card_details
    easygui.msgbox("Card added successfully!")
else:
    # Error message if input is invalid or incomplete
    easygui.msgbox("Card not added.")




