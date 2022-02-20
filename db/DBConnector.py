import sqlite3
import pandas as pd

DATABASE = "database/apptdata.db"
DF_REQUEST = """SELECT DISTINCT latitude, longitude, fsa, round(avg(rent_price), 2) 
AS average_price FROM appt_rent_prices GROUP BY fsa;"""


class DBConnector:
    def __init__(self, dbpath):
        self.conn = sqlite3.connect(dbpath)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS appt_rent_prices(
        latitude TEXT,
        longitude TEXT,
        postal_code TEXT,
        fsa TEXT,
        rent_price INTEGER)""")

    def save_distinct_to_db(self, data):
        for i in data:
            self.cur.execute("""INSERT OR IGNORE INTO appt_rent_prices VALUES(?, ?, ?, ?, ?)""",
                             (i['latitude'], i['longitude'], i['postal_code'], i['fsa'], i['rent_price']))
            self.conn.commit()
            return i

    def get_data_frame(self):
        return pd.read_sql_query(DF_REQUEST, self.conn)
