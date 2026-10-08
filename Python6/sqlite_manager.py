import sqlite3


class SQLiteManager:

    def __init__(self):
        self.conn = sqlite3.connect("database.db")
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
        """)

        self.conn.commit()

    def add(self, name, age):
        self.cursor.execute(
            "INSERT INTO users(name, age) VALUES (?, ?)",
            (name, age)
        )

        self.conn.commit()

    def show(self):
        self.cursor.execute("SELECT * FROM users")

        for row in self.cursor.fetchall():
            print(row)