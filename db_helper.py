import pymysql

# Re-usable data base connection function
def con():
    return pymysql.connect(
        host="localhost", user="", password="", database="FauxDB"
    )


# Create the necessary tables for storing user data and notes
def create_db_tables():
    connection = con()
    with connection.cursor() as cursor:
        sql = (
            "CREATE TABLE IF NOT EXISTS `users` (`id` int(11) NOT NULL AUTO_INCREMENT,"
            "`username` varchar(255) COLLATE utf8_bin NOT NULL UNIQUE,"
            "`password` varchar(255) COLLATE utf8_bin NOT NULL, PRIMARY KEY (`id`))"
            "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1;"
        )
        cursor.execute(sql)

        sql = (
            "CREATE TABLE IF NOT EXISTS `notes`(`id` int(11) NOT NULL AUTO_INCREMENT,"
            "`date` varchar(255) COLLATE utf8_bin NOT NULL,"
            "`note` TEXT COLLATE utf8_bin NOT NULL,"
            "`user_id` int NOT NULL,"
            "INDEX notes_user_index(`user_id`),"
            "FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE, PRIMARY KEY (`id`))"
            "ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1;"
        )
        cursor.execute(sql)


# Check if the entered username and password match db records
def query_user_from_db(username, password):
    connection = con()
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `password` FROM `users` WHERE `username`=%s;"
            cursor.execute(sql, username)
            row = cursor.fetchone()
            if cursor.rowcount > 0:
                if password == row[0]:
                    return True
            return False


# Write username and password into the users table
def write_user_to_db(username, password):
    connection = con()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s);"
            # If the username already exists, we catch the Integrity Error and return False
            try:
                cursor.execute(sql, (username, password))
                connection.commit()
            except pymysql.err.IntegrityError:
                return False
            return True


# We write the note and the date to our notes table
# and set the user_id to match the username
def write_item(date, note, username):
    connection = con()
    cur_user = username

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `id` FROM `users` WHERE `username`=%s;"
            cursor.execute(sql, cur_user)
            cur_user_id = cursor.fetchone()

        with connection.cursor() as cursor:
            sql = (
                "INSERT INTO `notes` (`date`, `note`, `user_id`) "
                "VALUES (%s, %s, %s);"
            )
            cursor.execute(sql, (date, note, cur_user_id))
            connection.commit()
            return print("Note saved")


# We select the saved notes and dates relative to the user_id
# for the current username and return all the rows
def fetch_items(username):
    connection = con()
    cur_user = username

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `id` FROM `users` WHERE `username`=%s;"
            cursor.execute(sql, cur_user)
            cur_user_id = cursor.fetchone()

        with connection.cursor() as cursor:
            sql = "SELECT * FROM `notes` WHERE `user_id`=%s;"
            cursor.execute(sql, cur_user_id)
            all_items = cursor.fetchall()
            return all_items
