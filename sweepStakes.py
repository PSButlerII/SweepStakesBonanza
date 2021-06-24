import random

import contestant
import userInterface
from contestant import Contestant


class Sweepstakes:
    contestants = {}

    def __init__(self, name):
        self.name = name

    @staticmethod
    def register_contestant():
        contestant.Contestant()
        Sweepstakes.contestants.update()

    @staticmethod
    def pick_winner():  # should return a contestant
        return random.choice(list(Sweepstakes.contestants))
        # notify the winner that they won and all the other contestants that they lost

    def view_contestants(self):
        for contestant.Contestant in Sweepstakes.contestants:
            userInterface.display_message(contestant.Contestant)
        # this just displays the contestant names in the list

    def sweepstakes_menu(self):

        menu_choice = True
        while menu_choice:
            userInterface.display_message("""
            1.View Contestant
            2.Register New Contestant 
            3.Pick Winner
            4.Exit Menu
            """
                                          )
            menu_choice = userInterface.get_user_input_number("Please Enter A number? ")
            if menu_choice == 1:
                Sweepstakes.view_contestants(self)
            elif menu_choice == 2:
                Sweepstakes.register_contestant()
            elif menu_choice == 3:
                Sweepstakes.pick_winner()
            elif menu_choice == 4:
                userInterface.display_message("\n Exiting Menu")
                break
            else:
                userInterface.get_user_input_number("\n Not Valid Choice Try again")
