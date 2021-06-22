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

    def menu(self):
        pass
