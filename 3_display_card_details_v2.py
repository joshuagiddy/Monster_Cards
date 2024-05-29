"""3_display_card_details_v2
This is now allowing the user to ask if they want to edit the card and to check if the card details are correct."""


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
def card_details():
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
    print(card_details_formatted)



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


def display_card_details(card_name):
    # Displaying the card details
    card_details_formatted = ""
    # Using for loops to format the card details
    card_details_formatted += f"{card_name}:\n"
    for key, value in monster_cards[card_name].items():
        card_details_formatted += f"{key}: {value}\n"
        # Asking if card details are correct
    choice = easygui.buttonbox(f"Are these card details correct?\n"
                          f"{card_details_formatted}", "", ["Yes", "No"])
    if choice == "Yes":
        pass
    elif choice == "No":
        display_card_details(card_name)

def main():
    while True:
        choice = easygui.buttonbox("Welcome to the Monster Cards catalogue\n"
                              "Please select an option:", "Monster Cards",
                              ["Add Card", "View Catalogue", "Exit"])
        if choice == "Add Card":
            add_card()
        elif choice == "View Catalogue":
            card_details()
        elif choice == "Exit":
            break

main()
