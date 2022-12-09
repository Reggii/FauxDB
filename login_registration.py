import db_helper
import write_fetch_notes


# Create a UserData object with username, password and authorization status
class UserData:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self._authorized = False

    @property
    def authorized(self):
        return self._authorized

    @authorized.setter
    def authorized(self, auth_feedback):
        self._authorized = auth_feedback


# Send a request to db_helper to check the username and password
# confirm if successful
def log_in(username, password):
    db_helper.create_db_tables()
    user = UserData(username, password)
    user.authorized = db_helper.query_user_from_db(username, password)

    if user.authorized:
        print("\nLogin Successful!\n")
        write_fetch_notes.query_user_for_action(username)
    if not user.authorized:
        print("\nLogin Unsuccessful\n" "Please restart and attempt again")


# Send a request to db_helper to write the username and password
# confirm if successful
def register(username, password):
    db_helper.create_db_tables()
    user = UserData(username, password)
    user.authorized = db_helper.write_user_to_db(username, password)

    if user.authorized:
        print("\nRegistration Successful!")
        write_fetch_notes.query_user_for_action(username)
    if not user.authorized:
        print("User already registered\n" "Please restart the application and log-in")
