import random

import contestant
import userInterface
from contestant import Contestant


class Sweepstakes:

    def __init__(self):
        self.name = ''
        self.contestants = {}

    def register_contestant(self, contestants):
        contestants = Contestant()

    def pick_winner(self):  # should return a contestant
        return random.choice(list(self.contestants))

    def view_contestants(self):
        # for contestants in self.contestants:
        userInterface.display_message(self.contestants.items())

    def menu(self):
        menu_choice = True
        while menu_choice:
            userInterface.display_message("""
            1.view Contestant
            2.register new contestant 
            3.pick winner
            4.exit menu
            """
                                          )
            menu_choice = userInterface.get_user_input_number("What would you like to do? ")
            if menu_choice == "1":
                self.view_contestants()
            elif menu_choice == "2":
                self.register_contestant(contestant)
            elif menu_choice == "3":
                self.pick_winner()
            elif menu_choice == "4":
                userInterface.display_message("\n Exiting Menu")
                break
            else:
                userInterface.get_user_input_number("\n Not Valid Choice Try again")
