import sqlite3


class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self):
        with self.conn:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                                id INTEGER PRIMARY KEY,
                                user_id INTEGER,
                                user_name TEXT,
                                subscription TEXT                                 
                                )""")

    def user_exists(self, user_id):
        with self.conn:
            result = self.cursor.execute("SELECT * FROM user WHERE user_id = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def add_user(self, user_id, user_name, subscription=0):
        with self.conn:
            return self.cursor.execute("INSERT INTO user (user_id, user_name, subscription) VALUES (?, ?, ?)",
                                       (user_id, user_name, subscription))
