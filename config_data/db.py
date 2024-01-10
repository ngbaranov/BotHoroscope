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
                                newsletter INTEGER DEFAULT NULL                                 
                                )""")

