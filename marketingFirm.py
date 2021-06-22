import sweepStakes
import userInterface


class MarketingFirm:
    def __init__(self, name):
        self.name = ''
        self.sweepstakes_storage = []

    @staticmethod
    def create_sweepstakes():
        sweepStakes.name = userInterface.get_user_input_string("What is the Name of the Sweepstake?")
        sweepStakes.contestants = {}

    def change_marketing_firm_name(self):
        self.name = userInterface.get_user_input_string("What is the Name of the Marketing Firm")

    def select_sweepstakes(self):
        pass
# send_user_menu_message(self.sweepstakes_storage)
# userInterface.get_user_input_string("Select a contestant ")
    # or
    def menu(self):
        pass
# send_user_menu_message( 1 - create_sweepstakes() - )
# send_user_menu_message( 2 - change_marketing_firm_name() - )
# send_user_menu_message( 3 - select_sweepstakes() - )
# send_user_menu_message( 4 - exit_menu() - )
