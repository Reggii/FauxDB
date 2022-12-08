import pymysql


def con():
    return pymysql.connect(
        host="localhost", user="", password="", database=""
    )


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


def write_user_to_db(username, password):
    connection = con()
    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `users` (`username`, `password`) VALUES (%s, %s);"
            try:
                cursor.execute(sql, (username, password))
                connection.commit()
            except pymysql.err.IntegrityError:
                return False
            return True


def write_item(date, note, username):
    connection = con()
    cur_user = username

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `id` FROM `users` WHERE `username`=%s;"
            cursor.execute(sql, cur_user)
            cur_user_id = cursor.fetchone()

        with connection.cursor() as cursor:
            sql = "INSERT INTO `notes` (`date`, `note`, `user_id`) " \
                  "VALUES (%s, %s, %s);"
            cursor.execute(sql, (date, note, cur_user_id))
            connection.commit()
            return print('Note saved')


def fetch_items(username):
    connection = con()
    cur_user = username

    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `id` FROM `users` WHERE `username`=%s;"
            cursor.execute(sql, cur_user)
            cur_user_id = cursor.fetchone()

        with connection.cursor() as cursor:
            sql = 'SELECT * FROM `notes` WHERE `user_id`=%s;'
            cursor.execute(sql, cur_user_id)
            all_items = cursor.fetchall()
            for row in all_items:
                print(f'\nDate: {row[1]}\n'
                      f'Note #{row[0]}: {row[2]}')

