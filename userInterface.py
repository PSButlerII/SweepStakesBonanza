import marketingFirm
import sweepStakes


def get_user_input_string(prompt):
    try:
        user_input = input(prompt)
        return user_input
    except ValueError:
        return input("Please enter words and letters")


def get_user_input_number(prompt):
    try:
        user_input = int(input(prompt))
        return user_input
    except ValueError:
        return int(input("Please enter a Number"))


def display_message(string):
    print(string)
    return string


def contestant_info(contestant):
    display_message(f"{len(contestant.Contestant.contestants)}.  {contestant.Contestant.contestants}")
    for contestant in contestant.Contestant.contestants:
        display_message(contestant)


# this is going to print the information about the contestant

def display_sweepstakes_info(self):
    for sweepstakes in self.marketingFirm.sweepstakes_storage:
        display_message(sweepstakes)


def display_sweepstakes_selection_menu(all_sweepstakes):
    display_message(
        f"{len(marketingFirm.MarketingFirm.sweepstakes_storage)}.  {marketingFirm.MarketingFirm.sweepstakes_storage}")
    sweepStakes.Sweepstakes.sweepstakes_menu(all_sweepstakes)


def display_marketing_firm_menu(marketing_firm_name):
    marketingFirm.MarketingFirm.marketing_firm_menu(marketing_firm_name)


def display_sweepstakes_menu_options(sweepstakes_name):
    sweepStakes.Sweepstakes.sweepstakes_menu(sweepstakes_name)
