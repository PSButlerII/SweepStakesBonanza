import random

import userInterface


class Sweepstakes:
    
    def __init__(self, name):
        self.name = ''
        self.contestants = {}

    def register_contestant(self, contestant):
        pass
        # contestant.first_name = userInterface.get_user_input_string("What is Your First Name?")
        # contestant.last_name = userInterface.get_user_input_string("What is Your Last Name?")
        # contestant.full_name = contestant.first_name + '' + contestant.last_name
        # self.contestants.update(contestant.full_name)
        # contestant.email_address = userInterface.get_user_input_string("What is Your Email Address?")

    def pick_winner(self):  # should return a contestant
        return random.choice(list(self.contestants))

    def view_contestants(self):
        # for contestants in self.contestants:
        userInterface.display_message(self.contestants.items())

    def menu(self):
        userInterface.get_user_input_string("please pick a menu item")
        # send_user_menu_message( 1 - view Contestant - )
        # send_user_menu_message( 2 - register new contestant - )
        # send_user_menu_message( 3 - pick winner - )
        # send_user_menu_message( 4 - exit menu - )
