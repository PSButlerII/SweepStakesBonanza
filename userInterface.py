@staticmethod
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

def send_user_menu_message(string):
    print(string)
    return print(string)

def send_user_print_message():


def contestant_info(contestant):
    pass


def display_sweepstakes_info(sweepstakes):
    pass


def display_sweepstakes_selection_menu(all_sweepstakes):
    pass


def display_marketing_firm_menu(marketing_firm_name):
    pass


def display_sweepstakes_menu_options(sweepstakes_name):
    pass
