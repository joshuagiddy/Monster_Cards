"""3_edit_card_v2
This version is now putting it into a function. This is so you can re use the code over and over again.
Still has no error message."""
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
# Edit card function
def edit_card(card_name):
    # This is where the card details will be stored
    card_details = ""
    # Asking the user which card they would like to edit
    card_name = easygui.enterbox("Enter card name: (Out of the Monster Cards Catalogue)", "Edit Card")
    card_defaults = [card_name]
    # Looping through the stats to get the default values
    for stat in list(monster_cards[card_name].keys()):
        card_defaults.append(monster_cards[card_name][stat])
    # Asking the user to enter the card details
    enter_card_details = easygui.multenterbox("Enter card details", "Edit Card",
                                         ["Card Name", "Strength", "Speed", "Stealth", "Cunning"], card_defaults)

    # Storing the answers inputted by the user in the dictionary
    card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                    "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}
# Outputting the results
    monster_cards[enter_card_details[0]] = card_details


edit_card("Stoneling")


