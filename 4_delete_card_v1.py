"""4_delete_card_v1
This is a function that allows the user to select a monster out of the catalogue and delete it."""
import easygui

# Monster Cards Catalogue
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

# Function to delete a card
def delete_card(card_to_delete):
    # Asking the user which card they would like to delete out of the Monsters Cards Catalogue
    card_to_delete = easygui.buttonbox("Which card would you like to delete?", "Delete Card", list(monster_cards.keys()))
    # Deleting the card
    del monster_cards[card_to_delete]
    easygui.msgbox(f"{card_to_delete} has been deleted", "Delete Card")

delete_card(monster_cards)
