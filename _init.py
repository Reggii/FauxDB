#! Python 3.10
# Launch from here
import login_registration as logreg


# We ask the user if they want to log-in or register
def query_user_for_action():
    user_action = ""
    while not (user_action == "1" or user_action == "2"):
        user_action = input(
            "\n - - - Faux DB - - - \n"
            "Please select an option (type the number):\n"
            "1) Log-in\n"
            "2) Register \n> "
        )
    return user_action


# We ask the user to privde their username and password
def query_user_for_data():
    user_name = input("\nPlease provide your username:\n> ")
    user_pass = input("Please provide your password:\n> ")
    return user_name, user_pass


if __name__ == "__main__":
    # Action returns '1' for log-in or '2' for register
    action = query_user_for_action()

    # Data returns a tuple of username at index 0 and password at index 1
    data = query_user_for_data()

    # If action is to log-in, call log_in from login_registration.py
    if action == "1":
        logreg.log_in(data[0], data[1])
    # If action is to register, call register from login_registration.py
    elif action == "2":
        result = logreg.register(data[0], data[1])
