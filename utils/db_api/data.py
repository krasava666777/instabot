import sqlite3

class Database:
    def __init__(self, path_to_db):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = (), fetchone=False, fetchall=False, commit=False):
        connection = self.connection
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if not parameters:
            parameters = tuple()

        if commit:
            connection.commit()

        if fetchone:
            data = cursor.fetchone()

        if fetchall:
            data = cursor.fetchall()

        cursor.close()
        return data

    def create_table(self):
        sql = "CREATE TABLE IF NOT EXISTS users (username TEXT)"
        self.execute(sql, commit=True)

    def add_user(self, username: str):
        sql = "INSERT or IGNORE INTO users VALUES(?)"
        parameters = [username]
        self.execute(sql, parameters=parameters, commit=True)

    def remove_user(self, username: str):
        sql = "DELETE FROM users WHERE username=?"
        parameters = [username]
        self.execute(sql, parameters=parameters, commit=True)

    def get_all_users(self):
        sql = "SELECT username FROM users"
        return self.execute(sql, fetchall=True)

    def check_user(self, username):
        sql = "SELECT * FROM users WHERE username=?"
        parameters = [username]
        info = self.execute(sql, parameters=parameters, fetchone=True)
        return info is not None

    def count(self):
        sql = "SELECT COUNT(*) as count FROM users"
        return self.execute(sql, fetchone=True)
