"""5_edit_card_v1
This version is now allowing the user to edit the card details. It asks the user which monster card it would like to edit
and it now allows the user to edit the card details. Does not save any card details or anything."""
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


card_name = easygui.enterbox("Enter card name", "Edit Card")


card_details = ""
card_defaults = [card_name]
for stat in list(monster_cards[card_name].keys()):
    card_defaults.append(monster_cards[card_name][stat])

enter_card_details = easygui.multenterbox("Enter card details", "Edit Card",
                                     ["Card Name", "Strength", "Speed", "Stealth", "Cunning"], card_defaults)

card_details = {"Strength": int(enter_card_details[1]), "Speed": int(enter_card_details[2]),
                "Stealth": int(enter_card_details[3]), "Cunning": int(enter_card_details[4])}

monster_cards[enter_card_details[0]] = card_details


