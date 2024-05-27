"""2_Add_Card_v2
We are now updating it to a function which allows the user to add a card to the monster cards catalogue.
It will continue using the try statement."""

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


# Function to add card
def add_card():
    # Card details which will be inputted by user
    card_details = ""
    enter_card_details = easygui.multenterbox("Enter card details", "Add Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"])
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

add_card()