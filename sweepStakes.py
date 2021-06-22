import userInterface


class Sweepstakes:
    def __init__(self, name):
        self.name = ''
        self.contestants = {}

    def register_contestant(self, contestant):
        contestant.first_name = userInterface.get_user_input_string("What is Your First Name?")
        contestant.last_name = userInterface.get_user_input_string("What is Your Last Name?")
        contestant.full_name = contestant.first_name + '' + contestant.last_name
        self.contestants.update(contestant.full_name)

    def pick_winner(self):  # should return a contestant
        pass

    def view_contestants(self):
        pass

    def menu(self):
        pass  # please picka menu
