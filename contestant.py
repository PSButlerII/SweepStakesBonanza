import sweepStakes
import userInterface


class Contestant:
    def __init__(self):
        self.first_name = userInterface.get_user_input_string("What is Your First Name?")
        self.last_name = userInterface.get_user_input_string("What is Your Last Name?")
        self.email_address = userInterface.get_user_input_string("What is Your Email Address?")
        self.registration_number = len({sweepStakes.Sweepstakes})

    def notify(self, is_winner):
        pass
