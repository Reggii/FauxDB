import db_helper


def query_user_for_action(username):
    action = ''
    while not (action == '1' or action == '2'):
        action = input(
            f'Welcome {username}, please select an option (type the number):\n'
            f'1) Write new notes\n'
            f'2) See all your existing notes\n> '
        )
    if action == '1':
        query_user_for_note_data(username)
    if action == '2':
        fetch_notes(username)


def query_user_for_note_data(username):
    note = input(
        'Please enter the note you want to save\n> '
    )
    date = input(
        'Please enter the date for the note\n> '
    )
    db_helper.write_item(date, note, username)
    continue_or_quit(username)


def fetch_notes(username):
    db_helper.fetch_items(username)
    continue_or_quit(username)


def continue_or_quit(username):
    action = ''
    while not (action == '1' or action == '2' or action == '3'):
        action = input(
            f'\nPlease select an option (type the number):\n'
            f'1) Write new notes\n'
            f'2) Fetch notes\n'
            f'3) Quit\n> '
        )
    if action == '1':
        query_user_for_note_data(username)
    if action == '2':
        fetch_notes(username)
    if action == '3':
        print('\n. . . . . . . \n' 'E x i t i n g')
