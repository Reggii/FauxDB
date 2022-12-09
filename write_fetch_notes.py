import db_helper


# We initially ask the user to either write notes or fetch saved notes from db
def query_user_for_action(username):
    action = ""
    while not (action == "1" or action == "2"):
        action = input(
            f"Welcome {username}, please select an option (type the number):\n"
            f"1) Write new notes\n"
            f"2) See all your existing notes\n> "
        )
    if action == "1":
        query_user_for_note_data(username)
    if action == "2":
        fetch_notes(username)


# We ask for the note input and date then write it to db
def query_user_for_note_data(username):
    note = input("Please enter the note you want to save\n> ")
    date = input("Please enter the date for the note\n> ")
    db_helper.write_item(date, note, username)
    continue_or_quit(username)


# We fetch the saved notes from db, print all the rows out
# then call continue or quit to ask what action to take next
def fetch_notes(username):
    notes = db_helper.fetch_items(username)
    note_order = 1
    for note in notes:
        print(
            f"\nDate: {note[1]}\n" 
            f"Note #{note_order}: {note[2]}")
        note_order += 1
    continue_or_quit(username)


# We ask the user if they wish to: 
# continue with writing a new note, fetch existing notes, or quit
def continue_or_quit(username):
    action = ""
    while not (action == "1" or action == "2" or action == "3"):
        action = input(
            f"\nPlease select an option (type the number):\n"
            f"1) Write a new note\n"
            f"2) Fetch notes\n"
            f"3) Quit\n> "
        )
    if action == "1":
        query_user_for_note_data(username)
    elif action == "2":
        fetch_notes(username)
    elif action == "3":
        print("\n. . . . . . . \n" "E x i t i n g")
        return
