import sweepStakes


class Contestants:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email_address = ''
        self.registration_number = '' # should equal the length of (sweepStakes.contestants)

    def notify(self, is_winner):
        pass
