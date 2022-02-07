import sqlite3

# TODO: Think over the db architecture and write more


class DBConnector:
    def __init__(self):
        self.con = sqlite3.connect("./db/database/realty.db")
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS flats(
        )
        """)

    def process_item(self, item):
        self.cur.execute("INSERT OR IGNORE INTO flats(?,?,?,?)", item)
        self.con.commit()
        return item

    def get_data_from_db(self):
        self.cur.execute("SELECT DISTINCT ....")
