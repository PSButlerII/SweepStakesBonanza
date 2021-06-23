import sweepStakes
import userInterface


class MarketingFirm:
    def __init__(self, name):
        self.name = ''
        self.sweepstakes_storage = []

    @staticmethod
    def create_sweepstakes():
        sweepStakes.name = userInterface.get_user_input_string("What is the Name of the Sweepstake?")
        sweepStakes.contestants = {}  # maybe just pre populate a list of sweepstakes sweep 1, sweep2, ect

    def change_marketing_firm_name(self):
        self.name = userInterface.get_user_input_string("What is the Name of the Marketing Firm")

    def select_sweepstakes(self):
        pass

    # send_user_menu_message(self.sweepstakes_storage)
    # userInterface.get_user_input_string("Select a sweepstake")
    # or

    def menu(self):
        menu_choice = True
        while menu_choice:
            userInterface.display_message("""
            1.create sweepstakes
            2.change marketing firm name
            3.select sweepstakes
            4.exit menu
            """
                                          )
            menu_choice = userInterface.get_user_input_number("Please Enter A number? ")
            if menu_choice == "1":
                self.create_sweepstakes()
            elif menu_choice == "2":
                self.change_marketing_firm_name()
            elif menu_choice == "3":
                self.select_sweepstakes()
            elif menu_choice == "4":
                userInterface.display_message("\n Exiting Menu")
                break
            else:
                userInterface.get_user_input_number("\n Not Valid Choice Try again")