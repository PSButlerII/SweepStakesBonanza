import sweepStakes
from sweepStakes import Sweepstakes
import userInterface


class MarketingFirm:

    sweepstakes_storage = []

    def __init__(self):
        self.name = "marketing_firm_name"



    def create_sweepstakes(self):
        sweepStakes.name = userInterface.get_user_input_string("What is the Name of the Sweepstake?")
        sweepStakes.contestants = {}  # maybe just pre populate a list of sweepstakes sweep 1, sweep2, ect
        self.sweepstakes_storage.append(sweepStakes)
        MarketingFirm.marketing_firm_menu(self)


    def change_marketing_firm_name(self):
        self.name = userInterface.get_user_input_string("What is the Name of the Marketing Firm")
        return userInterface.display_marketing_firm_menu(self)

    def select_sweepstakes(self):
        userInterface.get_user_input_number(f"{len(self.sweepstakes_storage)}. {self.sweepstakes_storage}.  Select a sweepstake number")
        userInterface.display_sweepstakes_selection_menu()

    def marketing_firm_menu(self):
        menu_choice = True
        while menu_choice:
            userInterface.display_message("""
            1.create sweepstakes
            2.change marketing firm name
            3.select sweepstakes
            4.exit menu
            """)
            menu_choice = userInterface.get_user_input_number("Please Enter A number? ")
            if menu_choice == 1:
                self.create_sweepstakes()
            elif menu_choice == 2:
                self.change_marketing_firm_name()
            elif menu_choice == 3:
                self.select_sweepstakes()
            elif menu_choice == 4:
                userInterface.display_message("\n Exiting Menu")
                break
            else:
                userInterface.get_user_input_number("\n Not Valid Choice Try again")


