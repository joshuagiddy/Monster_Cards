"""View_catalogue_V3
Now we are adding a function, so we can convert it to the main program."""
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
    easygui.msgbox(card_details_formatted,)

view_catalogue()