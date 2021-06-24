import sweepStakes
import userInterface


class MarketingFirm:
    sweepstakes_storage = []

    def __init__(self):
        self.name = "marketing_firm_name"


    def create_sweepstakes(self):
        sweepstake_name = userInterface.get_user_input_string("What is the Name of the Sweepstake?")
        self.sweepstakes_storage.append(sweepstake_name)
        MarketingFirm.marketing_firm_menu(self)

    def change_marketing_firm_name(self):
        self.name = userInterface.get_user_input_string("What is the Name of the Marketing Firm")




    def select_sweepstakes(self):
        userInterface.display_sweepstakes_selection_menu(self)
        all_sweepstakes = userInterface.get_user_input_number("Select a sweepstake number")
        # for all_sweepstakes in enumerate(MarketingFirm.sweepstakes_storage, start=1):
        all_sweepstakes.contestants.update([all_sweepstakes])
        sweepStakes.Sweepstakes.sweepstakes_menu(all_sweepstakes)
        return all_sweepstakes


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
