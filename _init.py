import login_registration as logreg


def query_user_for_action():
    user_action = ''
    while not (user_action == '1' or user_action == '2'):
        user_action = input(
            '\n - - - Faux DB - - - \n'
            'Please select an option (type the number):\n'
            '1) Log-in\n'
            '2) Register \n> ')
    return user_action


def query_user_for_data():
    user_name = input(
        '\nPlease provide your username:\n> '
    )
    user_pass = input(
        'Please provide your password:\n> '
    )
    return user_name, user_pass


if __name__ == '__main__':
    action = query_user_for_action()
    data = query_user_for_data()

    if action == '1':
        logreg.log_in(data[0],data[1])
    elif action == '2':
        result = logreg.register(data[0],data[1])

