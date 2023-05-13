import random

def dice_roll():
    dice = {"4":random.choice(range(1,5)),
            "6":random.choice(range(1,7)),
            "8":random.choice(range(1,9)),
            "10":random.choice(range(1,11)),
            "12":random.choice(range(1,13)),
            "20":random.choice(range(1,21)),}
    
    dice_selection = input("Which dice would you like to use?\n(4, 6, 8, 10, 12, 20): ")
    if dice_selection == "4" or dice_selection == "6" or dice_selection == "8" or dice_selection == "10" or dice_selection == "12" or dice_selection == "20":
        print(f"You rolled: {dice[dice_selection]}")
    else:
        print("Sorry, that is not a dice I am familiar with. Please enter a choice from the options provided.")
        dice_roll()
        
    if dice_selection == "20" and dice["20"] == 1:
        print("Oh no! You rolled a nat 1! Better luck next time!")
    if dice_selection == "20" and dice["20"] == 20:
        print("Oh baby!! That's a nat 20!")
        
    reroll = input("Would you like to reroll?\n(Y or N): ")
    if reroll.upper() == "Y":
        dice_roll()
    if reroll.upper() == "N":
        print("Thanks for rolling and Good luck in your campaign!")
    else:
        print("You collect no points and may god have mercy on your soul!")
        
dice_roll()