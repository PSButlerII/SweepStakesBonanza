import random

import contestant
import userInterface
from contestant import Contestant


class Sweepstakes:
    def __init__(self, name):
        self.name = name
        self.contestants = {}


    def register_contestant(self):
        sweepstake_contestant = contestant.Contestant()
        self.contestants.update(sweepstake_contestant)

    def pick_winner(self):  # should return a contestant
        return random.choice(list(self.contestants))
        # notify the winner that they won and all the other contestants that they lost

    def view_contestants(self):
        # for contestants in self.contestants:
        userInterface.display_message(self.contestants.items())
        # this just displays the contestant names in the list

    def sweepstakes_menu(self):

        menu_choice = True
        while menu_choice:
            userInterface.display_message("""
            1.View Contestant
            2.Register New Contestant 
            3.Pick Winner
            4.Exit Menu
            """)
            menu_choice = userInterface.get_user_input_number("Please Enter A number? ")
            if menu_choice == 1:
                self.view_contestants()
            elif menu_choice == 2:
                self.register_contestant()
            elif menu_choice == 3:
                self.pick_winner()
            elif menu_choice == 4:
                userInterface.display_message("\n Exiting Menu")
                break
            else:
                userInterface.get_user_input_number("\n Not Valid Choice Try again")
